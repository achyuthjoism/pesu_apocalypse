import pygame
from typing import TYPE_CHECKING
from helper import HEIGHT, WIDTH, Image
if TYPE_CHECKING:
    from game import Game
from helper import Text

class GameOver:
    def __init__(self,game:"Game",reason:str="You stood on a zombie too long!"):
        self.game = game
        self.txt = Text("Game Over",WIDTH//2,50,72,color='Red')
        self.reason = Text(reason,WIDTH//2,100,40,color='Red')
        self.restart = Text("Press r to restart",WIDTH//2,HEIGHT//2+10,40,color='White')
        self.home = Text("Press h to home",WIDTH//2,HEIGHT//2+60,40,color='White')
        self.quit = Text("Press q to quit",WIDTH//2,HEIGHT//2+110,40,color='White')
        self.images = pygame.sprite.Group()
        renu = Image('assets/renu_zombie.png',WIDTH//2,HEIGHT//2-20)
        self.images.add(renu)

    def update(self,reason=""):
        self.reason.update_text(reason)
        self.txt.update()
        self.reason.update()
        self.images.update()
        self.home.update()
        self.quit.update()
        self.restart.update()

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
        self.game.screen.fill('Black')
        self.game.screen.blit(self.txt.image,self.txt.rect)
        self.game.screen.blit(self.reason.image,self.reason.rect)
        self.game.screen.blit(self.restart.image,self.restart.rect)
        self.game.screen.blit(self.quit.image,self.quit.rect)
        self.game.screen.blit(self.home.image,self.home.rect)
        self.images.draw(self.game.screen)
