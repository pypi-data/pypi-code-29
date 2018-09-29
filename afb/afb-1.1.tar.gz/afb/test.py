# Copyright 2018 Siu-Kei Muk (David). All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from threading import RLock

import inspect
import six

from afb.utils import errors


class Manufacturer(object):
  def __init__(self, cls):
    self._cls = cls  # TODO: Check type(cls)
    self._factories = {}  # TODO: Support built-in functions
    self._lock = RLock()
    self._broker = None
    self._default = None  # Key of default factory

  @property
  def cls(self):
    return self._cls

  @cls.setter
  def cls(self, value):
    raise AttributeError("Output object type of manufacturer is immutable.")

  @property
  def default(self):
    return self._default

  @default.setter
  def default(self, method):
    with self._lock:
      errors.validate_is_string(method, 'method')
      if method not in self._factories:
        raise ValueError("Method with key `{}` not found.".format(method))
      self._default = method

  def set_broker(self, broker):
    """This is intended to be called by the broker in registration."""
    self._broker = broker

  def register(self, method, factory, sig, params=None):
    # Check types
    errors.validate_is_string(method, 'method')
    errors.validate_is_callable(factory, 'factory')

    if not isinstance(sig, dict):
      raise TypeError("")