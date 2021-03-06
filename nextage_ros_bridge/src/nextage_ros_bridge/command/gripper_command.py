#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2013, Tokyo Opensource Robotics Kyokai Association
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Tokyo Opensource Robotics Kyokai Association. nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Author: Isaac Isao Saito

import rospy

from abs_hand_command import AbsractHandCommand


class GripperCommand(AbsractHandCommand):
    '''
    Following Command design pattern, this class represents an abstract
    command for hand classes of NEXTAGE OPEN.

    NOTE: 1/31/2014 TODO: Only right hand is implemented for now.
    '''
    # TODO: Unittest is needed!!

    GRIPPER_CLOSE = 'close'
    GRIPPER_OPEN = 'open'
    GRIPPER_DANGER = 'danger'

    def __init__(self, hands, hand):
        super(GripperCommand, self).__init__(hands, hand)

    def _assign_dio_names(self):
        '''
        @see abs_hand_command.AbsractHandCommand._assign_dio_names
        '''
        self._DIO_VALVE_L_1 = self._DIO_25
        self._DIO_VALVE_L_2 = self._DIO_26

    def execute(self, operation):
        '''
        @see abs_hand_command.AbsractHandCommand.execute
        '''
        dout = []
        #TODO: Implement right arm too!
        mask = [self._DIO_VALVE_L_1, self._DIO_VALVE_L_2]
        if self.GRIPPER_CLOSE == operation:
            if self._hands.HAND_L == self._hand:
                dout = [self._DIO_VALVE_L_1]
        elif self.GRIPPER_OPEN == operation:
            if self._hands.HAND_L == self._hand:
                dout = [self._DIO_VALVE_L_2]
        self._hands._dio_writer(dout, mask)
