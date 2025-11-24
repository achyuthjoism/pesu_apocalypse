from game import *

if __name__ == '__main__':
    game = Game()

    while game.running:
        game.get_events()
        game.render()
