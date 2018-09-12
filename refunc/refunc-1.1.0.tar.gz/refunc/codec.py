# -*- coding: utf-8 -*-

import io
import json

from .interface import PayloadCodec


class JSONCodec(PayloadCodec):
    def to_bytes(self, obj):
        """
        return object as it will be mashal to json in ioloop
        """
        return obj

    def from_bytes(self, data: bytes):
        if len(data) == 0:
            return None
        return json.loads(data.decode('utf-8'))


__default_codec = JSONCodec()

__codec_registry = {}


def get_codec(endpoint: str) -> PayloadCodec:
    """
    returns a codec for given endpoint
    """
    if endpoint in __codec_registry:
        return __codec_registry[endpoint]

    parts = endpoint.split('/')
    if parts[0] and parts[0] in __codec_registry:
        return __codec_registry[parts[0]]

    # return default
    return __default_codec


def register_codec(endpoint_or_ns: str, pc: PayloadCodec):
    """
    register a new codec for endpoint(ns/name) or namespace
    """
    assert isinstance(pc, PayloadCodec)
    endpoint_or_ns = endpoint_or_ns.strip('/')
    __codec_registry[endpoint_or_ns] = _CodecWrapper(pc)


class _CodecWrapper(PayloadCodec):
    '''
    ensure to_bytes return None when object is None
    '''

    def __init__(self, parent: PayloadCodec, *args, **kwargs):
        super(*args, **kwargs)
        self.origin = parent

    def to_bytes(self, obj):
        if obj is None:
            return obj
        return self.origin.to_bytes(obj)

    def from_bytes(self, data: bytes):
        return self.origin.from_bytes(data)
