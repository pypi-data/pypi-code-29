# -*- coding: utf-8 -*-
"""
TenetAccount utility functions.
"""

import hashlib


def sizeof_fmt(num_in_bytes):
    """
    Converts bytes into human readable format (e.g., 1K 234M 2G)

    @param num_in_bytes: Number in bytes
    @type num_in_bytes: **any** numeric type

    @rtype: string
    @return: Bytes into human readable format (e.g., 1K 234M 2G)
    """
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB']:
        if abs(num_in_bytes) < 1024.0:
            return "%3.1f %s" % (num_in_bytes, unit)
        num_in_bytes /= 1024.0
    return "%.1f %s" % (num_in_bytes, 'YiB')


def password_to_hash(password):
    """
    Generates the MD5 hash of password.

    @param password: Password
    @type password: string

    @rtype: string
    @return: MD5 hash of password
    """
    return hashlib.md5(password).hexdigest()
