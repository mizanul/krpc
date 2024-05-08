# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ff_msgs/AgentStateStamped.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import ff_msgs.msg
import std_msgs.msg

class AgentStateStamped(genpy.Message):
  _md5sum = "156487b23e377e3a1dc7ef079f0e327d"
  _type = "ff_msgs/AgentStateStamped"
  _has_header = True  # flag to mark the presence of a Header object
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
# State of the Astrobee, based off of rapid::ext::astrobee::AgentState

# Header with timestamp
std_msgs/Header header

# Operating state of the Astrobee
ff_msgs/OpState operating_state

# Plan execution state. State is idle when there is no plan to be executed. Once
# a plan is uploaded, the state change to paused. Upon a run plan command, the
# state will change to executing. If a stop or pause plan command is received or
# a fault occurs, the state will be set to pause. Once the plan is completed,
# the state will go back to idle
ff_msgs/ExecState plan_execution_state

# Guest science state. If a primary guest science apk is started, the state
# will go from idle to executing. Once the primarty apk is finished, the state
# will go back to idle
ff_msgs/ExecState guest_science_state

# Mobility state of the Astrobee
ff_msgs/MobilityState mobility_state

# Proximity to the dock when docking and undocking. Proximity to a handrail when
# perching or unperching. 0 the rest of the time.
float32 proximity

# Name of profile configuration, i.e. Nominal, IgnoreObstacles, Faceforward,
# Quiet, etc. Profiles specify stuff like target velocity and acceleration,
# collision distance, etc.
string profile_name

#Defines GN&C gains, hard limits, tolerances, etc.
string flight_mode

# Maximum linear velocity to target while translating
float32 target_linear_velocity
# Maximum linear acceleration to target while translating
float32 target_linear_accel
# Maximum angular velocity to target while rotating
float32 target_angular_velocity
# Maximum angular acceleration to target while rotating
float32 target_angular_accel
# Minimum distance margin to maintain away from obstacles
float32 collision_distance

# Specifies whether the Astrobee is allowed to fly blind i.e. not faceforward
bool holonomic_enabled

# Specifies whether the Astrobee is checking for obstacles
bool check_obstacles

# Specifies whether the Astrobee is checking the keepin and keepout zones
bool check_zones

# Specifies whether the Astrobee is allowed to auto return. Please note,
# Astrobee will only use this flags when deciding if it should auto return. If
# the astrobee gets a command to auto return from the operator or guest science,
# it will auto return without checking this flag
bool auto_return_enabled

# Specifies whether the choreographer should execute a segment immediately or
# based on the time stamp in the segement
bool immediate_enabled

# Specifies the current planner being used
string planner

# Specifies whether re-planning is allowed
bool replanning_enabled

# Specifies the current world being used
string world

# Number of seconds since Unix Epoch
uint32 boot_time

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: ff_msgs/OpState
# Copyright (c) 2017, United States Government, as represented by the
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
# Operating States, based off of the enumeration constants
# in rapid::ext::astrobee::AgentState.
#
# *MUST* be kept in sync with the DDS IDL file in astrobee_common

uint8 READY            = 0  # Freeflyer is ready to accept commands
uint8 PLAN_EXECUTION   = 1  # Freeflyer is executing a plan
uint8 TELEOPERATION    = 2  # Freeflyer is executing a teleop command
uint8 AUTO_RETURN      = 3  # Freeflyer is autonomously returning to the dock
# The freeflyer is either executing a fault response or there is a fault
# occurring in the system that prevents the freeflyer from moving
uint8 FAULT            = 4

# Operating state
uint8 state

================================================================================
MSG: ff_msgs/ExecState
# Copyright (c) 2017, United States Government, as represented by the
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
# Execution States, based off of the enumeration constants in
# rapid::ext::astrobee::AgentState
#
# *MUST* be kept in sync with the DDS IDL file in astrobee_common

uint8 IDLE      = 0   # Process is idle
uint8 EXECUTING = 1   # Process is executing
uint8 PAUSED    = 2   # Process is paused
uint8 ERROR     = 3   # Process encountered an error

# Execution state
uint8 state

================================================================================
MSG: ff_msgs/MobilityState
# Copyright (c) 2017, United States Government, as represented by the
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
# Mobility states, based off the enumeration constants in
# rapid::ext::astrobee::AgentState
#
# *MUST* be kept in sync with the DDS IDL file in astrobee_common

uint8 DRIFTING        = 0   # Astrobee's propulsion is off
uint8 STOPPING        = 1   # Astrobee is either stopping or stopped
uint8 FLYING          = 2   # Astrobee is flying
uint8 DOCKING         = 3   # Astrobee is either docking or undocking
uint8 PERCHING        = 4   # Astrobee is either perching or unperching

