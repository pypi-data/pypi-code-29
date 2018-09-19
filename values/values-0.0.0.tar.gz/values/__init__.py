#!/usr/bin/env python
from public import public
import this_is

@public
def get(value=None):
    if not value:
        return []
    if not this_is.iterable(value) or this_is.string(value):
        return [value]
    return list(value)

