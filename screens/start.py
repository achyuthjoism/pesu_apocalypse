import pygame
from helper import *
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game

class Start:
    def __init__(self,game:"Game"):
        self.game = game
        self.background = pygame.image.load('assets/background.png').convert()
        self.txt = Text('PESU Apocalypse',WIDTH//2,100,100,color='Red')
        self.images = pygame.sprite.Group()
        dboos = Image('assets/dboos.jpg',150,300)
        renu = Image('assets/renu.jpg',WIDTH-150,300)
        self.images.add(dboos)
        self.images.add(renu)
        self.strings = pygame.sprite.Group()
        self.strings.add(self.txt)
        self.start_button = Button('Start',WIDTH//2,300)
        self.exit_button = Button('Exit',WIDTH//2,400)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.start_button)
        self.buttons.add(self.exit_button)

    def update(self):
        self.images.update()
        self.strings.update()
        self.buttons.update()

    def render(self):
        game = self.game
        game.screen.blit(self.background,(0,0))

        self.images.draw(game.screen)
        self.strings.draw(game.screen)
        self.buttons.draw(game.screen)




