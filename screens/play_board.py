import pygame
from helper import *
from typing import TYPE_CHECKING

from player import Grid, Player
if TYPE_CHECKING:
    from game import Game

class PlayBoard:
    def __init__(self,game:"Game"):
        self.game = game
        self.txt = Text('PlayBoard',WIDTH//2,75,100,color='Red')
        self.strings = pygame.sprite.Group()
        self.strings.add(self.txt)
        self.back_button = Button('Back',100,75,width=WIDTH//10,height=50)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.back_button)
        self.grid = Grid(7,7,50)
        self.modal = Player(game=game,grid=self.grid,row=0,col=0)

    def update(self):
        self.strings.update()
        self.buttons.update()
        self.modal.update()

    def render(self):
        game = self.game

        game.screen.fill('Black')
        self.strings.draw(game.screen)
        self.buttons.draw(game.screen)
        self.modal.render()




