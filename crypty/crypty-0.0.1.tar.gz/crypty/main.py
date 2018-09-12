#!/usr/bin/env python

from cryptography.fernet import Fernet


def encrypt(s, key=None):
    """Takes UTF-8 string and spits UTF-8 token"""
    if key is None:
        key = Fernet.generate_key()
    f = Fernet(to_bytes(key))
    token = f.encrypt(to_bytes(s))
    s_key, s_token = key.decode('utf8'), token.decode('utf8')
    return s_key, s_token


def decrypt(token, key):
    """Takes token in UTF-8 (or bytestring) and spits UTF-8 string"""
    f = Fernet(to_bytes(key))
    bytes = f.decrypt(to_bytes(token))
    return bytes.decode('utf8')


def to_bytes(str_bytes):
    """Takes UTF-8 string or bytes and safely spits out bytes"""
    try:
        bytes = str_bytes.encode('utf8')
    except AttributeError:
        return str_bytes
    return bytes
