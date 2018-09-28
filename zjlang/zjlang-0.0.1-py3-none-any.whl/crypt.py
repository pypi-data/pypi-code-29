"""
ZJLANG Cryptographic utils

author: tim.tang
date: 2018-09-05
"""

import hashlib
import base64
import hmac as _hmac


def hash(text, alg='sha1'):
  """
  Hash text with algs(SHA1, SHA256, SHA512, MD5).
  """
  if alg == 'sha1':
    text = hashlib.sha1(text.encode()).hexdigest()
  elif alg == 'md5':
    text = hashlib.md5(text.encode()).hexdigest()
  elif alg == 'sha256':
    text = hashlib.sha256(text.encode()).hexdigest()
  elif alg == 'sha512':
    text = hashlib.sha512(text.encode()).hexdigest()
  else:
    raise TypeError('invalid hash algorithms: (sha1,sha256,sha512,md5')

  return text


def b64_encode(text):
  """
  Encode text with base64.
  """
  if not text:
    return None

  bytes = base64.b64encode(text.encode())
  return bytes.decode()


def b64_decode(text):
  """
  Decode base64 encoded string.
  """
  bytes = base64.b64decode(text)
  return bytes.decode()


def hmac(key, text):
  """
  Keyed-Hashing for Message

  base64(sha1(...))
  """
  h = _hmac.new(key.encode(), msg=text.encode(), digestmod=hashlib.sha1)
  return base64.b64encode(h.digest()).decode()
