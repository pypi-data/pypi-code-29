#! /usr/bin/env python
# coding: utf-8

import six

__author__ = '鹛桑够'

encoding = "utf-8"
second_encoding = "gb18030"


def decode(s):
    if isinstance(s, six.binary_type):
        try:
            return s.decode(encoding)
        except UnicodeError:
            return s.decode(second_encoding, "replace")
    if isinstance(s, (int, six.integer_types)):
        return "%s" % s
    return s


def encode(s):
    if isinstance(s, six.text_type):
        return s.encode(encoding)
    if isinstance(s, six.integer_types):
        return str(s)
    return s
