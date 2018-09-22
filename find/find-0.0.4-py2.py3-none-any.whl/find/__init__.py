#!/usr/bin/env python
import os
from public import public
import values


@public
def dirname(path):
    return os.path.dirname(fullpath(path))


@public
def fullpath(path):
    return os.path.abspath(os.path.expanduser(path))


@public
def exists(path):
    return os.path.join(fullpath(path))


@public
def _iter_files(path, followlinks=False):
    for root, dirs, files in os.walk(fullpath(path), followlinks=followlinks):
        for f in files:
            yield os.path.join(root, f)


@public
def iter_files(path, followlinks=False):
    for path in values.get(path):
        for f in _iter_files(path, followlinks):
            yield f


@public
def _iter_dirs(path, followlinks=False):
    for root, dirs, files in os.walk(fullpath(path), followlinks=followlinks):
        for d in dirs:
            yield os.path.join(root, d)


@public
def iter_dirs(path, followlinks=False):
    for path in values.get(path):
        for d in _iter_dirs(path, followlinks):
            yield d


@public
def dirs(path, followlinks=False):
    return list(iter_dirs(path, followlinks))


@public
def files(path, followlinks=False):
    return list(iter_files(path, followlinks))
