import pygame

class Grid:
    def __init__(self, rows, cols, cell_size, color='White'):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.color = color

    """Generated Using AI"""
    def draw(self, surface):
        for c in range(self.cols + 1):
            x = c * self.cell_size
            pygame.draw.line(surface, self.color, (x, 0), (x, self.rows * self.cell_size))

        for r in range(self.rows + 1):
            y = r * self.cell_size
            pygame.draw.line(surface, self.color, (0, y), (self.cols * self.cell_size, y))

class Player:
    def __init__(self,grid:Grid,row:int,col: int):
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
        if keys[pygame.K_UP] and not self.prev_keys[pygame.K_UP] and self.row > 0:
            self.row -=1
        elif keys[pygame.K_s] and not self.prev_keys[pygame.K_s] and self.row < self.grid.rows - 1:
            self.row += 1
        elif keys[pygame.K_DOWN] and not self.prev_keys[pygame.K_DOWN] and self.row < self.grid.rows - 1:
            self.row += 1
        elif keys[pygame.K_a] and not self.prev_keys[pygame.K_a] and self.col > 0:
            self.col -= 1
        elif keys[pygame.K_LEFT] and not self.prev_keys[pygame.K_LEFT] and self.col > 0:
            self.col -= 1
        elif keys[pygame.K_d] and not self.prev_keys[pygame.K_d] and self.col < self.grid.cols - 1:
            self.col += 1
        elif keys[pygame.K_RIGHT] and not self.prev_keys[pygame.K_RIGHT] and self.col < self.grid.cols - 1:
            self.col += 1

        self.update_rect_from_grid()
        self.prev_keys = keys

    def update(self):
        self.listen()

    def render_on_surface(self, surface):
        surface.blit(self.modal, self.modalRect)
