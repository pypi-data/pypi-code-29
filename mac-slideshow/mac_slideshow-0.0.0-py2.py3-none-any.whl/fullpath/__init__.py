#!/usr/bin/env python
import os
from public import public


@public
def fullpath(path):
    if path is None:
        return None
    return os.path.abspath(os.path.expanduser(path))
