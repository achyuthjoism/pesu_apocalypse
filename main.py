import pygame
from constants import *
from helper import *

pygame.init()

if __name__ == '__main__':
    display = pygame.display
    maindisplay = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()
    background = pygame.image.load('background.png').convert()
    txt = Text('PESU Apocalypse',WIDTH//2,100,100,color='Red')
    player = pygame.sprite.Group()
    player.add(Image('dboos.jpg',150,300))
    player.add(Image('renu.jpg',WIDTH-150,300))
    strings = pygame.sprite.Group()
    strings.add(txt)
    start_button = Button('Start',WIDTH//2,300)
    exit_button = Button('Exit',WIDTH//2,400)
    buttons = pygame.sprite.Group()
    buttons.add(start_button)
    buttons.add(exit_button)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT or exit_button.is_clicked(event):
                pygame.quit()
                exit()

            if start_button.is_clicked(event):
                pass

        maindisplay.blit(background,(0,0))

        player.draw(maindisplay)
        player.update()

        strings.draw(maindisplay)
        strings.update()

        buttons.draw(maindisplay)
        buttons.update()

        display.update()
        clock.tick(60)
