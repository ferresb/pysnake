import random
from modules.Point import Point

class AppleGenerator:
    def __init__(self, minDim, maxDim):
        (self.__minX, self.__minY) = minDim
        (self.__maxX, self.__maxY) = maxDim
        random.seed()

    def generate(self, points):
        p = Point(-1, -1) 
        while (p.x < 0 and p.y < 0) or (p.belongs(points)):
            p.x = random.randint(self.__minX, self.__maxX)
            p.y = random.randint(self.__minY, self.__maxY)
        return p
