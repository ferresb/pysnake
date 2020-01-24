import curses
import sys

from modules.Utils import *

from modules.Interface import Interface
from modules.Snake import Snake
from modules.Score import Score
from modules.PointArray import PointArray
from modules.AppleGenerator import AppleGenerator

from modules.CustomException import *

class Game:
    def __init__(self):
        self.__interface = Interface()
        self.__interface.createBorder()
        self.__interface.addCenter("SNAKE")

        (self.__dimX, self.__dimY) = self.__interface.getDim()
        self.__cursor = self.__interface.initCursor((self.__dimX-1, self.__dimY-1), (1, 1))

        self.__cursor.goto(int(self.__dimX/2), int(self.__dimY/2))
        self.__counter      = 0
        self.__apples       = PointArray()
        self.__snake        = Snake(self.__cursor, self.__apples, self.__interface, BASE_SIZE)

        self.__generator    = AppleGenerator((1,1), (self.__dimX-2, self.__dimY-2))
        self.__score        = Score(self.__interface, self.__cursor)

    def run(self):
        while 1:
            try:
                self.__snake.draw() 
                self.__counter += 1
                if (self.__counter >= APPLE_RATE and self.__apples.len() < MAX_APPLE):
                    p = self.__generator.generate(self.__snake.getPoints())
                    p.draw(self.__interface, self.__cursor)
                    self.__apples.add(p)
                    self.__counter = 0
                    self.__apples.log("apple_str")
                c = self.__interface.getInput()
                if c == ord('q') or c == ord('Q'):
                    self.__apples.log("End")
                    break
                elif c == 65: self.__snake.move(Direction.UP)
                elif c == 66: self.__snake.move(Direction.DOWN)
                elif c == 68: self.__snake.move(Direction.LEFT)
                elif c == 67: self.__snake.move(Direction.RIGHT)
                elif c == -1: self.__snake.move(None)
            except GameOver as e:
                self.__endLoop(e)
            except MoveImpossible:
                pass

    def __endLoop(self, e):
        self.__interface.addCenter("You lost because {}!".format(str(e)), int(self.__dimY/2))
        while 1:
            c = self.__interface.getInput()
            if c == ord('q') or c == ord('Q'):
                self.destroy()                
                sys.exit()

    def destroy(self):
        self.__interface.destroy()
