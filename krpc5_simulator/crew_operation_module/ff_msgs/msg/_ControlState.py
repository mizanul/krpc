# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/ControlState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy
import geometry_msgs.msg

class ControlState(genpy.Message):
  _md5sum = "dd5e748762051ecb9ebb52fd483eda70"
  _type = "ff_msgs/ControlState"
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
# Full state vector containing Time, Pose, Vel, and Accel
# 
# when {time}
# flight_mode {string} - disctates, gains, tolerances, etc.
# pose {Point position, Quaternion orientation}
# twist {Vector3 linear, Vector3 angular}
# accel {Vector3 linear, Vector3 angular}

time when
geometry_msgs/Pose pose
geometry_msgs/Twist twist
geometry_msgs/Twist accel

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['when','pose','twist','accel']
  _slot_types = ['time','geometry_msgs/Pose','geometry_msgs/Twist','geometry_msgs/Twist']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       when,pose,twist,accel

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ControlState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.when is None:
        self.when = genpy.Time()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.twist is None:
        self.twist = geometry_msgs.msg.Twist()
      if self.accel is None:
        self.accel = geometry_msgs.msg.Twist()
    else:
      self.when = genpy.Time()
      self.pose = geometry_msgs.msg.Pose()
      self.twist = geometry_msgs.msg.Twist()
      self.accel = geometry_msgs.msg.Twist()

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
      buff.write(_get_struct_2I19d().pack(_x.when.secs, _x.when.nsecs, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel.linear.x, _x.accel.linear.y, _x.accel.linear.z, _x.accel.angular.x, _x.accel.angular.y, _x.accel.angular.z))
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
      if self.when is None:
        self.when = genpy.Time()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.twist is None:
        self.twist = geometry_msgs.msg.Twist()
      if self.accel is None:
        self.accel = geometry_msgs.msg.Twist()
      end = 0
      _x = self
      start = end
      end += 160
      (_x.when.secs, _x.when.nsecs, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel.linear.x, _x.accel.linear.y, _x.accel.linear.z, _x.accel.angular.x, _x.accel.angular.y, _x.accel.angular.z,) = _get_struct_2I19d().unpack(str[start:end])
      self.when.canon()
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
      buff.write(_get_struct_2I19d().pack(_x.when.secs, _x.when.nsecs, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel.linear.x, _x.accel.linear.y, _x.accel.linear.z, _x.accel.angular.x, _x.accel.angular.y, _x.accel.angular.z))
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
      if self.when is None:
        self.when = genpy.Time()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.twist is None:
        self.twist = geometry_msgs.msg.Twist()
      if self.accel is None:
        self.accel = geometry_msgs.msg.Twist()
      end = 0
      _x = self
      start = end
      end += 160
      (_x.when.secs, _x.when.nsecs, _x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.twist.linear.x, _x.twist.linear.y, _x.twist.linear.z, _x.twist.angular.x, _x.twist.angular.y, _x.twist.angular.z, _x.accel.linear.x, _x.accel.linear.y, _x.accel.linear.z, _x.accel.angular.x, _x.accel.angular.y, _x.accel.angular.z,) = _get_struct_2I19d().unpack(str[start:end])
      self.when.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I19d = None
def _get_struct_2I19d():
    global _struct_2I19d
    if _struct_2I19d is None:
        _struct_2I19d = struct.Struct("<2I19d")
    return _struct_2I19d
