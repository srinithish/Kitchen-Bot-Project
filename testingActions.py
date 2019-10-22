import os
import sys
import time

from cookingActions import cookingActions
from cookingActions2 import cookingActions2
from mainActions import mainActions
from xarm.wrapper import XArmAPI
from configparser import ConfigParser
import prepareNoodles


parser = ConfigParser()
parser.read('./robot1.conf')
ip1 = parser.get('xArm', 'ip')
parser.read('./robot2.conf')
ip2 = parser.get('xArm', 'ip')


arm1 = prepareNoodles.initialiseArms(ip1)
arm2 = prepareNoodles.initialiseArms(ip2)

myCkAct1 = cookingActions(arm1,speed = 900,mvacc = 900,wait = True)
myCkAct2 = cookingActions(arm2,speed = 900,mvacc = 900,wait = True)

myCkAct1.customGoHome(wait=True)
myCkAct2.customGoHome(wait=True)

# prepareNoodles.switchStoveOn()
# prepareNoodles.pickGlassAndPour()
# prepareNoodles.sprinkleSalt()
# prepareNoodles.sprinklePepper()
# prepareNoodles.sprinkleFlakes()
# prepareNoodles.sprinkleFlavor()
# prepareNoodles.pickAndPlaceNoodles()
# prepareNoodles.holdPan()
# prepareNoodles.pickStirrerAndStir()
# prepareNoodles.releasePan()
# prepareNoodles.switchStoveOff()

arm1.disconnect()
arm2.disconnect()

