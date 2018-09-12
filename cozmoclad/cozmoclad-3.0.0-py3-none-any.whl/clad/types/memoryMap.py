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
Source: clad/types/memoryMap.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/types/memoryMap.clad
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
Anki.Cozmo.ExternalInterface = msgbuffers.Namespace()

class MemoryMapInfo(object):
  "Generated message-passing structure."

  __slots__ = (
    '_rootDepth',   # int_32
    '_rootSize_mm', # float_32
    '_rootCenterX', # float_32
    '_rootCenterY', # float_32
    '_rootCenterZ', # float_32
    '_identifier',  # string[uint_8]
  )

  @property
  def rootDepth(self):
    "int_32 rootDepth struct property."
    return self._rootDepth

  @rootDepth.setter
  def rootDepth(self, value):
    self._rootDepth = msgbuffers.validate_integer(
      'MemoryMapInfo.rootDepth', value, -2147483648, 2147483647)

  @property
  def rootSize_mm(self):
    "float_32 rootSize_mm struct property."
    return self._rootSize_mm

  @rootSize_mm.setter
  def rootSize_mm(self, value):
    self._rootSize_mm = msgbuffers.validate_float(
      'MemoryMapInfo.rootSize_mm', value, 'f')

  @property
  def rootCenterX(self):
    "float_32 rootCenterX struct property."
    return self._rootCenterX

  @rootCenterX.setter
  def rootCenterX(self, value):
    self._rootCenterX = msgbuffers.validate_float(
      'MemoryMapInfo.rootCenterX', value, 'f')

  @property
  def rootCenterY(self):
    "float_32 rootCenterY struct property."
    return self._rootCenterY

  @rootCenterY.setter
  def rootCenterY(self, value):
    self._rootCenterY = msgbuffers.validate_float(
      'MemoryMapInfo.rootCenterY', value, 'f')

  @property
  def rootCenterZ(self):
    "float_32 rootCenterZ struct property."
    return self._rootCenterZ

  @rootCenterZ.setter
  def rootCenterZ(self, value):
    self._rootCenterZ = msgbuffers.validate_float(
      'MemoryMapInfo.rootCenterZ', value, 'f')

  @property
  def identifier(self):
    "string[uint_8] identifier struct property."
    return self._identifier

  @identifier.setter
  def identifier(self, value):
    self._identifier = msgbuffers.validate_string(
      'MemoryMapInfo.identifier', value, 255)

  def __init__(self, rootDepth=0, rootSize_mm=0.0, rootCenterX=0.0, rootCenterY=0.0, rootCenterZ=0.0, identifier=''):
    self.rootDepth = rootDepth
    self.rootSize_mm = rootSize_mm
    self.rootCenterX = rootCenterX
    self.rootCenterY = rootCenterY
    self.rootCenterZ = rootCenterZ
    self.identifier = identifier

  @classmethod
  def unpack(cls, buffer):
    "Reads a new MemoryMapInfo from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('MemoryMapInfo.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new MemoryMapInfo from the given BinaryReader."
    _rootDepth = reader.read('i')
    _rootSize_mm = reader.read('f')
    _rootCenterX = reader.read('f')
    _rootCenterY = reader.read('f')
    _rootCenterZ = reader.read('f')
    _identifier = reader.read_string('B')
    return cls(_rootDepth, _rootSize_mm, _rootCenterX, _rootCenterY, _rootCenterZ, _identifier)

  def pack(self):
    "Writes the current MemoryMapInfo, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current MemoryMapInfo to the given BinaryWriter."
    writer.write(self._rootDepth, 'i')
    writer.write(self._rootSize_mm, 'f')
    writer.write(self._rootCenterX, 'f')
    writer.write(self._rootCenterY, 'f')
    writer.write(self._rootCenterZ, 'f')
    writer.write_string(self._identifier, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._rootDepth == other._rootDepth and
        self._rootSize_mm == other._rootSize_mm and
        self._rootCenterX == other._rootCenterX and
        self._rootCenterY == other._rootCenterY and
        self._rootCenterZ == other._rootCenterZ and
        self._identifier == other._identifier)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._rootDepth, 'i') +
      msgbuffers.size(self._rootSize_mm, 'f') +
      msgbuffers.size(self._rootCenterX, 'f') +
      msgbuffers.size(self._rootCenterY, 'f') +
      msgbuffers.size(self._rootCenterZ, 'f') +
      msgbuffers.size_string(self._identifier, 'B'))

  def __str__(self):
    return '{type}(rootDepth={rootDepth}, rootSize_mm={rootSize_mm}, rootCenterX={rootCenterX}, rootCenterY={rootCenterY}, rootCenterZ={rootCenterZ}, identifier={identifier})'.format(
      type=type(self).__name__,
      rootDepth=self._rootDepth,
      rootSize_mm=self._rootSize_mm,
      rootCenterX=self._rootCenterX,
      rootCenterY=self._rootCenterY,
      rootCenterZ=self._rootCenterZ,
      identifier=msgbuffers.shorten_string(self._identifier))

  def __repr__(self):
    return '{type}(rootDepth={rootDepth}, rootSize_mm={rootSize_mm}, rootCenterX={rootCenterX}, rootCenterY={rootCenterY}, rootCenterZ={rootCenterZ}, identifier={identifier})'.format(
      type=type(self).__name__,
      rootDepth=repr(self._rootDepth),
      rootSize_mm=repr(self._rootSize_mm),
      rootCenterX=repr(self._rootCenterX),
      rootCenterY=repr(self._rootCenterY),
      rootCenterZ=repr(self._rootCenterZ),
      identifier=repr(self._identifier))

