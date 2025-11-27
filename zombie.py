"""Audio and Distance Finding Algorithm was generated completly using AI"""
import pygame
import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game
    from player import Grid

npcs = ['assets/modal1.png','assets/modal2.png','assets/modal3.png','assets/modal4.png']

class NPC:
    def __init__(self,grid,row:int,col:int,image='assets/modal1.png'):
        self.row = row
        self.col = col
        self.grid = grid
        self.is_flagged = False
        cell = self.grid.cell_size
        x = self.col * cell + cell // 2
        y = self.row * cell + cell // 2
        self.modal = pygame.image.load(image).convert_alpha()
        self.modalRect = self.modal.get_rect(center=(x,y))

    def render(self,surface):
        surface.blit(self.modal, self.modalRect)

class Zombie:
    def __init__(self, grid, row: int, col: int, image='assets/modal1.png'):
        self.row = row
        self.col = col
        self.grid = grid
        self.is_flagged = False
        cell = self.grid.cell_size
        x = self.col * cell + cell // 2
        y = self.row * cell + cell // 2
        self.modal = pygame.image.load(image).convert_alpha()
        self.modalRect = self.modal.get_rect(center=(x, y))

    def render(self, surface):
        if self.is_flagged:
            cell = self.grid.cell_size
            x = self.col * cell + cell // 2
            y = self.row * cell + cell // 2
            font = pygame.font.Font('assets/ByteBounce.ttf', 36)
            flag_text = font.render('F', True, 'Yellow')
            flag_rect = flag_text.get_rect(center=(x, y))
            surface.blit(flag_text, flag_rect)
        else:
            surface.blit(self.modal, self.modalRect)

class ZombieManager:
    def __init__(self, game: "Game", grid: "Grid", num_zombies):
        self.game = game
        self.grid = grid
        self.zombies = []
        self.num_zombies = num_zombies
        self.game_over = False
        self.game_over_reason = ""
        self.inspection_timer = 0
        self.inspection_delay = 37
        self.is_inspecting = False
        self.inspecting_position = None
        self.npc_objects = []

        # Audio setup (placeholder files)
        pygame.mixer.init()
        try:
            self.audio_safe = pygame.mixer.Sound('assets/audio_safe.wav')
            self.audio_close = pygame.mixer.Sound('assets/audio_close.wav')
            self.audio_danger = pygame.mixer.Sound('assets/audio_danger.wav')
            self.audio_game_over = pygame.mixer.Sound('assets/audio_gameover.wav')
        except:
            print("Warning: Audio files not found. Create placeholder audio files:")
            print("  - assets/audio_safe.wav (distance > 2)")
            print("  - assets/audio_close.wav (distance 2)")
            print("  - assets/audio_danger.wav (distance 1)")
            print("  - assets/audio_gameover.wav (game over sound)")
            self.audio_safe = None
            self.audio_close = None
            self.audio_danger = None
            self.audio_game_over = None

        self.current_audio_channel = None
        self.last_distance = -1

        self.spawn_zombies()
        self.gen_npc()


    def spawn_zombies(self):
        positions = []
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                if r != 0 or c != 0:
                    positions.append((r, c))

        random.shuffle(positions)
        for i in range(min(self.num_zombies, len(positions))):
            r, c = positions[i]
            zombie = Zombie(self.grid, r, c, image=random.choice(npcs))
            self.zombies.append(zombie)

    def gen_npc(self):
        all_positions = set()
        zombie_positions = set()
        for zombie in self.zombies:
            zombie_positions.add((zombie.row, zombie.col))

        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                all_positions.add((r, c))

        npc_positions = random.sample(list(all_positions - zombie_positions), 50)

        self.npc_objects = []
        for row, col in npc_positions:
            npc = NPC(self.grid, row, col, image=random.choice(npcs))
            self.npc_objects.append(npc)

    def spawn_npcs(self, surface):
        for npc in self.npc_objects:
            npc.render(surface)

    def get_zombie_at(self, row: int, col: int):
        for zombie in self.zombies:
            if zombie.row == row and zombie.col == col:
                return zombie
        return False

    def get_nearest_zombie_distance(self, player_row: int, player_col: int):
        """Calculate Manhattan distance to nearest zombie"""
        if not self.zombies:
            return float('inf')

        min_distance = float('inf')
        for zombie in self.zombies:
            distance = abs(zombie.row - player_row) + abs(zombie.col - player_col)
            min_distance = min(min_distance, distance)

        return min_distance

    def play_proximity_audio(self, player_row: int, player_col: int):
        """Play audio based on distance to nearest zombie"""
        distance = self.get_nearest_zombie_distance(player_row, player_col)

        if distance == self.last_distance:
            return

        self.last_distance = distance

        if self.current_audio_channel:
            self.current_audio_channel.stop()

        if distance == 0:
            pass
        elif distance == 1:
            if self.audio_danger:
                self.current_audio_channel = self.audio_danger.play()
        elif distance == 2:
            if self.audio_close:
                self.current_audio_channel = self.audio_close.play()
        else:
            if self.audio_safe:
                self.current_audio_channel = self.audio_safe.play()

    def get_npc_at(self, row: int, col: int):
        for npc in self.npc_objects:
            if npc.row == row and npc.col == col:
                return npc
        return None

    def flag_tile(self, player_row: int, player_col: int):
        npc = self.get_npc_at(player_row, player_col)
        if npc:
            self.game_over = True
            self.game.game_over_reason = 'You Flagged A Human!!'
            if self.audio_game_over:
                self.audio_game_over.play()
            return

        zombie = self.get_zombie_at(player_row, player_col)
        if zombie:
            zombie.is_flagged = not zombie.is_flagged

    def check_game_over(self, player_row: int, player_col: int):
        zombie = self.get_zombie_at(player_row, player_col)

        if zombie:
            self.is_inspecting = True
            self.inspecting_position = (player_row, player_col)
            self.inspection_timer += 1

            if self.inspection_timer >= self.inspection_delay:
                self.game_over = True
                self.game.game_over_reason = "You stood on a zombie too long!"
                if self.audio_game_over:
                    self.audio_game_over.play()
                return True

        else:
            self.is_inspecting = False
            self.inspection_timer = 0
            self.inspecting_position = None

        return False

    def check_win_condition(self):
        for zombie in self.zombies:
            if not zombie.is_flagged:
                return False
        return True

    def update(self, player_row: int, player_col: int):
        if self.game_over:
            return

        self.play_proximity_audio(player_row, player_col)
        self.check_game_over(player_row, player_col)


    def render_zombies(self, surface):
        for zombie in self.zombies:
            zombie.render(surface)
