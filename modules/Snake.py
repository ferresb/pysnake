from modules.Cursor import Cursor
from modules.Point import Point
from modules.LinkedList import LinkedList

from modules.CustomException import GameOver
from modules.CustomException import MoveImpossible

class Snake:
    def __init__(self, cursor, length=3):
        self.__cursor = cursor
        self.__points = LinkedList(Point(cursor.getX(), cursor.getY()))
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

    def getDirection(self):
        (x, y) = (self.__points.head.x, self.__points.head.y)
        (ox, oy) = (self.__points.head.next.x, self.__points.head.next.y)

        if (x == ox):
            if (y > oy):
                return "DOWN"
            return "UP"
        elif (x > ox):
            return "RIGHT"
        return "LEFT"

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
        self.__points.addElemFirst(Point(self.__cursor.getX(), self.__cursor.getY()))
        interface.clearPoint(self.__cursor, self.__points.tail.x, self.__points.tail.y)
        self.__points.remElemLast()

# Display
    def draw(self, interface):
        interface.draw(self.__points.getPoints(), self.__cursor)

# Logic
    def __isGoingBack(self, direction):
        p = self.__calcPoint(direction)
        if p.isEqual(self.__points.head.next):
            return True
        return False

    def __willCollide(self, direction):
        p = self.__calcPoint(direction)
        for point in self.__points.getPoints():
            if point.isEqual(p):
                return True
        return False

    def __calcPoint(self, direction):
        (x, y) = self.__cursor.getCoordinates()
        if direction == "UP":
            y -= 1
        elif direction == "DOWN":
            y += 1
        elif direction == "LEFT":
            x -= 1
        elif direction == "RIGHT":
            x += 1
        else:
            raise CursorException("Direction unknown : {}".format(direction))
        return Point(x, y)
