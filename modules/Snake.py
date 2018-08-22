from modules.Cursor import Cursor
from modules.Point import Point
from modules.LinkedList import LinkedList

from modules.CustomException import GameOver

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
        (ox, oy) = (self.__points.head.prev.x, self.__points.head.prev.y)

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
        if not self.__cursor.isOutOfBound(direction):
            self.__cursor.move(direction)
            self.__points.addElemFirst(Point(self.__cursor.getX(), self.__cursor.getY()))
            interface.clearPoint(self.__cursor, self.__points.tail.x, self.__points.tail.y)
            self.__points.remElemLast()
        else:
            raise GameOver("Reached game border")
            

# Display
    def draw(self, interface):
        interface.draw(self.__points.getPoints(), self.__cursor)
