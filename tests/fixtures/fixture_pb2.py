# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fixtures/fixture.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fixtures/fixture.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_pb=_b('\n\x16\x66ixtures/fixture.proto\x12\x0fgoogle.protobuf\"(\n\x06Simple\x12\x0e\n\x06\x66ield1\x18\x01 \x01(\t\x12\x0e\n\x06\x66ield2\x18\x02 \x01(\t\"?\n\x05Outer\x12&\n\x05inner\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Simple\x12\x0e\n\x06\x66ield1\x18\x02 \x01(\t\"\x19\n\x07\x42undled\x12\x0e\n\x06\x66ield1\x18\x01 \x03(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIMPLE = _descriptor.Descriptor(
  name='Simple',
  full_name='google.protobuf.Simple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='google.protobuf.Simple.field1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field2', full_name='google.protobuf.Simple.field2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=83,
)


_OUTER = _descriptor.Descriptor(
  name='Outer',
  full_name='google.protobuf.Outer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inner', full_name='google.protobuf.Outer.inner', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field1', full_name='google.protobuf.Outer.field1', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=148,
)


_BUNDLED = _descriptor.Descriptor(
  name='Bundled',
  full_name='google.protobuf.Bundled',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field1', full_name='google.protobuf.Bundled.field1', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=175,
)

_OUTER.fields_by_name['inner'].message_type = _SIMPLE
DESCRIPTOR.message_types_by_name['Simple'] = _SIMPLE
DESCRIPTOR.message_types_by_name['Outer'] = _OUTER
DESCRIPTOR.message_types_by_name['Bundled'] = _BUNDLED

Simple = _reflection.GeneratedProtocolMessageType('Simple', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLE,
  __module__ = 'fixtures.fixture_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Simple)
  ))
_sym_db.RegisterMessage(Simple)

Outer = _reflection.GeneratedProtocolMessageType('Outer', (_message.Message,), dict(
  DESCRIPTOR = _OUTER,
  __module__ = 'fixtures.fixture_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Outer)
  ))
_sym_db.RegisterMessage(Outer)

Bundled = _reflection.GeneratedProtocolMessageType('Bundled', (_message.Message,), dict(
  DESCRIPTOR = _BUNDLED,
  __module__ = 'fixtures.fixture_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Bundled)
  ))
_sym_db.RegisterMessage(Bundled)


# @@protoc_insertion_point(module_scope)
