
from xarm.wrapper import XArmAPI

class cookingActions2:

    def __init__(self, armHandle):

        self._armHandle = armHandle
        # TODO:check for sanity and connection

        pass

    def stirWithOrient(self, circleCenterWithOrient, orient, speed, radius, numTimes, wait):

        self._armHandle = armHandle

        initPosition = list(circleCenterWithOrient)
        initPosition[1] = initPosition[1] - radius  ## change y go up by radius

        armHandle.set_position(*initPosition, speed=speed, is_radian=False, wait=wait)  ## reach the upper point
        print(armHandle.get_position(), armHandle.get_position(is_radian=False))

        Point2 = list(circleCenterWithOrient)
        Point2[0] = Point2[0] + radius  ## change x to go right by radius

        Point3 = list(circleCenterWithOrient)
        Point3[1] = Point3[1] + radius  ##change y to go down by radius
        Point3[4] = -orient

        # percent = numTimes * 100
        for i in range(1, numTimes):
            ret = armHandle.move_circle(pose1=Point2, pose2=Point3,
                                        percent=100, speed=speed, mvacc=50, wait=wait, is_radian=False)
            print('move_circle, ret: {}'.format(ret))
            armHandle.set_position(pitch=+orient, wait=wait, is_radian=False, speed=400)

        pass

    def stirAnyPlane(self, circleCenterWithOrient,plane, speed, radius, numTimes, wait):

        #XYplane = 0
        #YZplane = 1
        #XZplane = 2

        armHandle = self._armHandle

        valid = {0, 1, 2}
        if plane not in valid:
            raise ValueError("given plane not in " % valid)

        if plane == 2:
            i = 0
        else:
            i = plane+1

        initPosition = list(circleCenterWithOrient)
        initPosition[i] = initPosition[i] - radius

        armHandle.set_position(*initPosition, speed=speed, is_radian=False, wait=wait)
        print(armHandle.get_position(), armHandle.get_position(is_radian=False))

        Point2 = list(circleCenterWithOrient)
        Point2[plane] = Point2[plane] + radius

        Point3 = list(circleCenterWithOrient)
        Point3[i] = Point3[i] + radius

        percent = numTimes * 100
        ret = armHandle.move_circle(pose1=Point2, pose2=Point3,
                                    percent=percent, speed=speed, mvacc=100, wait=wait, is_radian=False)
        print('move_circle, ret: {}'.format(ret))

        pass

    def stirEight(self, circleCenterWithOrient, speed, radius, numTimes, wait):

        armHandle = self._armHandle

        radius = radius / 2

        initPosition = list(circleCenterWithOrient)

        armHandle.set_position(*initPosition, speed=speed, is_radian=False, wait=wait)  ## reach the centre of eight
        print(armHandle.get_position(), armHandle.get_position(is_radian=False))

        Point2 = list(circleCenterWithOrient)
        Point2[0] = Point2[0] + 2 * radius

        Point3 = list(circleCenterWithOrient)
        Point3[0] = Point3[0] + radius
        Point3[1] = Point3[1] + radius

        Point4 = list(circleCenterWithOrient)
        Point4[0] = Point4[0] - 2 * radius

        Point5 = list(circleCenterWithOrient)
        Point5[0] = Point5[0] - radius
        Point5[1] = Point5[1] - radius

        for i in range(1, numTimes):
            ret = armHandle.move_circle(pose1=Point2, pose2=Point3,
                                        percent=100, speed=speed, mvacc=100, wait=wait, is_radian=False)
            print('move_circle, ret: {}'.format(ret))


            ret = armHandle.move_circle(pose1=Point4, pose2=Point5,
                                        percent=100, speed=speed, mvacc=100, wait=wait, is_radian=False)
            print('move_circle, ret: {}'.format(ret))


        pass
