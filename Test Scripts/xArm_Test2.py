#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2019, UFACTORY, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

"""
Description: Move Circle
"""

import os
import sys
import time

#sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from xarm.wrapper import XArmAPI


#######################################################
"""
Just for test example
"""
if len(sys.argv) >= 2:
    ip = sys.argv[1]
else:
    try:
        from configparser import ConfigParser
        parser = ConfigParser()
        parser.read('./robot1.conf')
        ip = parser.get('xArm', 'ip')
    except:
        ip = input('Please input the xArm ip address:')
        if not ip:
            print('input error, exit')
            sys.exit(1)
########################################################


arm = XArmAPI(ip, is_radian=True)
arm.motion_enable(enable=True)
arm.set_mode(0)
arm.set_state(state=0)

arm.reset(wait=True)

poses = [
    [300,  0,   100, -180, 0, 0],
    [300,  100, 100, -3.1416, 0, 0],
    [400,  100, 100, -3.1416, 0, 0],
    [400, -100, 100, -3.1416, 0, 0],
    [300,  0,   300, -3.1416, 0, 0]
]

ret = arm.set_position(*poses[0], speed=50, wait=True,is_radian= False)

print('set_position, ret: {}'.format(ret))


arm.set_position(x=300, y=0, z=100, roll=-180, pitch=0, yaw=0, speed=100, is_radian=False, wait=True)
print(arm.get_position(), arm.get_position(is_radian=False))



ret = arm.move_circle(pose1=poses[1], pose2=poses[2], percent=70, speed=200, mvacc=200, wait=True)
print('move_circle, ret: {}'.format(ret))

ret = arm.move_circle(pose1=poses[3], pose2=poses[4], percent=200, speed=200, mvacc=1000, wait=True)
print('move_circle, ret: {}'.format(ret))

arm.reset(wait=True)
arm.disconnect()
8