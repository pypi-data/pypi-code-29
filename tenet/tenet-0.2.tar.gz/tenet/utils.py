# -*- coding: utf-8 -*-
import hashlib


def sizeof_fmt(num):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB']:
        if abs(num) < 1024.0:
            return "%3.1f %s" % (num, unit)
        num /= 1024.0
    return "%.1f %s" % (num, 'YiB')


def password_to_hash(password):
    return hashlib.md5(password).hexdigest()
