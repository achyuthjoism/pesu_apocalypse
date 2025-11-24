import pygame
from constants import *
import math

class Image(pygame.sprite.Sprite):
    def __init__(self,image:str,x,y):
        super().__init__()
        self.image = pygame.image.load(image).convert()
        self.name = image[:image.find('.')]
        self.rect = self.image.get_rect(midbottom=(x,y))
        self.j = 0
        self.y = y

    def animate(self):
        self.j += 0.1
        self.rect.bottom = self.y + math.sin(self.j)*7

    def update(self):
        self.animate()

class Text(pygame.sprite.Sprite):
    def __init__(self, txt, x:int, y:int, size, color='Black', font_path='assets/ByteBounce.ttf', align='center'):
        super().__init__()
        self.txt = txt
        self.color = color
        self.align = align
        self.pos = (x, y)

        try:
            self.font = pygame.font.Font(font_path, size)
        except (FileNotFoundError, OSError):
            print(f"ERROR: Font file '{font_path}' not found. Using default.")
            self.font = pygame.font.SysFont('Arial', size)

        self.image = self.font.render(self.txt, True, self.color)
        self.rect = self.image.get_rect()

        self.set_position()

    def set_position(self):
        x, y = self.pos
        if self.align == 'center':
            self.rect.center = (x, y)
        elif self.align == 'topleft':
            self.rect.topleft = (x, y)
        elif self.align == 'topright':
            self.rect.topright = (x, y)
        elif self.align == 'bottom':
            self.rect.midbottom = (x, y)
        elif self.align == 'bottomleft':
            self.rect.bottomleft = (x, y)
        elif self.align == 'bottomright':
            self.rect.bottomright = (x, y)
        else:
            self.rect.center = (x, y)

    def update_text(self, new_text):
        if new_text != self.txt:
            self.txt = new_text
            self.image = self.font.render(self.txt, True, self.color)
            self.rect = self.image.get_rect()
            self.set_position()

    def update(self):
        pass

class Button(pygame.sprite.Sprite):
    def __init__(self, txt:str, x, y, width=WIDTH//3, height=75):
        super().__init__()

        self.width = width
        self.height = height

        self.color_normal = (89,3,3) # Dark Red
        self.color_hover = (100, 100, 100) # Lighter Grey
        self.text_color = (255, 255, 255)  # White

        self.font = pygame.font.Font("assets/ByteBounce.ttf", 30)
        self.txt = txt

        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.draw_button(self.color_normal)

    def draw_button(self, bg_color):
        """Draws the background and puts the text in the middle"""
        self.image.fill(bg_color)

        text_surf = self.font.render(self.txt, True, self.text_color)

        text_rect = text_surf.get_rect(center=self.image.get_rect().center)

        self.image.blit(text_surf, text_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.draw_button(self.color_hover)
        else:
            self.draw_button(self.color_normal)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    return True
        return False
