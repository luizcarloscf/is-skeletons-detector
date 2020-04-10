import re
import time
import dateutil.parser as dp

from is_wire.core import Subscription, Message, Logger, Tracer, AsyncTransport
from opencensus.ext.zipkin.trace_exporter import ZipkinExporter
from is_msgs.image_pb2 import Image
from prometheus_client import start_http_server, Gauge

from .stream_channel import StreamChannel
from .skeletons import SkeletonsDetector
from .utils import load_options, get_np_image, get_pb_image, draw_skeletons


def span_duration_ms(span):
    dt = dp.parse(span.end_time) - dp.parse(span.start_time)
    return dt.total_seconds() * 1000.0


def create_exporter(service_name, uri):
    log = Logger(name="CreateExporter")
    zipkin_ok = re.match("http:\\/\\/([a-zA-Z0-9\\.]+)(:(\\d+))?", uri)
    if not zipkin_ok:
        log.critical("Invalid zipkin uri \"{}\", expected http://<hostname>:<port>", uri)
    exporter = ZipkinExporter(
        service_name=service_name,
        host_name=zipkin_ok.group(1),
        port=zipkin_ok.group(3),
        transport=AsyncTransport)
    return exporter


def main():
    service_name = 'SkeletonsDetector.Detection'
    re_topic = re.compile(r'CameraGateway.(\w+).Frame')

    op = load_options()
    sd = SkeletonsDetector(op)

    log = Logger(name=service_name)
    channel = StreamChannel(op.broker_uri)
    log.info('Connected to broker {}', op.broker_uri)

    exporter = create_exporter(service_name=service_name, uri=op.zipkin_uri)
    
    skeletons_detected = Gauge("skeletons",
                               "Skeletons detected by any camera")
    skeletons_detected.set(0.0)
    start_http_server(8080)

    buffer = list()
    initial_time = time.time()

    subscription = Subscription(channel=channel, name=service_name)
    subscription.subscribe('CameraGateway.*.Frame')

    while True:
        msg, dropped = channel.consume(return_dropped=True)

        tracer = Tracer(exporter, span_context=msg.extract_tracing())
        span = tracer.start_span(name='detection_and_render')
        detection_span = None

        with tracer.span(name='unpack'):
            im = msg.unpack(Image)
            im_np = get_np_image(im)
        with tracer.span(name='detection') as _span:
            skeletons = sd.detect(im_np)
            detection_span = _span
        with tracer.span(name='pack_and_publish_detections'):
            sks_msg = Message()
            sks_msg.topic = re_topic.sub(r'SkeletonsDetector.\1.Detection', msg.topic)
            sks_msg.inject_tracing(span)
            sks_msg.pack(skeletons)
            channel.publish(sks_msg)
        with tracer.span(name='render_pack_publish_expose'):
            im_rendered = draw_skeletons(im_np, skeletons)
            rendered_msg = Message()
            rendered_msg.topic = re_topic.sub(r'SkeletonsDetector.\1.Rendered', msg.topic)
            rendered_msg.pack(get_pb_image(im_rendered))
            channel.publish(rendered_msg)
            buffer.append(len(skeletons.objects))
            if (time.time() - initial_time) > op.period and len(buffer) > 0:
                log.info('metric = {:5.2f}',sum(buffer) / len(buffer))
                skeletons_detected.set(sum(buffer) / len(buffer))
                buffer = []
                initial_time = time.time()

        span.add_attribute('Detections', len(skeletons.objects))
        tracer.end_span()
        log.info('detections = {:2d}, dropped_messages = {:2d}', len(skeletons.objects), dropped)
        log.info('took_ms = {{ detection: {:5.2f}, service: {:5.2f}}}',
                 span_duration_ms(detection_span), span_duration_ms(span))


if __name__ == "__main__":
    main()