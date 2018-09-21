# coding=utf-8
"""
Computes hashes
"""

import hashlib

from elib import custom_logging

LOGGER = custom_logging.get_logger('ELIB')


def get_hash(data, method: str = 'md5') -> str:
    """
    Computes hash from data

    Args:
        data: data
        method: hash method (defaults to MD5) One of [sha1, sha224, sha256, sha384, sha512, blake2b, blake2s]

    Returns: hash value

    """
    if not isinstance(data, bytes):
        try:
            data = bytes(data, 'utf-8')
        except ValueError:
            raise ValueError(f'cannot cast {type(data)} to bytes implicitly')

    try:
        func = getattr(hashlib, method)
    except AttributeError:
        raise AttributeError('cannot find method "{}" in hashlib'.format(method))
    else:
        hash_ = func(data).hexdigest()
        LOGGER.debug('hash for binary data: %s', hash_)

        return hash_
