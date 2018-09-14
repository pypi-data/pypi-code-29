#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """

property
--------

Custom Property decorator.

"""


class classproperty:
    """
    Decorator to set a property as classmethod.
    Work only as getter.

    usage: @classproperty.
    """
    def __init__(self, fget=None, doc=None):
        self.fget = fget
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(objtype)

    def getter(self, fget):
        return type(self)(fget, self.__doc__)


class staticproperty:
    """
    Decorator to set a property as staticmethod.
    Work only as getter.

    usage: @staticproperty.
    """
    def __init__(self, fget=None, doc=None):
        self.fget = fget
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget()

    def getter(self, fget):
        return type(self)(fget, self.__doc__)
