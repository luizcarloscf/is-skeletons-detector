#pragma once

#include <string>
#include <regex>
#include <algorithm>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include "is/msgs/utils.hpp"
#include "is/msgs/image.pb.h"
#include "is/wire/core.hpp"
#include "zipkin/opentracing.h"
#include "options.pb.h"

using namespace zipkin;
using namespace opentracing;

is::SkeletonsDetectorOptions load_options(int argc, char** argv);

int64_t get_topic_id(std::string const& topic);

void render_skeletons(cv::Mat& cv_image,
                      is::vision::ObjectAnnotations const& skeletons,
                      is::vision::Image* pb_image = nullptr);

std::shared_ptr<opentracing::Tracer> make_tracer(is::SkeletonsDetectorOptions const& options,
                                                 std::string const& service_name);
class StreamChannel {
 public:
  StreamChannel(std::string const& uri) : channel(uri) {}
  is::Channel& internal_channel() { return this->channel; }
  void publish(std::string const& topic, is::Message const& message);
  is::Message consume_last(int* dropped = nullptr);

 private:
  is::Channel channel;
};