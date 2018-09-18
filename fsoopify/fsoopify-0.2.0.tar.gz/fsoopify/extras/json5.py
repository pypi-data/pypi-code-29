#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

try:
    import json5
except ModuleNotFoundError as err:
    raise ModuleNotFoundError('\n'.join([
        f'{err}. try install it from pip:',
        f'    pip install json5'
    ]))

from ..nodes import FileInfo
from ..serialize import register_format

# pylint: disable=R0201,C0111

@register_format(__name__.split('.')[-1])
class Json5Serializer:

    def load(self, src: FileInfo, kwargs):
        return json5.loads(src.read_text(), **kwargs)

    def dump(self, src: FileInfo, obj, kwargs):
        return src.write_text(json5.dumps(obj, **kwargs), append=False)
