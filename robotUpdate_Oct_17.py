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
myCkAct2 = cookingActions2(arm)
myMainAct = mainActions(arm)




myMainAct.customGoHome()
print(arm.last_used_joint_acc,arm.last_used_joint_speed)

"""
Pick handle and stir
"""


arm.set_position(510,-225,100,-180,0,0,speed = 100, mvacc = 100, wait = True)


myMainAct.verticalPick([510,-225,100,-180,0,0],{'z':-100},(300,0))
myMainAct.approach(z = 200)
myMainAct._achieveHorizontalGripperPos([500,0,300,-180,0,0])
myMainAct.traverseWithPrevAttitude([500,0,450])
myMainAct.approach(z = -150)
myCkAct.stir(speed = 200,radius = 50,numTimes=5,wait = True)

## get back to vertical position
myMainAct._achieveVerticalGripperPos([500,0,400,-180,0,0])

myMainAct.verticalPlace([510,-225,100,-180,0,0],{'z':-100},300)

myMainAct.approach(z = 200)
#arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 100, wait = True)

#time.sleep(5)
#arm.move_gohome()
#myMainAct.customGoHome()


"""
pick glass and pour

"""



















arm.disconnect()
