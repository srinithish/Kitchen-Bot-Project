from xarm.wrapper import XArmAPI

#import numpy as np







class mainActions:
    
    def __init__(self,armHandle):
        
        self._armHandle = armHandle
        # TODO:check for sanity and coonection
        
        pass
    
    
    def setStateAndConnect():
        pass
    
    
    
    def holdObject(self,value):
        
        """
        holds the object with gripper value
        """
        
        armHandle = self._armHandle
        armHandle.set_gripper_position(600, wait=True)
        pass
    
    def releaseObject(self):
        
        """
        releases the object completely
        """
        armHandle = self._armHandle
        armHandle.set_gripper_position(600, wait=True)
        
        pass
    
    
    def traverseWithGripperHorizontal(self,startPos,endPose,wait = True):
        
        
        armHandle = self._armHandle
        
        
        
        ## if y is +ve
        if startPos[1] > 0:
        
            xRoll = -90
        
        
        ## if y is -ve
        elif  startPos[1] < 0:
            
            xRoll = 90
        
        
        elif  startPos[1] == 0:
            
            xRoll = 180
        
        ##over ridding orientations
        ## assisting x axis rotation roll
        startPos[3:] = [-180,90,0]
        armHandle.set_position(*startPos,  wait=wait,is_radian  = False)
        
        
        ##first pos
        startPos[3:] = [xRoll,90,0]
        armHandle.set_position(*startPos,  wait=wait,is_radian  = False)
        
        ##second pose
        endPose[3:] = [xRoll,90,0]
        armHandle.set_position(*endPose,  wait=wait,is_radian  = False)
        
        pass
    
    
    def traverseWithGripperVertical(self,startPos,endPose,wait = True):
        
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
        
        
        
        armHandle.set_position(**kwargs,relative = True)
        
        
        
        pass
        
        
        
if __name__ == '__main__':
    
    myAct = mainActions('hello')
    myAct.approach(x=200)
    
    
    
    
    