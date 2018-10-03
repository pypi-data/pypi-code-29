# -*- coding: utf-8 -*-

try:
    from secrets import token_urlsafe as make_secret
except ImportError:
    import random

    def make_secret(length):
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz'
                                     'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                     '1234567890&~{([-|_^)]}%$*')
                       for x in range(length))
from jinja2 import nodes, lexer
from jinja2.ext import Extension


class SecretExtension(Extension):
    # a set of names that trigger the extension.
    tags = set(['get_secret'])

    def parse(self, parser):
        lineno = next(parser.stream).lineno

        length = parser.stream.expect(lexer.TOKEN_INTEGER).value

        secret = nodes.Const(self._get_secret(length))
        return nodes.Output([secret], lineno=lineno)

    def _get_secret(self, length):
        return make_secret(length)
