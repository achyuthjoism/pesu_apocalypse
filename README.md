# PESU Apocalypse - Escape the Zombies!

A zombie-themed grid-based puzzle game built with Pygame where players must identify and flag all zombies while avoiding humans.

## Game Overview

Navigate through a grid filled with characters and use audio cues to find hidden zombies. Flag all zombies without flagging any humans to win! Be careful not to stand on a zombie for too long, or it's game over.

## Features

- **Grid-based gameplay**: 10x24 grid with 50+ characters
- **Audio proximity system**: Sound cues indicate how close you are to zombies
- **Strategic flagging**: Mark zombies while avoiding innocent humans
- **Multiple screens**: Start menu, gameplay, victory, and game over screens
- **Visual feedback**: Character sprites and flagging indicators

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Clone or download this repository
2. Install Pygame:
```bash
pip install pygame
```

3. Ensure all required asset files are in the `assets/` directory:
   - `background.png` - Start screen background
   - `ByteBounce.ttf` - Game font
   - `modal_down_trans.png` - Player sprite
   - `modal1.png`, `modal2.png`, `modal3.png`, `modal4.png` - Character sprites
   - `audio_safe.wav` - Safe distance sound
   - `audio_close.wav` - Close proximity sound
   - `audio_danger.wav` - Danger sound
   - `audio_gameover.wav` - Game over sound

## How to Play

1. Run the game:
```bash
python main.py
```

2. **Controls:**
   - **WASD** or **Arrow Keys**: Move the player
   - **F**: Flag/unflag the current tile
   - **R**: Restart (on game over/victory screens)
   - **H**: Return to home screen
   - **Q**: Quit game

3. **Objective:**
   - Find and flag all 10 zombies hidden in the grid
   - Use audio cues to gauge proximity to zombies
   - Avoid flagging humans (game over!)
   - Don't stand on a zombie for too long (game over!)

4. **Audio Cues:**
   - Different sounds play based on your distance to the nearest zombie
   - Use these cues strategically to locate zombies

## Game States

- **Start Screen**: Main menu with start and exit options
- **Playing**: Active gameplay with grid navigation
- **Victory**: All zombies successfully flagged
- **Game Over**: Failed by flagging a human or standing on a zombie

## File Structure

```
.
├── main.py              # Entry point
├── game.py              # Main game loop and state management
├── helper.py            # Helper classes (Image, Text, Button)
├── player.py            # Player movement and grid system
├── zombie.py            # Zombie and NPC management
├── screens/
│   ├── start.py         # Start screen
│   ├── play_board.py    # Main gameplay screen
│   ├── game_over.py     # Game over screen
│   └── victory.py       # Victory screen
└── assets/              # Game assets (images, fonts, audio)
```

## Credits

- Audio and distance-finding algorithm generated using AI
- Grid drawing generated using AI

## Notes

- The game spawns 10 zombies randomly across the grid
- 50 NPCs (humans) are also randomly placed
- Player always starts at position (0, 0)
- Standing on a zombie for 37 frames (~0.6 seconds at 60 FPS) results in game over

## License

This is an educational project. Please ensure you have appropriate rights to any assets used.
