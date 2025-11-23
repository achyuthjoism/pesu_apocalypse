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
        self.pos = (x, y) # Store position for updates later

        # FIX 1: Use pygame.font.Font for file paths.
        # We add a try/except block so the game doesn't crash if the file is missing.
        try:
            self.font = pygame.font.Font(font_path, size)
        except (FileNotFoundError, OSError):
            print(f"ERROR: Font file '{font_path}' not found. Using default.")
            self.font = pygame.font.SysFont('Arial', size)

        self.image = self.font.render(self.txt, True, self.color)
        self.rect = self.image.get_rect()

        # call the helper function to set position
        self.set_position()

    def set_position(self):
        # FIX 2: Correcting rect attributes (using tuple-accepting anchors)
        x, y = self.pos
        if self.align == 'center':
            self.rect.center = (x, y)
        elif self.align == 'topleft':
            self.rect.topleft = (x, y)
        elif self.align == 'topright':
            self.rect.topright = (x, y)
        elif self.align == 'bottom':
            self.rect.midbottom = (x, y) # 'bottom' usually implies middle-bottom
        elif self.align == 'bottomleft':
            self.rect.bottomleft = (x, y)
        elif self.align == 'bottomright':
            self.rect.bottomright = (x, y)
        else:
            self.rect.center = (x, y) # Default fallback

    def update_text(self, new_text):
        # Use this to update scores/timers
        if new_text != self.txt:
            self.txt = new_text
            self.image = self.font.render(self.txt, True, self.color)
            # We must re-calculate the rect because the text size changed!
            old_rect = self.rect
            self.rect = self.image.get_rect()
            # Re-apply alignment so it expands in the correct direction
            self.set_position()

    def update(self):
        pass

class Button(pygame.sprite.Sprite):
    def __init__(self, txt:str, x, y, width=WIDTH//3, height=75):
        super().__init__()

        # 1. Setup Dimensions and Colors
        self.width = width
        self.height = height

        self.color_normal = (89,3,3)
        self.color_hover = (100, 100, 100) # Lighter Grey
        self.text_color = (255, 255, 255)  # White

        # 2. Setup Font
        # Using SysFont for simplicity, but you can switch to Font(path) like before
        self.font = pygame.font.Font("assets/ByteBounce.ttf", 30)
        self.txt = txt

        # 3. Create the Surface (The canvas for the button)
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # 4. Initial Draw
        self.draw_button(self.color_normal)

    def draw_button(self, bg_color):
        """Draws the background and puts the text in the middle"""
        # A. Fill the background
        self.image.fill(bg_color)

        # B. Render the text
        text_surf = self.font.render(self.txt, True, self.text_color)

        # C. Center the text on the button surface
        # We align the text_rect center to the image_rect center
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)

        # D. Blit (draw) the text onto the button image
        self.image.blit(text_surf, text_rect)

    def update(self):
        """Checks if mouse is hovering and changes color"""
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is inside the button rect
        if self.rect.collidepoint(mouse_pos):
            self.draw_button(self.color_hover)
        else:
            self.draw_button(self.color_normal)

    def is_clicked(self, event):
        """Helper to call in the event loop"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left click
                if self.rect.collidepoint(event.pos):
                    return True
        return False
