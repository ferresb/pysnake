#!/bin/python
from modules.CustomException import CursorError

class Cursor:
    def __init__(self, screen, maxdim=(-1, -1), mindim=(0, 0)):
        self.__x = 0
        self.__y = 0
        self.__screen = screen
        if maxdim == (-1, -1):
            (self.__maxy, self.__maxx) = screen.getmaxyx() # ! Stored as (y, x)
        else:
            (self.__maxx, self.__maxy) = maxdim
        (self.__minx, self.__miny) = mindim
    
    def __actualize(self):
        (self.__y, self.__x) = self.__screen.getyx() # ! Stored as (y, x)

    def __refresh(self):
        self.__screen.move(self.__y, self.__x)
        self.__screen.refresh()

    def getCoordinates(self):
        self.__actualize()
        return (self.__x, self.__y)
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

# Set dimensions for available moves
    def setMaxX(self, x):
        self.__maxx = x

    def setMaxY(self, y):
        self.__maxy = y

    def setMinX(self, x):
        self.__minx = x

    def setMinY(self, y):
        self.__miny = y
    
# Relative movements
    def move(self, direction):
        self.__actualize()
        if direction == "UP":
            if self.__y > self.__miny:
                self.__y -= 1
        elif direction == "DOWN":
            if self.__y < self.__maxy - 1:
                self.__y += 1
        elif direction == "LEFT":
            if self.__x > self.__minx:
                self.__x -= 1
        elif direction == "RIGHT":
            if self.__x < self.__maxx - 1:
                self.__x += 1
        else:
            raise CursorException("Direction unknown : {}".format(direction))
        self.__refresh()

    def isOutOfBound(self, direction):
        self.__actualize()
        if direction == "UP":
            if self.__y > self.__miny:
                return False
        elif direction == "DOWN":
            if self.__y < self.__maxy - 1:
                return False
        elif direction == "LEFT":
            if self.__x > self.__minx:
                return False
        elif direction == "RIGHT":
            if self.__x < self.__maxx - 1:
                return False
        else:
            raise CursorException("Direction unknown : {}".format(direction))
        return True

# Absolute movements
    def goto(self, x, y):
        self.__actualize()
        self.__x = x
        self.__y = y
        self.__refresh()

    def gotoX(self, x):
        self.__actualize()
        self.__x = x
        self.__refresh()

    def gotoY(self, y):
        self.__actualize()
        self.__y = y
        self.__refresh()
