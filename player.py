import pygame
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game


class Grid:
    def __init__(self, rows, cols, cell_size, color=(255, 255, 255)):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.color = color  # line color

    def draw(self, surface):
        # Draw vertical lines
        for c in range(self.cols + 1):
            x = c * self.cell_size
            pygame.draw.line(surface, self.color, (x, 0), (x, self.rows * self.cell_size))

        # Draw horizontal lines
        for r in range(self.rows + 1):
            y = r * self.cell_size
            pygame.draw.line(surface, self.color, (0, y), (self.cols * self.cell_size, y))


class Player:
    def __init__(self, game: "Game", grid: Grid, row: int, col: int, type='player'):
        self.game = game
        self.type = type
        self.grid = grid
        self.row = row
        self.col = col

        self.modal = pygame.image.load('assets/modal_down_trans.png').convert_alpha()
        self.modalRect = self.modal.get_rect()
        self.update_rect_from_grid()
        self.prev_keys = pygame.key.get_pressed()

    def update_rect_from_grid(self):
        cell = self.grid.cell_size
        x = self.col * cell + cell // 2
        y = self.row * cell + cell // 2
        self.modalRect.center = (x, y)

    def listen(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not self.prev_keys[pygame.K_w] and self.row > 0:
            self.row -= 1
        elif keys[pygame.K_s] and not self.prev_keys[pygame.K_s] and self.row < self.grid.rows - 1:
            self.row += 1
        elif keys[pygame.K_a] and not self.prev_keys[pygame.K_a] and self.col > 0:
            self.col -= 1
        elif keys[pygame.K_d] and not self.prev_keys[pygame.K_d] and self.col < self.grid.cols - 1:
            self.col += 1

        self.update_rect_from_grid()
        self.prev_keys = keys


    def update(self):
        pass

    def render(self):
        game = self.game
        game.screen.blit(self.modal, self.modalRect)
        self.grid.draw(game.screen)
