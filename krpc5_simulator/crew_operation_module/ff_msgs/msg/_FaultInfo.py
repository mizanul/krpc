# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/FaultInfo.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FaultInfo(genpy.Message):
  _md5sum = "1f6014a9106a0f40b77f475f6f9592fa"
  _type = "ff_msgs/FaultInfo"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# Copyright (c) 2017, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
# 
# All rights reserved.
# 
# The Astrobee platform is licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Fault info message is used in the fault config message to contain all the 
# information GDS needs to know about a fault

uint16 subsystem    # index into subsystem names array found in fault config msg

uint16 node         # index into node names array found in fault config msg

uint32 id           # id corresponding to the fault

bool warning        # whether the fault is a warning or not

string description  # A short description of why the fault occurred
"""
  __slots__ = ['subsystem','node','id','warning','description']
  _slot_types = ['uint16','uint16','uint32','bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       subsystem,node,id,warning,description

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FaultInfo, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.subsystem is None:
        self.subsystem = 0
      if self.node is None:
        self.node = 0
      if self.id is None:
        self.id = 0
      if self.warning is None:
        self.warning = False
      if self.description is None:
        self.description = ''
    else:
      self.subsystem = 0
      self.node = 0
      self.id = 0
      self.warning = False
      self.description = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2HIB().pack(_x.subsystem, _x.node, _x.id, _x.warning))
      _x = self.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.subsystem, _x.node, _x.id, _x.warning,) = _get_struct_2HIB().unpack(str[start:end])
      self.warning = bool(self.warning)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.description = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.description = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2HIB().pack(_x.subsystem, _x.node, _x.id, _x.warning))
      _x = self.description
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 9
      (_x.subsystem, _x.node, _x.id, _x.warning,) = _get_struct_2HIB().unpack(str[start:end])
      self.warning = bool(self.warning)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.description = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.description = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2HIB = None
def _get_struct_2HIB():
    global _struct_2HIB
    if _struct_2HIB is None:
        _struct_2HIB = struct.Struct("<2HIB")
    return _struct_2HIB
