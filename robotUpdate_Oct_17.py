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
myMainAct = mainActions(arm,speed = 200)




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
myMainAct.approach(z = -120)
myCkAct.stir(speed = 100,radius = 50,numTimes=5,wait = True)

## get back to vertical position
myMainAct._achieveVerticalGripperPos([500,0,400,-180,0,0])

myMainAct.verticalPlace([510,-225,100,-180,0,0],{'z':-100},300)

myMainAct.approach(z = 200)



myMainAct.customGoHome()

"""
May be duplicate below
"""
# arm.set_position(510,-225,100,-180,0,0,speed = 100, mvacc = 100, wait = True)
#
#
# myMainAct.verticalPick([510,-225,100,-180,0,0],{'z':-100},(300,0))
# myMainAct.approach(z = 200)
# myMainAct._achieveHorizontalGripperPos([500,0,300,-180,0,0])
# myMainAct.traverseWithPrevAttitude([500,0,450])
# myMainAct.approach(z = -120)
# myCkAct.stir(speed = 100,radius = 50,numTimes=5,wait = True)
#
# ## get back to vertical position
# myMainAct._achieveVerticalGripperPos([500,0,400,-180,0,0])
#
# myMainAct.verticalPlace([510,-225,100,-180,0,0],{'z':-100},300)
#
# myMainAct.approach(z = 200)
# #arm.set_position(256,0,200,-180,0,0,speed = 100, mvacc = 100, wait = True)
#
#
# myMainAct.customGoHome()



"""
pick glass and pour

"""
#
#myMainAct.horizontalPick([293,-225,50,-180,0,0],{'y':-100},
#                               (900,700))
#myMainAct.approach(z = 200)

# myMainAct.horizontalPick([293,-225,50,-180,0,0],{'y':-100},
#                                (900,700),
#                                speed = None,mvacc=None,wait = None)
# myMainAct.approach(z = 200)
#
# myMainAct.traverseWithPrevAttitude([380,0,350])
# myCkAct.pour(-100,speed=100,mvacc=20,wait=True)
#
# myMainAct.approach(x= -100)
# myMainAct.horizontalPlace([293,-325,50,-180,0,0],{'y':-100},900)
# myMainAct.customGoHome()


"""
switch the stove on
"""
myMainAct.customGoHome()

arm.set_position(499,-200,250,-180,0,0,speed = 100, mvacc = 100, wait = True)
arm.set_position(yaw= -90, relative=True, wait =True,is_radian  = False)
arm.set_position(pitch= 54, relative=True, wait =True,is_radian  = False)
arm.set_gripper_position(200, wait=True)
myMainAct.approach(z= -215)
myMainAct.approach(y= 87)

arm.set_gripper_position(110, wait=True)

code,angles = arm.get_servo_angle(is_radian=False)
angles1= angles[:-1] + [angles[-1]+90]

arm.set_servo_angle( angle=angles1,
                     speed=None, mvacc=None, mvtime=None, is_radian=False,wait=True)

arm.set_gripper_position(500, wait=True)

arm.set_servo_angle( angle=angles,
                     speed=None, mvacc=None, mvtime=None, is_radian=False,wait=True)

arm.set_gripper_position(500, wait=True)

myMainAct.traverseWithPrevAttitude([499,-150,35])

myMainAct.approach(z= 100)

myMainAct.customGoHome()
arm.disconnect()
