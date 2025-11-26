"""Audio and Distance Finding Algorithm was generated completly using AI"""
import pygame
import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Game
    from player import Grid

class Zombie:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.is_flagged = False
        self.is_revealed = False

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

    def spawn_zombies(self):
        positions = []
        for r in range(self.grid.rows):
            for c in range(self.grid.cols):
                if r != 0 or c != 0:
                    positions.append((r, c))

        random.shuffle(positions)
        for i in range(min(self.num_zombies, len(positions))):
            r, c = positions[i]
            self.zombies.append(Zombie(r, c))

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

        # Only play new audio if distance changed
        if distance == self.last_distance:
            return

        self.last_distance = distance

        # Stop current audio
        if self.current_audio_channel:
            self.current_audio_channel.stop()

        # Play appropriate audio
        if distance == 0:
            # Player is on zombie tile - handled separately
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

    def flag_tile(self, player_row: int, player_col: int):
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

    def render_flags(self, surface):
        """Draw flags on flagged tiles"""
        cell = self.grid.cell_size
        font = pygame.font.Font(None, 36)

        for zombie in self.zombies:
            if zombie.is_flagged:
                x = zombie.col * cell + cell // 2
                y = zombie.row * cell + cell // 2
                flag_text = font.render('F', True, 'Yellow')
                flag_rect = flag_text.get_rect(center=(x, y))
                surface.blit(flag_text, flag_rect)
