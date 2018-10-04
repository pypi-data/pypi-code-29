#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      db_util.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    tangmi(tangmi360@gmail.com)
    @date:      September 04, 2018
    @desc:      Mongo Helper
"""

import os
import leveldb
from tomato.utils import singleton
from tomato.store import MongoClient
from tomato.store import RedisClient


@singleton
class MongoCliGlobal(MongoClient):

    def __init__(self, *args, **kwargs):
        MongoClient.__init__(self, *args, **kwargs)


@singleton
class RedisCliGlobal(RedisClient):

    def __init__(self, *args, **kwargs):
        RedisClient.__init__(self, *args, **kwargs)


@singleton
class LevelDBGlobal(object):
    def __init__(self, *args, **kwargs):
        exists_dir = os.path.exists(args[0])
        if not exists_dir:
            os.makedirs(args[0])
        self._leveldb = leveldb.LevelDB(*args, **kwargs)

    def __getattr__(self, attr):
        return getattr(self._leveldb, attr)