# Mobility state
uint8 state

# Specifies the progress of the action. For docking, this value can be N to -N
# where N through 1 specifies the progress of a docking action, 0 is docked, and
# -1 through -N specifies the process of an undocking action. For stopping, this
# value is either 1 or 0 where 1 means the robot is coming to a stop and 0 means
# the robot is stopped. For perching, this value can be N to -N where N through
# 1 specifies the progress of a perching action, 0 is perched, and -1 through
# -N specifies the process of an unperching action.
int32 sub_state
"""
  __slots__ = ['header','operating_state','plan_execution_state','guest_science_state','mobility_state','proximity','profile_name','flight_mode','target_linear_velocity','target_linear_accel','target_angular_velocity','target_angular_accel','collision_distance','holonomic_enabled','check_obstacles','check_zones','auto_return_enabled','immediate_enabled','planner','replanning_enabled','world','boot_time']
  _slot_types = ['std_msgs/Header','ff_msgs/OpState','ff_msgs/ExecState','ff_msgs/ExecState','ff_msgs/MobilityState','float32','string','string','float32','float32','float32','float32','float32','bool','bool','bool','bool','bool','string','bool','string','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,operating_state,plan_execution_state,guest_science_state,mobility_state,proximity,profile_name,flight_mode,target_linear_velocity,target_linear_accel,target_angular_velocity,target_angular_accel,collision_distance,holonomic_enabled,check_obstacles,check_zones,auto_return_enabled,immediate_enabled,planner,replanning_enabled,world,boot_time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AgentStateStamped, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.operating_state is None:
        self.operating_state = ff_msgs.msg.OpState()
      if self.plan_execution_state is None:
        self.plan_execution_state = ff_msgs.msg.ExecState()
      if self.guest_science_state is None:
        self.guest_science_state = ff_msgs.msg.ExecState()
      if self.mobility_state is None:
        self.mobility_state = ff_msgs.msg.MobilityState()
      if self.proximity is None:
        self.proximity = 0.
      if self.profile_name is None:
        self.profile_name = ''
      if self.flight_mode is None:
        self.flight_mode = ''
      if self.target_linear_velocity is None:
        self.target_linear_velocity = 0.
      if self.target_linear_accel is None:
        self.target_linear_accel = 0.
      if self.target_angular_velocity is None:
        self.target_angular_velocity = 0.
      if self.target_angular_accel is None:
        self.target_angular_accel = 0.
      if self.collision_distance is None:
        self.collision_distance = 0.
      if self.holonomic_enabled is None:
        self.holonomic_enabled = False
      if self.check_obstacles is None:
        self.check_obstacles = False
      if self.check_zones is None:
        self.check_zones = False
      if self.auto_return_enabled is None:
        self.auto_return_enabled = False
      if self.immediate_enabled is None:
        self.immediate_enabled = False
      if self.planner is None:
        self.planner = ''
      if self.replanning_enabled is None:
        self.replanning_enabled = False
      if self.world is None:
        self.world = ''
      if self.boot_time is None:
        self.boot_time = 0
    else:
      self.header = std_msgs.msg.Header()
      self.operating_state = ff_msgs.msg.OpState()
      self.plan_execution_state = ff_msgs.msg.ExecState()
      self.guest_science_state = ff_msgs.msg.ExecState()
      self.mobility_state = ff_msgs.msg.MobilityState()
      self.proximity = 0.
      self.profile_name = ''
      self.flight_mode = ''
      self.target_linear_velocity = 0.
      self.target_linear_accel = 0.
      self.target_angular_velocity = 0.
      self.target_angular_accel = 0.
      self.collision_distance = 0.
      self.holonomic_enabled = False
      self.check_obstacles = False
      self.check_zones = False
      self.auto_return_enabled = False
      self.immediate_enabled = False
      self.planner = ''
      self.replanning_enabled = False
      self.world = ''
      self.boot_time = 0

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4Bif().pack(_x.operating_state.state, _x.plan_execution_state.state, _x.guest_science_state.state, _x.mobility_state.state, _x.mobility_state.sub_state, _x.proximity))
      _x = self.profile_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.flight_mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5f5B().pack(_x.target_linear_velocity, _x.target_linear_accel, _x.target_angular_velocity, _x.target_angular_accel, _x.collision_distance, _x.holonomic_enabled, _x.check_obstacles, _x.check_zones, _x.auto_return_enabled, _x.immediate_enabled))
      _x = self.planner
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.replanning_enabled
      buff.write(_get_struct_B().pack(_x))
      _x = self.world
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.boot_time
      buff.write(_get_struct_I().pack(_x))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.operating_state is None:
        self.operating_state = ff_msgs.msg.OpState()
      if self.plan_execution_state is None:
        self.plan_execution_state = ff_msgs.msg.ExecState()
      if self.guest_science_state is None:
        self.guest_science_state = ff_msgs.msg.ExecState()
      if self.mobility_state is None:
        self.mobility_state = ff_msgs.msg.MobilityState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.operating_state.state, _x.plan_execution_state.state, _x.guest_science_state.state, _x.mobility_state.state, _x.mobility_state.sub_state, _x.proximity,) = _get_struct_4Bif().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.profile_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.profile_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.flight_mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.flight_mode = str[start:end]
      _x = self
      start = end
      end += 25
      (_x.target_linear_velocity, _x.target_linear_accel, _x.target_angular_velocity, _x.target_angular_accel, _x.collision_distance, _x.holonomic_enabled, _x.check_obstacles, _x.check_zones, _x.auto_return_enabled, _x.immediate_enabled,) = _get_struct_5f5B().unpack(str[start:end])
      self.holonomic_enabled = bool(self.holonomic_enabled)
      self.check_obstacles = bool(self.check_obstacles)
      self.check_zones = bool(self.check_zones)
      self.auto_return_enabled = bool(self.auto_return_enabled)
      self.immediate_enabled = bool(self.immediate_enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.planner = str[start:end]
      start = end
      end += 1
      (self.replanning_enabled,) = _get_struct_B().unpack(str[start:end])
      self.replanning_enabled = bool(self.replanning_enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.world = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.world = str[start:end]
      start = end
      end += 4
      (self.boot_time,) = _get_struct_I().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_4Bif().pack(_x.operating_state.state, _x.plan_execution_state.state, _x.guest_science_state.state, _x.mobility_state.state, _x.mobility_state.sub_state, _x.proximity))
      _x = self.profile_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.flight_mode
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_5f5B().pack(_x.target_linear_velocity, _x.target_linear_accel, _x.target_angular_velocity, _x.target_angular_accel, _x.collision_distance, _x.holonomic_enabled, _x.check_obstacles, _x.check_zones, _x.auto_return_enabled, _x.immediate_enabled))
      _x = self.planner
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.replanning_enabled
      buff.write(_get_struct_B().pack(_x))
      _x = self.world
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.boot_time
      buff.write(_get_struct_I().pack(_x))
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
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.operating_state is None:
        self.operating_state = ff_msgs.msg.OpState()
      if self.plan_execution_state is None:
        self.plan_execution_state = ff_msgs.msg.ExecState()
      if self.guest_science_state is None:
        self.guest_science_state = ff_msgs.msg.ExecState()
      if self.mobility_state is None:
        self.mobility_state = ff_msgs.msg.MobilityState()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.operating_state.state, _x.plan_execution_state.state, _x.guest_science_state.state, _x.mobility_state.state, _x.mobility_state.sub_state, _x.proximity,) = _get_struct_4Bif().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.profile_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.profile_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.flight_mode = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.flight_mode = str[start:end]
      _x = self
      start = end
      end += 25
      (_x.target_linear_velocity, _x.target_linear_accel, _x.target_angular_velocity, _x.target_angular_accel, _x.collision_distance, _x.holonomic_enabled, _x.check_obstacles, _x.check_zones, _x.auto_return_enabled, _x.immediate_enabled,) = _get_struct_5f5B().unpack(str[start:end])
      self.holonomic_enabled = bool(self.holonomic_enabled)
      self.check_obstacles = bool(self.check_obstacles)
      self.check_zones = bool(self.check_zones)
      self.auto_return_enabled = bool(self.auto_return_enabled)
      self.immediate_enabled = bool(self.immediate_enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.planner = str[start:end]
      start = end
      end += 1
      (self.replanning_enabled,) = _get_struct_B().unpack(str[start:end])
      self.replanning_enabled = bool(self.replanning_enabled)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.world = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.world = str[start:end]
      start = end
      end += 4
      (self.boot_time,) = _get_struct_I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_4Bif = None
def _get_struct_4Bif():
    global _struct_4Bif
    if _struct_4Bif is None:
        _struct_4Bif = struct.Struct("<4Bif")
    return _struct_4Bif
_struct_5f5B = None
def _get_struct_5f5B():
    global _struct_5f5B
    if _struct_5f5B is None:
        _struct_5f5B = struct.Struct("<5f5B")
    return _struct_5f5B
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
