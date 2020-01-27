from modules.Game import Game
import sys

def main(xDim=None, yDim=None):
    game = Game(xDim, yDim)
    try:
        game.run()
    finally:
        game.destroy()

if __name__=="__main__":
    if (len(sys.argv) > 1):
        main(int(sys.argv[1]), int(sys.argv[2]))
    else:
        main()
