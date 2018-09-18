#!/usr/bin/env python
import os
from public import public


@public
def _map_files(path, followlinks=False):
    for root, dirs, files in os.walk(path, followlinks=followlinks):
        for _file in files:
            yield os.path.join(root, _file)


@public
def _map_dirs(path, followlinks=False):
    for root, dirs, files in os.walk(path, followlinks=followlinks):
        for _dir in dirs:
            yield os.path.join(root, _dir)


@public
def dirs(path, followlinks=False):
    return list(_map_dirs(path, followlinks))


@public
def files(path, followlinks=False):
    return list(_map_files(path, followlinks))
