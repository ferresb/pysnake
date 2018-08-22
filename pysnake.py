from modules.Game import Game

def main():
    game = Game()
    try:
        game.run()
    finally:
        game.destroy()

if __name__=="__main__":
    main()
