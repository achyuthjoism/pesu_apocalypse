import pygame
from typing import TYPE_CHECKING
from helper import HEIGHT, WIDTH, Image
if TYPE_CHECKING:
    from game import Game
from helper import Text

class Victory:
    def __init__(self,game:"Game"):
        self.game = game
        self.txt = Text("Victory",WIDTH//2,50,72,color='Green')
        self.restart = Text("Press r to restart",WIDTH//2,HEIGHT//2,40,color='Black')
        self.home = Text("Press h to home",WIDTH//2,HEIGHT//2+50,40,color='Black')
        self.quit = Text("Press q to quit",WIDTH//2,HEIGHT//2+100,40,color='Black')
        self.images = pygame.sprite.Group()
        dboos = Image('assets/dboos.jpg',WIDTH//2,HEIGHT//2-50)
        self.images.add(dboos)

    def update(self):
        self.txt.update()
        self.home.update()
        self.quit.update()
        self.restart.update()
        self.images.update()

    def get_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.game.state = 'playing'
            self.game.render()
        elif keys[pygame.K_h]:
            self.game.state = 'start'
            self.game.render()
        elif keys[pygame.K_q]:
            self.game.running = False

    def render(self):
        self.game.screen.fill('White')
        self.game.screen.blit(self.txt.image,self.txt.rect)
        self.game.screen.blit(self.restart.image,self.restart.rect)
        self.game.screen.blit(self.quit.image,self.quit.rect)
        self.game.screen.blit(self.home.image,self.home.rect)
        self.images.draw(self.game.screen)

