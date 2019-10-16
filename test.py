import os
import sys
import time

from cookingActions import cookingActions
from cookingActions2 import cookingActions2
from mainActions import mainActions
from xarm.wrapper import XArmAPI
from configparser import ConfigParser

parser = ConfigParser()
parser.read('./robot1.conf')

ip = parser.get('xArm', 'ip')

def handle_err_warn_changed(item):
    print('ErrorCode: {}, WarnCode: {}'.format(item['error_code'], item['warn_code']))
    # TODO：Do different processing according to the error code

arm = XArmAPI(ip, do_not_open=True, is_radian=False)
arm.register_error_warn_changed_callback(handle_err_warn_changed)
arm.connect()


# enable motion
arm.motion_enable(enable=True)
# set mode: position control mode
arm.set_mode(0)
# set state: sport state
arm.set_state(state=0)

## actions here
myCkAct = cookingActions(arm)
myCkAct2 = cookingActions2(arm)
myMainAct = mainActions(arm)

myMainAct.customGoHome()
print(arm.last_used_joint_acc,arm.last_used_joint_speed)

arm.set_position(450,0,250,-180,0,0,speed = 100, mvacc = 100, wait = False)
time.sleep(1)
arm.set_state(3)
time.sleep(5)
arm.set_state(0)


myMainAct.customGoHome()