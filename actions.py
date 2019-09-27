# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:39:26 2019

@author: GELab
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
    [300,  50,   100, -180, 0, 0],
    [350,  0,   100, -180, 0, 0],

]


arm.set_position(x=300, y=0, z=100, roll=-180, pitch=0, yaw=0, speed=100, is_radian=False, wait=True)
print(arm.get_position(), arm.get_position(is_radian=False))


ret = arm.move_circle(pose1=poses[0], pose2=poses[1], percent=1000, speed=100, mvacc=100, wait=True,is_radian=False)
print('move_circle, ret: {}'.format(ret))


arm.reset(wait=True)
arm.disconnect()

