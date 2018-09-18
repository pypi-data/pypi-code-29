# -*- coding: utf-8 -*-
#
# Copyright (c) 2018~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

_FORMAT_MAP = {
    '.json' : 'json',
    '.json5': 'json5',
    '.yaml' : 'yaml',
    '.toml' : 'toml',
}

_REGISTERED_SERIALIZERS = {}

class FormatNotFoundError(Exception):
    pass


class SerializeError(Exception):
    pass


def _detect_format(file_info):
    ext = file_info.path.name.ext
    try:
        return _FORMAT_MAP[ext.lower()]
    except KeyError:
        raise FormatNotFoundError(f'cannot detect format from ext "{ext}".')

def load(file_info, format=None, *, kwargs={}):
    if format is None:
        format = _detect_format(file_info)
    serializer = _load_serializer(format)
    try:
        return serializer.load(file_info, kwargs)
    except Exception as err:
        raise SerializeError(err)

def dump(file_info, obj, format=None, *, kwargs={}):
    if format is None:
        format = _detect_format(file_info)
    serializer = _load_serializer(format)
    try:
        return serializer.dump(file_info, obj, kwargs)
    except Exception as err:
        raise SerializeError(err)

def register_format(name):
    '''
    register a serializer for load and dump.
    '''
    def decorator(cls):
        _REGISTERED_SERIALIZERS[name] = cls
        return cls
    return decorator

def _load_serializer(format):
    if not isinstance(format, str):
        raise TypeError(f'format must be str.')

    if format not in _REGISTERED_SERIALIZERS:
        import importlib
        try:
            importlib.import_module('.extras.' + format, 'fsoopify')
        except ImportError:
            _REGISTERED_SERIALIZERS[format] = None

    cls = _REGISTERED_SERIALIZERS.get(format)
    if cls is None:
        raise FormatNotFoundError(f'unknown format: {format}')
    return cls()
