# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: text-data.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0ftext-data.proto\x12\ttext_data"\x1b\n\tSemantics\x12\x0e\n\x06values\x18\x01 \x03(\r"B\n\x08Sentence\x12\r\n\x05texts\x18\x01 \x03(\t\x12\'\n\tsemantics\x18\x03 \x03(\x0b\x32\x14.text_data.Semantics"P\n\x08TextData\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12&\n\tsentences\x18\x04 \x03(\x0b\x32\x13.text_data.Sentence"Q\n\x0bSampledData\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12$\n\x07samples\x18\x03 \x03(\x0b\x32\x13.text_data.Sentenceb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "text_data_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_SEMANTICS"]._serialized_start = 30
    _globals["_SEMANTICS"]._serialized_end = 57
    _globals["_SENTENCE"]._serialized_start = 59
    _globals["_SENTENCE"]._serialized_end = 125
    _globals["_TEXTDATA"]._serialized_start = 127
    _globals["_TEXTDATA"]._serialized_end = 207
    _globals["_SAMPLEDDATA"]._serialized_start = 209
    _globals["_SAMPLEDDATA"]._serialized_end = 290
# @@protoc_insertion_point(module_scope)
