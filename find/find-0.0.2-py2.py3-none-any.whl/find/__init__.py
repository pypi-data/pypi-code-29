#!/usr/bin/env python
import os
from public import public


@public
def _map_files(path, followlinks=False):
    for root, dirs, files in os.walk(path, followlinks=followlinks):
        for file in files:
            yield os.path.join(root, file)


@public
def files(path, followlinks=False):
    # followlinks
    if not os.path.exists(path):
        return []
    return list(_map_files(path, followlinks))
