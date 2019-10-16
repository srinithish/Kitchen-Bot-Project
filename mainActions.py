
"""
@author: nithish
"""

from xarm.wrapper import XArmAPI


# import numpy as np


class mainActions:

    def __init__(self, armHandle, **kwargs):

        """
        @params:
            armHandle : required
            
            wait: default True
            
            speed: default 100

            mvacc: default 100
        """

        self._armHandle = armHandle
        # TODO:check for sanity and coonection

        self._speed = kwargs.get('speed', 100)
        self._mvacc = kwargs.get('mvacc', 100)
        self._wait = kwargs.get('wait', True)

        pass

    def setStateAndConnect():
        pass

    def _getDefaults(self, **kwargs):
        
        """
        gets default speed,mvacc,wait if not passed or is None
        """

        speed = self._speed if kwargs.get('speed', None) is None else kwargs['speed']
        mvacc = self._mvacc if kwargs.get('mvacc', None) is None else kwargs['mvacc']
        wait = self._wait if kwargs.get('wait', None) is None else kwargs['wait']

        return speed, mvacc, wait

    def customGoHome(self):

        armHandle = self._armHandle

        # TODO: convert to servo angle
        #        armHandle.set_mode(1)

        armHandle.set_servo_angle(angle = [0,-43.3,0,17.6,0,60.9,0],speed = 100,mvacc = 10,wait  = True)

        #        armHandle.set_mode(0)
        # armHandle.set_position(250, 0, 150, -180, 0, 0,
        #                        speed=100, mvacc=10,
        #                        wait=True, is_radian=False)

        armHandle.set_gripper_position(100, wait=True)

        pass

    def holdObject(self, value):

        """
        holds the object with gripper value
        """

        armHandle = self._armHandle
        armHandle.set_gripper_position(value, wait=True)
        pass

    def releaseObject(self):

        """
        releases the object completely
        """
        armHandle = self._armHandle
        armHandle.set_gripper_position(800, wait=True)

        pass

    def _achieveHorizontalGripperPos(self, startPos):

        """
        Takes in start position that it wants to reach and decides the attitude to be
        negative Y or positive y

        
        Always reaches 250,y,400 and performs action
        

        @params:
            startPos: [x,y,z,attituted] uses only to decide the direiton of change

        """

        armHandle = self._armHandle

        if startPos[1] > 0:

            xRoll = -90
            y = 20

        ## if y is -ve
        elif startPos[1] <= 0:

            xRoll = 90
            y = -20

        ###a

        ## TODO : check these speeds and mvacc for valididty and change y if reqired
        armHandle.set_position(250, y, 400, -180, 90, 0, speed=100, mvacc=10,
                               wait=True, is_radian=False)

        armHandle.set_position(250, y, 400, xRoll, 90, 0, speed=100, mvacc=10,
                               wait=True, is_radian=False)

        ## return orientation
        return armHandle.get_position(is_radian=False)[1][3:]

    def _achieveVerticalGripperPos(self, startPos):

        """
        no use of start pos
        """

        armHandle = self._armHandle

        ## TODO may require to do in joint angles
        armHandle.set_position(250, 0, 400, -180, 0, 0, speed=100, mvacc=10,
                               wait=True, is_radian=False)

        pass

    def achieveAttitude(self):
        """
        could be used to dynamically orient to an object
        """

        pass

    def horizontalPick(self, startPos, approachAfterStart,
                       gripHoldValues,
                       speed=None, mvacc=None, wait=None):

        """
        Achieves horizontal position first

        @params:
            startPos: where to standby for picking up the object
            endPos: the endpoint at where the object has to be placed

            approachAfterStart: dict of what movements to make relative {x:100,y:100}
            
            gripHoldValues: tuple(startGripper,endGripper)

        """

        armHandle = self._armHandle

        ##speed, mvacc, wait overridden with defauls if not provided
        speed, mvacc, wait = self._getDefaults(speed=speed, mvacc=mvacc, wait=wait)

        ##horizaontal position achieved
        horizontalPosAngles = self._achieveHorizontalGripperPos(startPos)

        ##before gripper position
        self.holdObject(gripHoldValues[0])

        ##reach start pos
        startPos[3:] = horizontalPosAngles
        armHandle.set_position(*startPos, wait=wait, is_radian=False)

        ###approach the object
        self.approach(**approachAfterStart)

        ###hold the object
        self.holdObject(gripHoldValues[1])

        
        ###lift the object of the surface
        self.approach(z= -50)
        
        

        ###go back by approach

        reverseApproachAfterStart = {key: -value for key, value in approachAfterStart.items()}
        self.approach(**reverseApproachAfterStart)

        ##second pose

        return armHandle.get_position(is_radian=False)[1]

    def horizontalPlace(self, endPose, approachAfterEnd,
                        gripHoldValue,
                        speed=None, mvacc=None, wait=None):

        """
        Always succeds a horizontal Pick
        Assumes object already held by gripper

        @params:
            endPose : position before approach

            approachEnd: dict of what movements to make relative {x:100,y:100}

        """
        armHandle = self._armHandle

        ##speed, mvacc, wait overridden with defauls if not provided
        speed, mvacc, wait = self._getDefaults(speed=speed, mvacc=mvacc, wait=wait)

        ### assumes horizontal Pick was performed
        horizontalPosAngles = armHandle.get_position(is_radian=False)[1][3:]

        ## TODO: check for validity of horizontal gripper positions

        endPose[3:] = horizontalPosAngles
        armHandle.set_position(*endPose, speed=speed, mvacc=mvacc, wait=wait, is_radian=False)

        ###approach the object
        self.approach(**approachAfterEnd)

        ###release the object
        self.holdObject(gripHoldValue)

        ###go back by approach

        reverseApproachAfterStart = {key: -value for key, value in approachAfterEnd.items()}
        self.approach(**reverseApproachAfterStart)

        return armHandle.get_position(is_radian=False)[1]

    def verticalPick(self, startPos, approachAfterStart,
                     gripHoldValues,
                     speed=None, mvacc=None, wait=None):

        """
        Orientation should and change
        Overrides orienations

        @params:
            gripHoldValues = (before,after)


        @return:

            current position list
        """

        armHandle = self._armHandle
        speed, mvacc, wait = self._getDefaults(speed=speed, mvacc=mvacc, wait=wait)

        ##before gripper position
        self.holdObject(gripHoldValues[0])
        ##over ridding orientations

        ## TODO: Achieve vertical attitutde here through function
        startPos[3:] = [-180, 0, 0]
        armHandle.set_position(*startPos, speed=speed, mvacc=mvacc, wait=wait, is_radian=False)

        ###approach the object
        self.approach(**approachAfterStart)

        ###hold the object
        self.holdObject(gripHoldValues[1])

        ###go back by approach
        reverseApproachAfterStart = {key: -value for key, value in approachAfterStart.items()}
        self.approach(**reverseApproachAfterStart)

        return armHandle.get_position(is_radian=False)[1]

    def verticalPlace(self, endPose, approachAfterEnd,
                      gripHoldValue=600,
                      speed=None, mvacc=None, wait=None):

        """
        assumes already holding an object
        """
        armHandle = self._armHandle
        speed, mvacc, wait = self._getDefaults(speed=speed, mvacc=mvacc, wait=wait)

        ##go to end position
        endPose[3:] = [-180, 0, 0]
        armHandle.set_position(*endPose, speed=speed, mvacc=mvacc, wait=wait, is_radian=False)

        ###approach the table
        self.approach(**approachAfterEnd)

        ###place the object
        self.holdObject(gripHoldValue)

        ###go back by approach and stand by there
        reverseApproachAfterStart = {key: -value for key, value in approachAfterEnd.items()}
        self.approach(**reverseApproachAfterStart)

        return armHandle.get_position(is_radian=False)[1]

    def traverseWithPrevAttitude(self, endPosOnlyList,
                                 speed=None, mvacc=None, wait=None):

        """
        Traverse to the new location continuing present attitude
        @ params:
            endPosOnlyList : [x,y,z]



        """
        armHandle = self._armHandle
        speed, mvacc, wait = self._getDefaults(speed=speed, mvacc=mvacc, wait=wait)

        prevAttitutde = armHandle.get_position(is_radian=False)[1][3:]

        armHandle.set_position(*endPosOnlyList, *prevAttitutde,
                               speed=speed, mvacc=mvacc, wait=wait, is_radian=False)

        return armHandle.get_position(is_radian=False)[1]

    def approach(self,speed=None,mvacc = None,wait = None, **kwargs):

        """
        @params:
            kwargs = {x:+100,y:-100,....}

        reaches a initial positin near the object and then travels relative
        in the direction of approach to grab the object


        @return :
        """
        ## TODO: make kwargs and delete for wait

        armHandle = self._armHandle

        speed, mvacc, wait = self._getDefaults(speed=speed, mvacc=mvacc, wait=wait)

        armHandle.set_position(**kwargs, relative=True, speed=speed, mvacc=mvacc, wait=wait)

        return armHandle.get_position(is_radian=False)[1]


if __name__ == '__main__':
    myAct = mainActions('hello')
    #    myAct.approach(x=200)
    myAct._getDefaults(speed=200, mvacc=100, wait=True)




