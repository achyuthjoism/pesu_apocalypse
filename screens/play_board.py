import pygame
from helper import *
from typing import TYPE_CHECKING
from player import Grid, Player
from zombie import ZombieManager
if TYPE_CHECKING:
    from game import Game

class PlayBoard:
    def __init__(self, game: "Game"):
        self.game = game
        self.txt = Text('PESU Apocalypse - Escape the Zombies!',WIDTH//2,75,60,color='Red')
        self.info_text = Text('Use WASD/Arrow Keys to move | F to flag',WIDTH//2,120,25,color='Black')
        self.strings = pygame.sprite.Group()
        self.strings.add(self.txt)
        self.strings.add(self.info_text)
        self.back_button = Button('Back',100,75,width=WIDTH//10,height=50)
        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.back_button)


        """Grid Offset(Need improvement)"""
        self.grid_offset_x = 50
        self.grid_offset_y = 180
        self.grid = Grid(10, 24, 50)
        self.modal = Player(grid=self.grid,row=0,col=0)

        self.zombie_manager = ZombieManager(game, self.grid, num_zombies=10)
        self.win_text = Text('YOU WIN! All zombies flagged!',WIDTH//2,HEIGHT//2,60,color='Green')
        self.stats_text = Text('',WIDTH//2,HEIGHT-30,25,color='Black')

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if hasattr(self, 'prev_keys'):
            if keys[pygame.K_f] and not self.prev_keys[pygame.K_f]:
                self.zombie_manager.flag_tile(self.modal.row, self.modal.col)
        self.prev_keys = keys

    def update(self):
        if not self.zombie_manager.game_over:
            self.handle_input()
            self.strings.update()
            self.buttons.update()
            self.modal.update()
            self.zombie_manager.update(self.modal.row, self.modal.col)

            flagged_count = sum(1 for z in self.zombie_manager.zombies if z.is_flagged)
            total_zombies = len(self.zombie_manager.zombies)
            distance = self.zombie_manager.get_nearest_zombie_distance(self.modal.row, self.modal.col)
            stats_str = f'Flagged: {flagged_count}/{total_zombies} | Nearest Zombie: {distance} tiles away'
            self.stats_text.update_text(stats_str)

            if self.zombie_manager.check_win_condition():
                self.game.state = 'victory'
                self.game.render()
        else:
            self.game.state = 'game_over'
            self.game.render()

    def render(self):
        game = self.game
        game.screen.fill('White')

        if not self.zombie_manager.game_over:
            self.strings.draw(game.screen)
            self.buttons.draw(game.screen)
            grid_surface = pygame.Surface((self.grid.cols*self.grid.cell_size,self.grid.rows*self.grid.cell_size))
            grid_surface.fill('Black')
            self.zombie_manager.spawn_npcs(grid_surface)
            self.zombie_manager.render_zombies(grid_surface)
            self.modal.render_on_surface(grid_surface)
            self.grid.draw(grid_surface)
            game.screen.blit(grid_surface, (self.grid_offset_x, self.grid_offset_y))
            game.screen.blit(self.stats_text.image, self.stats_text.rect)
        else:
            game.state = 'game_over'
            game.render()
            self.buttons.draw(game.screen)
