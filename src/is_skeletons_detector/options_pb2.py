# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='options.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\roptions.proto\"\xfa\x02\n\x18SkeletonsDetectorOptions\x12\x12\n\nbroker_uri\x18\x01 \x01(\t\x12\x12\n\nzipkin_uri\x18\x02 \x01(\t\x12.\n\x05model\x18\x03 \x01(\x0e\x32\x1f.SkeletonsDetectorOptions.Model\x12\x30\n\x06resize\x18\x04 \x01(\x0b\x32 .SkeletonsDetectorOptions.Resize\x12\x18\n\x10resize_out_ratio\x18\x05 \x01(\x01\x12\x14\n\x0crender_topic\x18\x06 \x01(\r\x12\x1c\n\x14gpu_mem_allow_growth\x18\x07 \x01(\x08\x12\'\n\x1fper_process_gpu_memory_fraction\x18\x08 \x01(\x01\x12\x0e\n\x06period\x18\t \x01(\x01\x1a\'\n\x06Resize\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\"$\n\x05Model\x12\x07\n\x03\x43MU\x10\x00\x12\x12\n\x0eMOBILENET_THIN\x10\x01\x62\x06proto3')
)



_SKELETONSDETECTOROPTIONS_MODEL = _descriptor.EnumDescriptor(
  name='Model',
  full_name='SkeletonsDetectorOptions.Model',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CMU', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOBILENET_THIN', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=360,
  serialized_end=396,
)
_sym_db.RegisterEnumDescriptor(_SKELETONSDETECTOROPTIONS_MODEL)


_SKELETONSDETECTOROPTIONS_RESIZE = _descriptor.Descriptor(
  name='Resize',
  full_name='SkeletonsDetectorOptions.Resize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='SkeletonsDetectorOptions.Resize.width', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='SkeletonsDetectorOptions.Resize.height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=358,
)

_SKELETONSDETECTOROPTIONS = _descriptor.Descriptor(
  name='SkeletonsDetectorOptions',
  full_name='SkeletonsDetectorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='broker_uri', full_name='SkeletonsDetectorOptions.broker_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zipkin_uri', full_name='SkeletonsDetectorOptions.zipkin_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='SkeletonsDetectorOptions.model', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resize', full_name='SkeletonsDetectorOptions.resize', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resize_out_ratio', full_name='SkeletonsDetectorOptions.resize_out_ratio', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='render_topic', full_name='SkeletonsDetectorOptions.render_topic', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gpu_mem_allow_growth', full_name='SkeletonsDetectorOptions.gpu_mem_allow_growth', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='per_process_gpu_memory_fraction', full_name='SkeletonsDetectorOptions.per_process_gpu_memory_fraction', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='SkeletonsDetectorOptions.period', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SKELETONSDETECTOROPTIONS_RESIZE, ],
  enum_types=[
    _SKELETONSDETECTOROPTIONS_MODEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=396,
)

_SKELETONSDETECTOROPTIONS_RESIZE.containing_type = _SKELETONSDETECTOROPTIONS
_SKELETONSDETECTOROPTIONS.fields_by_name['model'].enum_type = _SKELETONSDETECTOROPTIONS_MODEL
_SKELETONSDETECTOROPTIONS.fields_by_name['resize'].message_type = _SKELETONSDETECTOROPTIONS_RESIZE
_SKELETONSDETECTOROPTIONS_MODEL.containing_type = _SKELETONSDETECTOROPTIONS
DESCRIPTOR.message_types_by_name['SkeletonsDetectorOptions'] = _SKELETONSDETECTOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SkeletonsDetectorOptions = _reflection.GeneratedProtocolMessageType('SkeletonsDetectorOptions', (_message.Message,), dict(

  Resize = _reflection.GeneratedProtocolMessageType('Resize', (_message.Message,), dict(
    DESCRIPTOR = _SKELETONSDETECTOROPTIONS_RESIZE,
    __module__ = 'options_pb2'
    # @@protoc_insertion_point(class_scope:SkeletonsDetectorOptions.Resize)
    ))
  ,
  DESCRIPTOR = _SKELETONSDETECTOROPTIONS,
  __module__ = 'options_pb2'
  # @@protoc_insertion_point(class_scope:SkeletonsDetectorOptions)
  ))
_sym_db.RegisterMessage(SkeletonsDetectorOptions)
_sym_db.RegisterMessage(SkeletonsDetectorOptions.Resize)


# @@protoc_insertion_point(module_scope)