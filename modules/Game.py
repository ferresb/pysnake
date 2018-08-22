import curses
import sys
from modules.Interface import Interface
from modules.Snake import Snake

from modules.CustomException import GameOver

class Game:
    def __init__(self):
        self.__interface = Interface()
        self.__interface.createBorder()
        self.__interface.addCenter("SNAKE")

        (self.__dimX, self.__dimY) = self.__interface.getDim()
        self.__cursor = self.__interface.initCursor((self.__dimX-1, self.__dimY-1), (1, 1))

        self.__cursor.goto(int(self.__dimX/2), int(self.__dimY/2))
        self.__snake = Snake(self.__cursor)

    def run(self):
        while 1:
            try:
                self.__snake.draw(self.__interface)
                c = self.__interface.getInput()
                if c == ord('q') or c == ord('Q'):
                    break
                elif c == 65: self.__snake.move(self.__interface, "UP")
                elif c == 66: self.__snake.move(self.__interface, "DOWN")
                elif c == 68: self.__snake.move(self.__interface, "LEFT")
                elif c == 67: self.__snake.move(self.__interface, "RIGHT")
            except GameOver:
                self.__endLoop()

    def __endLoop(self):
        self.__interface.addCenter("You lost !", int(self.__dimY/2))
        while 1:
            c = self.__interface.getInput()
            if c == ord('q') or c == ord('Q'):
                self.destroy()                
                sys.exit()
                

    def destroy(self):
        self.__interface.destroy()
