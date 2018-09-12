#! /usr/bin/env python
# coding: utf-8

from functools import partial
import base64
from crypt import crypt
import hashlib

__author__ = '鹛桑够'


def verify_plain(plain_text, cipher_text):
    return plain_text == cipher_text


def verify_use_hashlib(method, plain_text, cipher_text):
    cipher_b = base64.b64decode(cipher_text)
    md4_obj = hashlib.new(method)
    md4_obj.update(plain_text)
    md4_b = md4_obj.digest()
    return md4_b == cipher_b

verify_md4 = partial(verify_use_hashlib, "md4")
verify_ripemd160 = partial(verify_use_hashlib, "ripemd160")


def verify_md5(plain_text, cipher_text):
    cipher_b = base64.b64decode(cipher_text)
    md5_obj = hashlib.md5(plain_text)
    if len(cipher_b) > 16:
        md5_obj.update(cipher_b[16:])
    md5_b = md5_obj.digest()
    return md5_b == cipher_b[:16]


def verify_sha1(plain_text, cipher_text):
    sha1_obj = hashlib.sha1(plain_text)
    cipher_b = base64.b64decode(cipher_text)
    if len(cipher_b) > 20:
        sha1_obj.update(cipher_b[20:])
    return sha1_obj.digest() == cipher_b[:20]


def verify_crypt(plain_text, cipher_text):
    md5_h = crypt(plain_text, cipher_text)
    return md5_h == cipher_text

verify_ssha = verify_sha1
verify_smd5 = verify_md5

v_d = dict(md4=verify_md4, md5=verify_md5, smd5=verify_smd5, sha=verify_sha1, ssha=verify_ssha, crypt=verify_crypt,
           plain=verify_plain, rmd160=verify_ripemd160)
v_d[""] = verify_plain
SUPPORT_METHOD = map(lambda x: x.upper(), v_d.keys())


def verify(method, plain_text, cipher_text):
    if method not in SUPPORT_METHOD:
        return False
    low_method = method.lower()
    return v_d[low_method](plain_text, cipher_text)
    

__all__ = [SUPPORT_METHOD, verify]
