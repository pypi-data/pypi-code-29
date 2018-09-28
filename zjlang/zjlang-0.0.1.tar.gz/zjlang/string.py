"""
ZJLANG string utils function

rename to stringx preventing conflict with stlib string module, which doctest will import implicitly

author: tim.tang
date: 2018-09-04
"""
import random

_lower_case_ = [chr(x) for x in range(97, 123)]
_upper_case_ = [chr(x) for x in range(65, 91)]
_digits_ = [chr(x) for x in range(48, 58)]
_all_letters_ = _digits_ + _upper_case_ + _lower_case_


def uuid(safe=True):
  """
  Generate UUID string 

  return lowcase string without '-':
  >>>34df3ddfdfad33333
  """
  import uuid
  if safe:
    return uuid.uuid4().hex
  return uuid.uuid1().hex


def random_str(num):
  s = [_all_letters_[random.randint(0, 61)] for i in range(num)]
  return ''.join(s)


def random_int(num):
  s = [_digits_[random.randint(0, 9)] for i in range(num)]
  return ''.join(s)
