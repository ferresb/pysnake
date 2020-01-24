
from modules.Point import Point
from modules.Utils import *

class PointArray:
    def __init__(self):
        self.__points = []

    def add(self, p):
        self.__points.append(Point.copy(p))

    def remove(self,p):
        for point in self.__points:
            if point.isEqual(p):
                logger.info("Removed point" + str(point.getXY()))
                self.__points.remove(point)
                self.log("Array is now")

    def get(self):
        return self.__points

    def len(self):
        logger.info("Array len is now "+str(len(self.__points)))
        return len(self.__points)

    def log(self, title):
        str_ = "PointArray:"+title
        for a in self.__points:
            str_ = str_ + str(a.getXY())
        logger.info(str_)
