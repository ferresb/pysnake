#!/bin/python
import curses
from modules.Cursor import Cursor

class Interface:
    def __init__(self, delay=250):
        self.__screen = curses.initscr()
        self.__screen.timeout(delay)
        curses.noecho()
        curses.cbreak()
        (maxX, maxY) = self.getDim()

    def initCursor(self, maxDim=(-1, -1), minDim=(0, 0)):
        return Cursor(self.__screen, maxDim, minDim)

# Clear functions
    def clearScreen(self):
        (y, x) = self.__screen.getmaxyx()
        for i in range(0, x-1):
            for j in range(0, y-1):
                self.addString(i, j, " ")
        self.refresh()
    
    def clearLine(self, line, bpos=0, epos=-1):
        (y, x) = self.__screen.getmaxyx()
        if line > y-1:
            return
        if epos == -1:
            epos = x-1
        for i in range(bpos, epos):
            self.addString(i, line, " ")
        self.refresh()

    def clearPoint(self, cursor, x, y, char=" "):
        (ox, oy) = cursor.getCoordinates()
        self.addString(x, y, char)
        cursor.goto(ox, oy)
        self.refresh()

    def refresh(self):
        self.__screen.refresh()

# Graphical Primitives
    def addString(self, x, y, string):
        self.__screen.addstr(y, x, string)

    def addVerticalLine(self, x, delta):
        for y in range (0,delta):
            self.addString(x, y, "|")
    
    def addHorizontalLine(self, y, delta):
        line = delta * "-"
        self.addString(0, y, line)

    def createBorder(self):
        (maxX, maxY) = self.getDim()
        self.addVerticalLine(0, maxY-1)
        self.addVerticalLine(maxX-1, maxY-1)
        self.addHorizontalLine(0, maxX)
        self.addHorizontalLine(maxY-1, maxX-1)
        self.refresh()

    def addCenter(self, title, line=0):
        title = "   {}   ".format(title)
        (maxX, __) = self.getDim()
        initX = int((maxX - len(title))/2)
        self.addString(initX, line, title)
        self.refresh()

    def draw(self, points, cursor, char='o'):
        (x, y) = cursor.getCoordinates()
        for point in points:
            self.addString(point.x, point.y, char)
        cursor.goto(x, y)
        self.refresh()

    def drawPoint(self, point, cursor, char='o'):
        (x, y) = cursor.getCoordinates()
        self.addString(point.x, point.y, char)
        cursor.goto(x, y)
        self.refresh()
        
# Inputs
    def getInput(self):
        return self.__screen.getch()

    def getDim(self):
        (maxY, maxX) = self.__screen.getmaxyx()
        return (maxX, maxY)

# Lifecycle
    def destroy(self):
        curses.endwin()
