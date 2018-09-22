#!/usr/bin/env python
from public import public
import this_is


@public
def get(input):
    if input is None:
        return []
    if not this_is.iterable(input) or this_is.string(input):
        return [input]
    return list(input)
