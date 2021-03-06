# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kms.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import blockchain_pb2 as blockchain__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='kms.proto',
  package='kms',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tkms.proto\x12\x03kms\x1a\x0c\x63ommon.proto\x1a\x10\x62lockchain.proto\"\x87\x01\n\x15GetCryptoInfoResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.common.StatusCode\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08hash_len\x18\x03 \x01(\r\x12\x15\n\rsignature_len\x18\x04 \x01(\r\x12\x13\n\x0b\x61\x64\x64ress_len\x18\x05 \x01(\r\"-\n\x16GenerateKeyPairRequest\x12\x13\n\x0b\x44\x65scription\x18\x01 \x01(\t\":\n\x17GenerateKeyPairResponse\x12\x0e\n\x06key_id\x18\x01 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\"\x1f\n\x0fHashDataRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"3\n\x15VerifyDataHashRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\"1\n\x12SignMessageRequest\x12\x0e\n\x06key_id\x18\x01 \x01(\x04\x12\x0b\n\x03msg\x18\x02 \x01(\x0c\"L\n\x13SignMessageResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.common.StatusCode\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"9\n\x17RecoverSignatureRequest\x12\x0b\n\x03msg\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"O\n\x18RecoverSignatureResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.common.StatusCode\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0c\x32\xe9\x03\n\nKmsService\x12:\n\rGetCryptoInfo\x12\r.common.Empty\x1a\x1a.kms.GetCryptoInfoResponse\x12L\n\x0fGenerateKeyPair\x12\x1b.kms.GenerateKeyPairRequest\x1a\x1c.kms.GenerateKeyPairResponse\x12\x36\n\x08HashData\x12\x14.kms.HashDataRequest\x1a\x14.common.HashResponse\x12@\n\x0eVerifyDataHash\x12\x1a.kms.VerifyDataHashRequest\x1a\x12.common.StatusCode\x12@\n\x0bSignMessage\x12\x17.kms.SignMessageRequest\x1a\x18.kms.SignMessageResponse\x12O\n\x10RecoverSignature\x12\x1c.kms.RecoverSignatureRequest\x1a\x1d.kms.RecoverSignatureResponse\x12\x44\n\x11\x43heckTransactions\x12\x1b.blockchain.RawTransactions\x1a\x12.common.StatusCodeb\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,blockchain__pb2.DESCRIPTOR,])




_GETCRYPTOINFORESPONSE = _descriptor.Descriptor(
  name='GetCryptoInfoResponse',
  full_name='kms.GetCryptoInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='kms.GetCryptoInfoResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='kms.GetCryptoInfoResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash_len', full_name='kms.GetCryptoInfoResponse.hash_len', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature_len', full_name='kms.GetCryptoInfoResponse.signature_len', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address_len', full_name='kms.GetCryptoInfoResponse.address_len', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=51,
  serialized_end=186,
)


_GENERATEKEYPAIRREQUEST = _descriptor.Descriptor(
  name='GenerateKeyPairRequest',
  full_name='kms.GenerateKeyPairRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Description', full_name='kms.GenerateKeyPairRequest.Description', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=188,
  serialized_end=233,
)


_GENERATEKEYPAIRRESPONSE = _descriptor.Descriptor(
  name='GenerateKeyPairResponse',
  full_name='kms.GenerateKeyPairResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='kms.GenerateKeyPairResponse.key_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='kms.GenerateKeyPairResponse.address', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=235,
  serialized_end=293,
)


_HASHDATAREQUEST = _descriptor.Descriptor(
  name='HashDataRequest',
  full_name='kms.HashDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='kms.HashDataRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=295,
  serialized_end=326,
)


_VERIFYDATAHASHREQUEST = _descriptor.Descriptor(
  name='VerifyDataHashRequest',
  full_name='kms.VerifyDataHashRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='kms.VerifyDataHashRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hash', full_name='kms.VerifyDataHashRequest.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=328,
  serialized_end=379,
)


_SIGNMESSAGEREQUEST = _descriptor.Descriptor(
  name='SignMessageRequest',
  full_name='kms.SignMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_id', full_name='kms.SignMessageRequest.key_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='kms.SignMessageRequest.msg', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=381,
  serialized_end=430,
)


_SIGNMESSAGERESPONSE = _descriptor.Descriptor(
  name='SignMessageResponse',
  full_name='kms.SignMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='kms.SignMessageResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='kms.SignMessageResponse.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=432,
  serialized_end=508,
)


_RECOVERSIGNATUREREQUEST = _descriptor.Descriptor(
  name='RecoverSignatureRequest',
  full_name='kms.RecoverSignatureRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='kms.RecoverSignatureRequest.msg', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='signature', full_name='kms.RecoverSignatureRequest.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=510,
  serialized_end=567,
)


_RECOVERSIGNATURERESPONSE = _descriptor.Descriptor(
  name='RecoverSignatureResponse',
  full_name='kms.RecoverSignatureResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='kms.RecoverSignatureResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='kms.RecoverSignatureResponse.address', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=569,
  serialized_end=648,
)

