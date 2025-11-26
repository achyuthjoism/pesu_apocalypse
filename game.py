import pygame
from helper import *
from screens.game_over import GameOver
from screens.start import *
from screens.play_board import *
from screens.victory import Victory

class Game:
    def __init__(self):
        pygame.init()
        self.height = 720
        self.width = 1280
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.display = pygame.display
        self.state = 'start'
        self.clock = pygame.time.Clock()
        self.running = True
        self.start_screen = Start(self)
        self.playing_screen = PlayBoard(self)
        self.game_over_screen = GameOver(self)
        self.victory_screen = Victory(self)

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not self.running or self.start_screen.exit_button.is_clicked(event):
                pygame.quit()
                exit()

            if self.start_screen.start_button.is_clicked(event):
                self.state = 'playing'
                self.render()

            if self.playing_screen.back_button.is_clicked(event):
                self.state = 'start'
                self.render()

            if self.state == 'playing':
                self.playing_screen.modal.listen()

            if self.state == 'game_over':
                self.game_over_screen.get_events()

            if self.state == 'victory':
                self.victory_screen.get_events()

    def render(self):
        if self.state == 'start':
            self.start_screen.update()
            self.start_screen.render()
        elif self.state == 'playing':
            self.playing_screen.update()
            self.playing_screen.render()
        elif self.state == 'game_over':
            self.playing_screen = PlayBoard(self)
            self.game_over_screen.update()
            self.game_over_screen.render()
        elif self.state == 'victory':
            self.playing_screen = PlayBoard(self)
            self.victory_screen.update()
            self.victory_screen.render()

        self.display.update()
        self.clock.tick(60)
