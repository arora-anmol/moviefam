# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='recommendation.proto',
  package='recommendation',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14recommendation.proto\x12\x0erecommendation\"@\n\rmovie_request\x12\x0b\n\x03\x61ge\x18\x01 \x01(\x01\x12\x12\n\nprofession\x18\x02 \x01(\t\x12\x0e\n\x06genres\x18\x03 \x03(\t\"1\n\x0emovie_response\x12\x0e\n\x06movies\x18\x01 \x03(\t\x12\x0f\n\x07ratings\x18\x02 \x03(\x05\x32[\n\nget_movies\x12M\n\nget_movies\x12\x1d.recommendation.movie_request\x1a\x1e.recommendation.movie_response\"\x00\x62\x06proto3')
)




_MOVIE_REQUEST = _descriptor.Descriptor(
  name='movie_request',
  full_name='recommendation.movie_request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='age', full_name='recommendation.movie_request.age', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='profession', full_name='recommendation.movie_request.profession', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='genres', full_name='recommendation.movie_request.genres', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=40,
  serialized_end=104,
)


_MOVIE_RESPONSE = _descriptor.Descriptor(
  name='movie_response',
  full_name='recommendation.movie_response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='movies', full_name='recommendation.movie_response.movies', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratings', full_name='recommendation.movie_response.ratings', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=106,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['movie_request'] = _MOVIE_REQUEST
DESCRIPTOR.message_types_by_name['movie_response'] = _MOVIE_RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

movie_request = _reflection.GeneratedProtocolMessageType('movie_request', (_message.Message,), dict(
  DESCRIPTOR = _MOVIE_REQUEST,
  __module__ = 'recommendation_pb2'
  # @@protoc_insertion_point(class_scope:recommendation.movie_request)
  ))
_sym_db.RegisterMessage(movie_request)

movie_response = _reflection.GeneratedProtocolMessageType('movie_response', (_message.Message,), dict(
  DESCRIPTOR = _MOVIE_RESPONSE,
  __module__ = 'recommendation_pb2'
  # @@protoc_insertion_point(class_scope:recommendation.movie_response)
  ))
_sym_db.RegisterMessage(movie_response)



_GET_MOVIES = _descriptor.ServiceDescriptor(
  name='get_movies',
  full_name='recommendation.get_movies',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=157,
  serialized_end=248,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_movies',
    full_name='recommendation.get_movies.get_movies',
    index=0,
    containing_service=None,
    input_type=_MOVIE_REQUEST,
    output_type=_MOVIE_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GET_MOVIES)

DESCRIPTOR.services_by_name['get_movies'] = _GET_MOVIES

# @@protoc_insertion_point(module_scope)