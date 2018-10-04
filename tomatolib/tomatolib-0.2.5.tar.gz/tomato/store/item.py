#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    @file:      item.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @auther:    tangmi(tangmi360@gmail.com)
    @date:      September 03, 2018
    @desc:      Simple extension to the dictionary
"""


class Item(dict):

    def __init__(self, callback=None):
        super(Item, self).__init__()
        self._data = {}
        self.callback = callback

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data.get(key, None)

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return str(self._data)

    __repr__ = __str__

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        if isinstance(data, dict):
            self._data = data

    def pop(self, key):
        return self._data.pop(key)
