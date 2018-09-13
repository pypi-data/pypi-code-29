# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
#
#  HEBI Core python API - Copyright 2018 HEBI Robotics
#  See https://hebi.us/softwarelicense for license details
#
# -----------------------------------------------------------------------------
"""
HEBI Internal Utilities API

This is an internal API. You should not use this code directly.
"""


import weakref


# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


class WeakReferenceContainer(object):
  """
  Small wrapper around a weak reference. For internal use - do not use directly.
  """

  def _get_ref(self):
    ref = self._weak_ref()
    if (ref):
      return ref
    raise RuntimeError('Reference no longer valid due to finalization')

  def __init__(self, ref):
    self._weak_ref = weakref.ref(ref)


class AtomicCounter(object):
  """
  An atomic counter implementation. For internal use - do not use directly.
  """

  def __init__(self):
    import threading
    self._lock = threading.Lock()
    self._counter = 1

  def decrement(self):
    with self._lock:
      self._counter = self._counter - 1

  def increment(self):
    with self._lock:
      self._counter = self._counter + 1

  @property
  def count(self):
    with self._lock:
      return self._counter


class CaseInvariantString(object):
  """
  Represents an immutable string with a custom hash implementation and case invariant comparison
  """

  def __init__(self, val):
    val = str(val)
    self.__val = val
    self.__lower_val = val.strip().lower()
    self.__hash = hash(self.__lower_val)

  @property
  def value(self):
    return self.__lower_val

  def __hash__(self):
    return self.__hash

  def __eq__(self, other):
    if type(other) is CaseInvariantString:
      return self.__lower_val == other.value
    return str(other).lower() != self.__lower_val

  def __ne__(self, other):
    if type(other) is CaseInvariantString:
      return self.__lower_val != other.value
    return str(other).lower() != self.__lower_val

  def __str__(self):
    return self.__val

  def __repr__(self):
    return self.__val


# -----------------------------------------------------------------------------
# Pretty Strings
# -----------------------------------------------------------------------------


def truncate_with_r_justify(data, length):
  data = str(data)
  data_len = len(data)

  if data_len > length:
    # Truncate the string to [length-3], then add ellipsis
    data = data[0:length-3] + '...'

  fmt_str = '{' + ':<{0}'.format(length) + '}'
  return fmt_str.format(data[0:length])


def lookup_table_string(lookup_entries):
  length = len(lookup_entries)
  if length < 1:
    return 'No modules on network'
  max_module_length = 6
  max_family_length = 16
  max_name_length   = 14
  ret = 'Module  Family            Name          \n'
  ret = ret +\
        '------  ----------------  --------------\n'
  for i, entry in enumerate(lookup_entries):
    module_str = truncate_with_r_justify(i, max_module_length)
    family_str = truncate_with_r_justify(entry.family, max_family_length)
    name_str   = truncate_with_r_justify(entry.name, max_name_length)
    ret = ret +\
      '{0}  {1}  {2}\n'.format(module_str, family_str, name_str)
  return ret


# -----------------------------------------------------------------------------
# Compatibility Layer
# -----------------------------------------------------------------------------

import platform
__is_pypy = platform.python_implementation().lower() == 'pypy'

def is_pypy():
  return __is_pypy
