# coding: utf-8

import collections
import logging
from .jsonpath import search

logger = logging.getLogger(__name__)


def omit(d: dict, *args, keys=()):
    excludes = []
    excludes.extend(args)
    excludes.extend(keys)
    new = d.__class__()
    for k, v in d.items():
        if k not in excludes:
            new[k] = v
    return new


def pick(d: dict, *args, keys=(), ignore_error=True):
    includes = []
    includes.extend(args)
    includes.extend(keys)
    new = d.__class__()
    for k in includes:
        try:
            new[k] = d[k]
        except KeyError:
            if not ignore_error:
                raise
    return new


class AttrDict(dict):
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as err:
            raise AttributeError(err)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as err:
            raise AttributeError(err)

    def omit(self, *args, keys=()):
        return omit(self, *args, keys=keys)

    def pick(self, *args, keys=()):
        return pick(self, *args, keys=keys)

    def search(self, path, *args, **kwargs):
        return search(path, self, *args, **kwargs)


class AttrOrderedDict(collections.OrderedDict, AttrDict):
    def __repr__(self):
        return dict.__repr__(self)


class MissingAsNoneDict(dict):
    def __missing__(self, key):
        return None

    def __contains__(self, key):
        return True

