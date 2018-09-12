# Copyright (c) 2016-2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Autogenerated python message buffer code.
Source: clad/types/debugConsoleTypes.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/types/debugConsoleTypes.clad
"""

from __future__ import absolute_import
from __future__ import print_function

def _modify_path():
  import inspect, os, sys
  search_paths = [
    '../..',
    '../../../../tools/message-buffers/support/python',
  ]
  currentpath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))
  for search_path in search_paths:
    search_path = os.path.normpath(os.path.abspath(os.path.realpath(os.path.join(currentpath, search_path))))
    if search_path not in sys.path:
      sys.path.insert(0, search_path)
_modify_path()

import msgbuffers

Anki = msgbuffers.Namespace()
Anki.Cozmo = msgbuffers.Namespace()

class ConsoleVarUnion(object):
  "Generated message-passing union."

  __slots__ = ('_tag', '_data')

  class Tag(object):
    "The type indicator for this union."
    varDouble   = 0 # float_64
    varUint     = 1 # uint_64
    varInt      = 2 # int_64
    varBool     = 3 # uint_8
    varFunction = 4 # string[uint_8]

  @property
  def tag(self):
    "The current tag for this union."
    return self._tag

  @property
  def tag_name(self):
    "The name of the current tag for this union."
    if self._tag in self._tags_by_value:
      return self._tags_by_value[self._tag]
    else:
      return None

  @property
  def data(self):
    "The data held by this union. None if no data is set."
    return self._data

  @property
  def varDouble(self):
    "float_64 varDouble union property."
    msgbuffers.safety_check_tag('varDouble', self._tag, self.Tag.varDouble, self._tags_by_value)
    return self._data

  @varDouble.setter
  def varDouble(self, value):
    self._data = msgbuffers.validate_float(
      'ConsoleVarUnion.varDouble', value, 'd')
    self._tag = self.Tag.varDouble

  @property
  def varUint(self):
    "uint_64 varUint union property."
    msgbuffers.safety_check_tag('varUint', self._tag, self.Tag.varUint, self._tags_by_value)
    return self._data

  @varUint.setter
  def varUint(self, value):
    self._data = msgbuffers.validate_integer(
      'ConsoleVarUnion.varUint', value, 0, 18446744073709551615)
    self._tag = self.Tag.varUint

  @property
  def varInt(self):
    "int_64 varInt union property."
    msgbuffers.safety_check_tag('varInt', self._tag, self.Tag.varInt, self._tags_by_value)
    return self._data

  @varInt.setter
  def varInt(self, value):
    self._data = msgbuffers.validate_integer(
      'ConsoleVarUnion.varInt', value, -9223372036854775808, 9223372036854775807)
    self._tag = self.Tag.varInt

  @property
  def varBool(self):
    "uint_8 varBool union property."
    msgbuffers.safety_check_tag('varBool', self._tag, self.Tag.varBool, self._tags_by_value)
    return self._data

  @varBool.setter
  def varBool(self, value):
    self._data = msgbuffers.validate_integer(
      'ConsoleVarUnion.varBool', value, 0, 255)
    self._tag = self.Tag.varBool

  @property
  def varFunction(self):
    "string[uint_8] varFunction union property."
    msgbuffers.safety_check_tag('varFunction', self._tag, self.Tag.varFunction, self._tags_by_value)
    return self._data

  @varFunction.setter
  def varFunction(self, value):
    self._data = msgbuffers.validate_string(
      'ConsoleVarUnion.varFunction', value, 255)
    self._tag = self.Tag.varFunction

  def __init__(self, **kwargs):
    if not kwargs:
      self._tag = None
      self._data = None

    elif len(kwargs) == 1:
      key, value = next(iter(kwargs.items()))
      if key not in self._tags_by_name:
        raise TypeError("'{argument}' is an invalid keyword argument for this method.".format(argument=key))
      # calls the correct property
      setattr(self, key, value)

    else:
      raise TypeError('This method only accepts up to one keyword argument.')

  @classmethod
  def unpack(cls, buffer):
    "Reads a new ConsoleVarUnion from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('ConsoleVarUnion.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new ConsoleVarUnion from the given BinaryReader."
    tag = reader.read('B')
    if tag in cls._tags_by_value:
      value = cls()
      setattr(value, cls._tags_by_value[tag], cls._tag_unpack_methods[tag](reader))
      return value
    else:
      raise ValueError('ConsoleVarUnion attempted to unpack unknown tag {tag}.'.format(tag=tag))

  def pack(self):
    "Writes the current ConsoleVarUnion, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current SampleUnion to the given BinaryWriter."
    if self._tag in self._tags_by_value:
      writer.write(self._tag, 'B')
      self._tag_pack_methods[self._tag](writer, self._data)
    else:
      raise ValueError('Cannot pack an empty ConsoleVarUnion.')

  def clear(self):
    self._tag = None
    self._data = None

  @classmethod
  def typeByTag(cls, tag):
    return cls._type_by_tag_value[tag]()

  def __eq__(self, other):
    if type(self) is type(other):
      return self._tag == other._tag and self._data == other._data
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    if 0 <= self._tag < 5:
      return self._tag_size_methods[self._tag](self._data)
    else:
      return 1

  def __str__(self):
    if 0 <= self._tag < 5:
      return '{type}({name}={value})'.format(
        type=type(self).__name__,
        name=self.tag_name,
        value=self._data)
    else:
      return '{type}()'.format(
        type=type(self).__name__)

  def __repr__(self):
    if 0 <= self._tag < 5:
      return '{type}({name}={value})'.format(
        type=type(self).__name__,
        name=self.tag_name,
        value=repr(self._data))
    else:
      return '{type}()'.format(
        type=type(self).__name__)

  _tags_by_name = dict(
    varDouble=0,
    varUint=1,
    varInt=2,
    varBool=3,
    varFunction=4,
  )

  _tags_by_value = dict()
  _tags_by_value[0] = 'varDouble'
  _tags_by_value[1] = 'varUint'
  _tags_by_value[2] = 'varInt'
  _tags_by_value[3] = 'varBool'
  _tags_by_value[4] = 'varFunction'
  

  _tag_unpack_methods = dict()
  _tag_unpack_methods[0] = lambda reader: reader.read('d')
  _tag_unpack_methods[1] = lambda reader: reader.read('Q')
  _tag_unpack_methods[2] = lambda reader: reader.read('q')
  _tag_unpack_methods[3] = lambda reader: reader.read('B')
  _tag_unpack_methods[4] = lambda reader: reader.read_string('B')
  

  _tag_pack_methods = dict()
  _tag_pack_methods[0] = lambda writer, value: writer.write(value, 'd')
  _tag_pack_methods[1] = lambda writer, value: writer.write(value, 'Q')
  _tag_pack_methods[2] = lambda writer, value: writer.write(value, 'q')
  _tag_pack_methods[3] = lambda writer, value: writer.write(value, 'B')
  _tag_pack_methods[4] = lambda writer, value: writer.write_string(value, 'B')
  

  _tag_size_methods = dict()
  _tag_size_methods[0] = lambda value: msgbuffers.size(value, 'd')
  _tag_size_methods[1] = lambda value: msgbuffers.size(value, 'Q')
  _tag_size_methods[2] = lambda value: msgbuffers.size(value, 'q')
  _tag_size_methods[3] = lambda value: msgbuffers.size(value, 'B')
  _tag_size_methods[4] = lambda value: msgbuffers.size_string(value, 'B')
  

  _type_by_tag_value = dict()
  _type_by_tag_value[0] = lambda : float
  _type_by_tag_value[1] = lambda : int
  _type_by_tag_value[2] = lambda : int
  _type_by_tag_value[3] = lambda : int
  _type_by_tag_value[4] = lambda : bytes
  

Anki.Cozmo.ConsoleVarUnion = ConsoleVarUnion
del ConsoleVarUnion


