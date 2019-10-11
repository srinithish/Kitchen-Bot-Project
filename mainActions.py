from xarm.wrapper import XArmAPI

#import numpy as np







class mainActions:
    
    def __init__(self,armHandle):
        
        self._armHandle = armHandle
        # TODO:check for sanity and coonection
        
        pass
    
    
    def setStateAndConnect():
        pass
    
    
    def customGoHome(self):
        
        armHandle = self._armHandle
        
        
#        armHandle.set_mode(1)
        
#        armHandle.set_servo_angle(angle = [0,0,0,45,0,45,0],speed = 10,mvacc = 1)
        
        armHandle.set_position(250, 0, 150, -180, 0, 0,
                               speed = 100 ,mvacc = 100,
                               wait=True,is_radian  = False)
        
        
        armHandle.set_gripper_position(100, wait=True)
#        armHandle.set_mode(0)
        
        
        pass
        
        
    def holdObject(self,value):
        
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
    
    
    def _achieveHorizontalGripperPos(self,startPos):
        
        
        
        armHandle = self._armHandle
        
        if startPos[1] > 0:
        
            xRoll = -90
            y = 20
        
        ## if y is -ve
        elif  startPos[1] <= 0:
            
            xRoll = 90
            y = -20
            
        
        ###a
        armHandle.set_position(250,y,400,-180,90,0,  wait=True,is_radian  = False)
        
        
        armHandle.set_position(250,y,400,xRoll,90,0,  wait=True,is_radian  = False)
        
        
        
        ## return orientation
        return armHandle.get_position(is_radian = False)[1][3:]
    
    
    
    def horizontalPickAndPlace(self,startPos,endPose,wait = True):
        
        
        armHandle = self._armHandle
        
        
        
        self._achieveHorizontalGripperPos(startPos)
        
        ## if y is +ve
        if startPos[1] > 0:
        
            xRoll = -90
        
        
        ## if y is -ve
        elif  startPos[1] <= 0:
            
            xRoll = 90
        
    
        
        
        
        ##first pos
        startPos[3:] = [xRoll,90,0]
        armHandle.set_position(*startPos,  wait=wait,is_radian  = False)
        
        ##second pose
        endPose[3:] = [xRoll,90,0]
        armHandle.set_position(*endPose,  wait=wait,is_radian  = False)
        
        pass
    
    
    def verticalPickAndPlace(self,startPos,endPose,wait = True):
        
        """
        Orientation should and change
        Overrides orienations
        """
        armHandle = self._armHandle
        
        
        ##over ridding orientations
        startPos[3:] = [-180,0,0]
        endPose[3:] = [-180,0,0]
        
        
        armHandle.set_position(*startPos,  wait=wait,is_radian  = False)
        
        armHandle.set_position(*endPose,  wait=wait,is_radian  = False)
        
        pass
    
    
    def approach(self,**kwargs):
        
        """
        reaches a initial positin near the object and then travels relative 
        in the direction of approach to grab the object
        
        """
        armHandle = self._armHandle

        armHandle.set_position(**kwargs,relative = True,wait = True)

        
        
        pass
        
    
        
if __name__ == '__main__':
    
    myAct = mainActions('hello')
    myAct.approach(x=200)
    
    
    
    
    