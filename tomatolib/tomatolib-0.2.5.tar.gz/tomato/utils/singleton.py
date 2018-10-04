#!/usr/bin/python3
# -*- coding:utf-8 -*-


def singleton(cls):
    _instances = {}
    def _singleton(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]
    return _singleton
