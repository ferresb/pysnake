from modules.Utils import *

from modules.Cursor import Cursor
from modules.Point import Point
from modules.LinkedList import LinkedList

from modules.CustomException import *

class Snake:
    def __init__(self, cursor, apples, length=3):
        self.__cursor = cursor
        self.__points = LinkedList(Point(cursor.getX(), cursor.getY()))
        self.__apples = apples
        #Manage length too long
        for i in range (1, length):
            self.__points.addElemLast(Point(cursor.getX()-i, cursor.getY()))
        self.__cursor.goto(cursor.getX(), cursor.getY())

    def getX(self):
        return self.__cursor.getX()

    def getY(self):
        return self.__cursor.getY()

    def getCoordinates(self):
        return self.__cursor.getCoordinates()

    def getPoints(self):
        return self.__points.getPoints()

    def getDirection(self):
        (x, y) = (self.__points.head.x, self.__points.head.y)
        (ox, oy) = (self.__points.head.next.x, self.__points.head.next.y)

        if (x == ox):
            if (y > oy):
                return Direction.DOWN
            return Direction.UP
        elif (x > ox):
            return Direction.RIGHT
        return Direction.LEFT

# Movements
    def move(self, interface, direction=None):
        direction = direction if direction != None else self.getDirection()
        if self.__cursor.isOutOfBound(direction):
            raise GameOver("you reached game border")
        if self.__isGoingBack(direction):
            raise MoveImpossible("going back")
        if self.__willCollide(direction):
            raise GameOver("a collision occured")
        self.__cursor.move(direction)
        self.__removeCollisionIfExists()
        self.__points.addElemFirst(Point(self.__cursor.getX(), self.__cursor.getY()))
        self.__points.tail.erase(interface, self.__cursor)
        #interface.clearPoint(self.__cursor, self.__points.tail.x, self.__points.tail.y)
        self.__points.remElemLast()

# Display
    def draw(self, interface):
        interface.draw(self.__points.getPoints(), self.__cursor)

# Logic
    def __removeCollisionIfExists(self):
        if (self.__apples== None):
            return False
        for p in self.__apples:
            if p.isEqual(self.__cursor.getPoint()):
                self.__apples.pop(p)
                return True
        return False

    def __isGoingBack(self, direction):
        p = self.__calcPoint(direction)
        if p.isEqual(self.__points.head.next):
            return True
        return False

    def __willCollide(self, direction):
        p = self.__calcPoint(direction)
        return p.belongs(self.__points.getPoints())

    def __calcPoint(self, direction):
        (x, y) = self.__cursor.getCoordinates()
        if direction == Direction.UP:
            y -= 1
        elif direction == Direction.DOWN:
            y += 1
        elif direction == Direction.LEFT:
            x -= 1
        elif direction == Direction.RIGHT:
            x += 1
        else:
            raise CursorError("Direction unknown : {}".format(direction))
        return Point(x, y)
