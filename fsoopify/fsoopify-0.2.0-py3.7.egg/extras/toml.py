#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

try:
    import toml
except ModuleNotFoundError as err:
    raise ModuleNotFoundError('\n'.join([
        f'{err}. try install it from pip:',
        f'    pip install toml'
    ]))

from ..nodes import FileInfo
from ..serialize import register_format

# pylint: disable=R0201,C0111

@register_format(__name__.split('.')[-1])
class TomlSerializer:

    def load(self, src: FileInfo, kwargs):
        return toml.loads(src.read_text(), **kwargs)

    def dump(self, src: FileInfo, obj, kwargs):
        return src.write_text(toml.dumps(obj, **kwargs), append=False)
