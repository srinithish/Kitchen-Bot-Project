import os
import sys
import time

from cookingActions import cookingActions
from cookingActions2 import cookingActions2
from xarm.wrapper import XArmAPI
from configparser import ConfigParser

parser = ConfigParser()
parser.read('./robot2.conf')

ip = parser.get('xArm', 'ip')

def handle_err_warn_changed(item):
    print('ErrorCode: {}, WarnCode: {}'.format(item['error_code'], item['warn_code']))
    # TODO：Do different processing according to the error code

arm = XArmAPI(ip, do_not_open=True, is_radian=False)
arm.register_error_warn_changed_callback(hangle_err_warn_changed)
arm.connect()


## set limited working space
#arm.set_reduced_max_tcp_speed(200)
# x_max, x_min, y_max, y_min, z_max, z_min = 500, 100, 600, 100, 400, 100
# arm.set_reduced_tcp_boundary([x_max, x_min, y_max, y_min, z_max, z_min])
# arm.set_reduced_mode(True)

# enable motion
arm.motion_enable(enable=True)
# set mode: position control mode
arm.set_mode(0)
# set state: sport state
arm.set_state(state=0)



## actions here
myCkAct = cookingActions(arm)
myCkAct2= cookingActions2(arm)

arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 50, wait = True)

myCkAct.stir([500,0,200,-180,0,0],speed = 100,radius = 50,numTimes=5,wait = True)
arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 50, wait = True)

myCkAct2.stirWithOrient([500,0,200,-180,0,0],orient = 20,speed = 200,radius = 50,numTimes=5,wait = True)
arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 50, wait = True)

myCkAct2.stirEight([500,0,200,-180,0,0],speed = 200,radius = 100,numTimes=5,wait = True)
arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 50, wait = True)

myCkAct2.stirAnyPlane([500,0,400,-180,0,0],plane = 1,speed = 200,radius = 50,numTimes=5,wait = True)
arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 50, wait = True)

myCkAct.makePlusMovement([500,0,200,-180,0,0],speed = 100,length = 50,numTimes = 3, wait = True)
arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 50, wait = True)

myCkAct.sprinkle([500,-30,250,-180,0,0],numTimes=5,wait = True)
arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 50, wait = True)

arm.move_gohome()
arm.disconnect()