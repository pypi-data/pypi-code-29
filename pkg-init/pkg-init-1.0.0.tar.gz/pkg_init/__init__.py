# Copyright (c) 2018 bluelief.
# This source code is licensed under the MIT license.

from __future__ import absolute_import

from pkg_init.utils.version import get_version

VERSION = (1, 0, 0, 'final', 0)

__version__ = get_version(VERSION)
__all__ = ['pkg_init']