_GETCRYPTOINFORESPONSE.fields_by_name['status'].message_type = common__pb2._STATUSCODE
_SIGNMESSAGERESPONSE.fields_by_name['status'].message_type = common__pb2._STATUSCODE
_RECOVERSIGNATURERESPONSE.fields_by_name['status'].message_type = common__pb2._STATUSCODE
DESCRIPTOR.message_types_by_name['GetCryptoInfoResponse'] = _GETCRYPTOINFORESPONSE
DESCRIPTOR.message_types_by_name['GenerateKeyPairRequest'] = _GENERATEKEYPAIRREQUEST
DESCRIPTOR.message_types_by_name['GenerateKeyPairResponse'] = _GENERATEKEYPAIRRESPONSE
DESCRIPTOR.message_types_by_name['HashDataRequest'] = _HASHDATAREQUEST
DESCRIPTOR.message_types_by_name['VerifyDataHashRequest'] = _VERIFYDATAHASHREQUEST
DESCRIPTOR.message_types_by_name['SignMessageRequest'] = _SIGNMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['SignMessageResponse'] = _SIGNMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['RecoverSignatureRequest'] = _RECOVERSIGNATUREREQUEST
DESCRIPTOR.message_types_by_name['RecoverSignatureResponse'] = _RECOVERSIGNATURERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCryptoInfoResponse = _reflection.GeneratedProtocolMessageType('GetCryptoInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCRYPTOINFORESPONSE,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.GetCryptoInfoResponse)
  })
_sym_db.RegisterMessage(GetCryptoInfoResponse)

GenerateKeyPairRequest = _reflection.GeneratedProtocolMessageType('GenerateKeyPairRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYPAIRREQUEST,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.GenerateKeyPairRequest)
  })
_sym_db.RegisterMessage(GenerateKeyPairRequest)

GenerateKeyPairResponse = _reflection.GeneratedProtocolMessageType('GenerateKeyPairResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATEKEYPAIRRESPONSE,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.GenerateKeyPairResponse)
  })
_sym_db.RegisterMessage(GenerateKeyPairResponse)

HashDataRequest = _reflection.GeneratedProtocolMessageType('HashDataRequest', (_message.Message,), {
  'DESCRIPTOR' : _HASHDATAREQUEST,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.HashDataRequest)
  })
_sym_db.RegisterMessage(HashDataRequest)

VerifyDataHashRequest = _reflection.GeneratedProtocolMessageType('VerifyDataHashRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYDATAHASHREQUEST,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.VerifyDataHashRequest)
  })
_sym_db.RegisterMessage(VerifyDataHashRequest)

SignMessageRequest = _reflection.GeneratedProtocolMessageType('SignMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _SIGNMESSAGEREQUEST,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.SignMessageRequest)
  })
_sym_db.RegisterMessage(SignMessageRequest)

SignMessageResponse = _reflection.GeneratedProtocolMessageType('SignMessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _SIGNMESSAGERESPONSE,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.SignMessageResponse)
  })
_sym_db.RegisterMessage(SignMessageResponse)

RecoverSignatureRequest = _reflection.GeneratedProtocolMessageType('RecoverSignatureRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOVERSIGNATUREREQUEST,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.RecoverSignatureRequest)
  })
_sym_db.RegisterMessage(RecoverSignatureRequest)

RecoverSignatureResponse = _reflection.GeneratedProtocolMessageType('RecoverSignatureResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOVERSIGNATURERESPONSE,
  '__module__' : 'kms_pb2'
  # @@protoc_insertion_point(class_scope:kms.RecoverSignatureResponse)
  })
_sym_db.RegisterMessage(RecoverSignatureResponse)



_KMSSERVICE = _descriptor.ServiceDescriptor(
  name='KmsService',
  full_name='kms.KmsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=651,
  serialized_end=1140,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCryptoInfo',
    full_name='kms.KmsService.GetCryptoInfo',
    index=0,
    containing_service=None,
    input_type=common__pb2._EMPTY,
    output_type=_GETCRYPTOINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GenerateKeyPair',
    full_name='kms.KmsService.GenerateKeyPair',
    index=1,
    containing_service=None,
    input_type=_GENERATEKEYPAIRREQUEST,
    output_type=_GENERATEKEYPAIRRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='HashData',
    full_name='kms.KmsService.HashData',
    index=2,
    containing_service=None,
    input_type=_HASHDATAREQUEST,
    output_type=common__pb2._HASHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='VerifyDataHash',
    full_name='kms.KmsService.VerifyDataHash',
    index=3,
    containing_service=None,
    input_type=_VERIFYDATAHASHREQUEST,
    output_type=common__pb2._STATUSCODE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SignMessage',
    full_name='kms.KmsService.SignMessage',
    index=4,
    containing_service=None,
    input_type=_SIGNMESSAGEREQUEST,
    output_type=_SIGNMESSAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RecoverSignature',
    full_name='kms.KmsService.RecoverSignature',
    index=5,
    containing_service=None,
    input_type=_RECOVERSIGNATUREREQUEST,
    output_type=_RECOVERSIGNATURERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CheckTransactions',
    full_name='kms.KmsService.CheckTransactions',
    index=6,
    containing_service=None,
    input_type=blockchain__pb2._RAWTRANSACTIONS,
    output_type=common__pb2._STATUSCODE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KMSSERVICE)

DESCRIPTOR.services_by_name['KmsService'] = _KMSSERVICE

# @@protoc_insertion_point(module_scope)