Anki.Cozmo.ExternalInterface.MemoryMapInfo = MemoryMapInfo
del MemoryMapInfo


class ENodeContentTypeEnum(object):
  "Automatically-generated uint_8 enumeration."
  Unknown         = 0
  ClearOfObstacle = 1
  ClearOfCliff    = 2
  ObstacleCube    = 3
  ObstacleCharger = 4
  ObstacleProx    = 5
  Cliff           = 6
  VisionBorder    = 7

Anki.Cozmo.ExternalInterface.ENodeContentTypeEnum = ENodeContentTypeEnum
del ENodeContentTypeEnum


class ENodeContentTypeDebugVizEnum(object):
  "Automatically-generated uint_8 enumeration."
  Unknown                = 0
  ClearOfObstacle        = 1
  ClearOfCliff           = 2
  ObstacleCube           = 3
  ObstacleCharger        = 4
  ObstacleChargerRemoved = 5
  ObstacleProx           = 6
  ObstacleUnrecognized   = 7
  Cliff                  = 8
  InterestingEdge        = 9
  NotInterestingEdge     = 10

Anki.Cozmo.ExternalInterface.ENodeContentTypeDebugVizEnum = ENodeContentTypeDebugVizEnum
del ENodeContentTypeDebugVizEnum


class MemoryMapQuadInfo(object):
  "Generated message-passing structure."

  __slots__ = (
    '_content', # Anki.Cozmo.ExternalInterface.ENodeContentTypeEnum
    '_depth',   # uint_8
  )

  @property
  def content(self):
    "Anki.Cozmo.ExternalInterface.ENodeContentTypeEnum content struct property."
    return self._content

  @content.setter
  def content(self, value):
    self._content = msgbuffers.validate_integer(
      'MemoryMapQuadInfo.content', value, 0, 255)

  @property
  def depth(self):
    "uint_8 depth struct property."
    return self._depth

  @depth.setter
  def depth(self, value):
    self._depth = msgbuffers.validate_integer(
      'MemoryMapQuadInfo.depth', value, 0, 255)

  def __init__(self, content=Anki.Cozmo.ExternalInterface.ENodeContentTypeEnum.Unknown, depth=0):
    self.content = content
    self.depth = depth

  @classmethod
  def unpack(cls, buffer):
    "Reads a new MemoryMapQuadInfo from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('MemoryMapQuadInfo.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new MemoryMapQuadInfo from the given BinaryReader."
    _content = reader.read('B')
    _depth = reader.read('B')
    return cls(_content, _depth)

  def pack(self):
    "Writes the current MemoryMapQuadInfo, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current MemoryMapQuadInfo to the given BinaryWriter."
    writer.write(self._content, 'B')
    writer.write(self._depth, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._content == other._content and
        self._depth == other._depth)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._content, 'B') +
      msgbuffers.size(self._depth, 'B'))

  def __str__(self):
    return '{type}(content={content}, depth={depth})'.format(
      type=type(self).__name__,
      content=self._content,
      depth=self._depth)

  def __repr__(self):
    return '{type}(content={content}, depth={depth})'.format(
      type=type(self).__name__,
      content=repr(self._content),
      depth=repr(self._depth))

Anki.Cozmo.ExternalInterface.MemoryMapQuadInfo = MemoryMapQuadInfo
del MemoryMapQuadInfo


class MemoryMapQuadInfoDebugViz(object):
  "Generated message-passing structure."

  __slots__ = (
    '_content', # Anki.Cozmo.ExternalInterface.ENodeContentTypeDebugVizEnum
    '_depth',   # uint_8
  )

  @property
  def content(self):
    "Anki.Cozmo.ExternalInterface.ENodeContentTypeDebugVizEnum content struct property."
    return self._content

  @content.setter
  def content(self, value):
    self._content = msgbuffers.validate_integer(
      'MemoryMapQuadInfoDebugViz.content', value, 0, 255)

  @property
  def depth(self):
    "uint_8 depth struct property."
    return self._depth

  @depth.setter
  def depth(self, value):
    self._depth = msgbuffers.validate_integer(
      'MemoryMapQuadInfoDebugViz.depth', value, 0, 255)

  def __init__(self, content=Anki.Cozmo.ExternalInterface.ENodeContentTypeDebugVizEnum.Unknown, depth=0):
    self.content = content
    self.depth = depth

  @classmethod
  def unpack(cls, buffer):
    "Reads a new MemoryMapQuadInfoDebugViz from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('MemoryMapQuadInfoDebugViz.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new MemoryMapQuadInfoDebugViz from the given BinaryReader."
    _content = reader.read('B')
    _depth = reader.read('B')
    return cls(_content, _depth)

  def pack(self):
    "Writes the current MemoryMapQuadInfoDebugViz, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current MemoryMapQuadInfoDebugViz to the given BinaryWriter."
    writer.write(self._content, 'B')
    writer.write(self._depth, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._content == other._content and
        self._depth == other._depth)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._content, 'B') +
      msgbuffers.size(self._depth, 'B'))

  def __str__(self):
    return '{type}(content={content}, depth={depth})'.format(
      type=type(self).__name__,
      content=self._content,
      depth=self._depth)

  def __repr__(self):
    return '{type}(content={content}, depth={depth})'.format(
      type=type(self).__name__,
      content=repr(self._content),
      depth=repr(self._depth))

Anki.Cozmo.ExternalInterface.MemoryMapQuadInfoDebugViz = MemoryMapQuadInfoDebugViz
del MemoryMapQuadInfoDebugViz


