# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:46:47 2019

@author: GELab
"""



from xarm.wrapper import XArmAPI

#import numpy as np




class cookingActions:
    
    def __init__(self,armHandle):
        
        self._armHandle = armHandle
        # TODO:check for sanity and coonection
        
        pass
    
    
    def setStateAndConnect():
        pass
    
    
    def stir(self,circleCenterWithOrient,speed,radius,numTimes,wait):
        
        
        """
        assumes the TCP is at the center but only differeing by z
        
        """
        armHandle = self._armHandle
        
        initPosition = list(circleCenterWithOrient)
        initPosition[1]  = initPosition[1] - radius ## change y go up by radius
        
        armHandle.set_position(*initPosition, speed=speed, is_radian=False, wait=wait) ## reach the upper point
        print(armHandle.get_position(), armHandle.get_position(is_radian=False))
        
        
        Point2 = list(circleCenterWithOrient)
        Point2[0] = Point2[0]+radius## change x to go right by radius
        
        Point3 = list(circleCenterWithOrient)
        Point3[1] = Point3[1]+radius ##change y to go down by radius
        
        percent = numTimes*100
        ret = armHandle.move_circle(pose1=Point2, pose2=Point3, 
                                    percent=percent, speed=speed, mvacc=100, wait=wait,is_radian=False)
        print('move_circle, ret: {}'.format(ret))
        
        
        
        pass
    
    def makePlusMovement(self,centerPosWithOrient,speed,length,numTimes,wait):
        armHandle = self._armHandle
        initPosition = list(centerPosWithOrient)
        ##center
        armHandle.set_position(*initPosition, speed=speed, is_radian=False, wait=wait) #reach the center point
        print(armHandle.get_position(), armHandle.get_position(is_radian=False))
        
        
        ## extreme up
        armHandle.set_position(y=length, relative=True, wait=wait)
        print(armHandle.get_position(), armHandle.get_position(is_radian=False))
        
        ## extreme down
        armHandle.set_position(y=-2*length, relative=True, wait=wait)
        
        ## center again
        armHandle.set_position(*initPosition, speed=speed, is_radian=False, wait=wait)
        
        
        ## extreme left
        armHandle.set_position(x=-length, relative=True, wait=wait)
        
        ##extreme right
        armHandle.set_position(x= 2*length, relative=True, wait=wait)
        
        ## center again
        armHandle.set_position(*initPosition, speed=speed, is_radian=False, wait=wait)
        
        
        
        pass
        
    
    def flip(self):
        
        
        pass
    
    
    def sprinkle(self, centerPosWithOrient,numTimes,speed, mvacc, wait):
        
        
        """
        imagines the Tool Orientation is upright 
        
        """
        
        
        armHandle = self._armHandle

        initPosition = list(centerPosWithOrient)
        
        # TODO: yet to decide roll or pitch or yaw
        ##position at 45
        armHandle.set_position(*initPosition,speed = speed, wait=wait,is_radian  = False)
        
        
        
        ### loop here
        for i in range(numTimes):
        ### jerk move front
            armHandle.set_position(x = 50,z = -200,pitch = +45, relative=True,mvacc=mvacc, wait=wait,is_radian  = False)

            ### jerk move back
            armHandle.set_position(x = -50,z = 200,pitch = -45,relative=True, mvacc=mvacc, wait=wait,is_radian  = False)

        pass
    
    
    def pour(self, centerPosWithOrient,pourDegree,wait):
        
        armHandle = self._armHandle
        
        # TODO: yet to decide roll or pitch or yaw
        armHandle.set_position(roll = +45, relative=True, wait=wait,is_radian  = False)
        
        
        
        
        pass
        
        
        
        
        
        