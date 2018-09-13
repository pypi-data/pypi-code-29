#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : config.py
# @Date : 2018/9/4 9:38
# @Author: donghaixing
# Do have a faith in what you're doing.
# Make your life a story worth telling.


from collections import Mapping
import copy
import json
import os
import fnmatch
from tornado_rest.config.config import CONFIG_OPTS


def walk_dir(dir_path, pattern):
    result = []
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            filename = os.path.join(root, name)
            if fnmatch.fnmatch(filename, pattern):
                result.append(filename)
    return result


class ValueNotSet(object):
    pass


class Config(Mapping):

    def __init__(self, opts):
        self._opts = opts or {}

    def from_files(self, opt_files, ignore_undefined):

        def _update(data_src, data_dst, ignore_undefined):
            if ignore_undefined:
                for key, value in data_src.items():
                    if isinstance(value, dict):
                        _update(value, data_dst.get(key, {}), ignore_undefined)
                    elif key in data_dst:
                        data_src[key] = data_dst[key]
            else:
                for key, value in data_dst.items():
                    if isinstance(value, dict):
                        if key in data_src:
                            _update(data_src[key], data_dst.get(key, {}), ignore_undefined)
                        else:
                            new_value = {}
                            data_src[key] = new_value
                            _update(new_value, data_dst.get(key, {}), ignore_undefined)
                    else:
                        data_src[key] = data_dst[key]

        def _check(data, name=None):
            for key, value in data.items():
                cur_name = copy.deepcopy(name) if name else []
                cur_name.append(key)
                if isinstance(value, dict):
                    _check(value, name=cur_name)
                if isinstance(value, ValueNotSet):
                    invalid_key = '.'.join(cur_name)
                    raise ValueError("config item: %s not set" % invalid_key)

        for opt_file in opt_files:
            with open(opt_file, 'r') as f:
                _update(self._opts, json.load(f), ignore_undefined)
        _check(self._opts)

    def __getattr__(self, name):
        try:
            value = self._opts[name]
            if isinstance(value, dict):
                return Config(value)
            return value
        except KeyError:
            raise AttributeError("No Such Option: %s" % name)

    def __getitem__(self, key):
        return self._opts[key]

    def __contains__(self, key):
        return key in self._opts

    def __iter__(self):
        for key in self._opts.keys():
            yield key

    def __len__(self):
        return len(self._opts)

    def iterkeys(self):
        'D.iterkeys() -> an iterator over the keys of D'
        return iter(self._opts)

    def itervalues(self):
        'D.itervalues() -> an iterator over the values of D'
        for key in self._opts:
            yield self._opts[key]

    def iteritems(self):
        'D.iteritems() -> an iterator over the (key, value) items of D'
        for key in self._opts:
            yield (key, self._opts[key])

    def keys(self):
        "D.keys() -> list of D's keys"
        return list(self._opts)

    def items(self):
        "D.items() -> list of D's (key, value) pairs, as 2-tuples"
        return [(key, self._opts[key]) for key in self._opts]

    def values(self):
        "D.values() -> list of D's values"
        return [self._opts[key] for key in self._opts]


class Configuration(object):
    def __init__(self, config):
        self._config = config

    def __repr__(self):
        return str(self._config)

    def __getattr__(self, attr):
        return getattr(self._config, attr)

    def __call__(self, config):
        self._config = config


def setup():
    default_opts = CONFIG_OPTS

    config = Config(copy.deepcopy(default_opts))
    CONF(config)


UNSET = ValueNotSet()

CONF = Configuration(None)
