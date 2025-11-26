# PESU Apocalypse 🧟

Can you escape the apocalypse? Navigate a zombie-infested grid and flag all the undead before it's too late!

## 🎮 Game Overview

PESU Apocalypse is a grid-based survival game where you must locate and flag all hidden zombies while avoiding standing on them for too long. Use audio cues and distance indicators to hunt down the zombies before they get you!

## ✨ Features

- **Grid-based Movement**: Navigate a 10x24 grid using WASD or arrow keys
- **Proximity Audio System**: Audio cues change based on your distance to the nearest zombie
  - Safe sound: Distance > 2 tiles
  - Close sound: Distance = 2 tiles  
  - Danger sound: Distance = 1 tile
- **Flag System**: Mark suspected zombie locations with flags (press F)
- **Distance Tracking**: Real-time display of distance to nearest zombie
- **Game Over Mechanic**: Standing on a zombie tile for too long triggers game over
- **Victory Condition**: Flag all zombies to win!

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Pygame library

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd pesu-apocalypse
```

2. Install dependencies:
```bash
pip install pygame
```

3. Run the game:
```bash
python main.py
```

## 🎯 How to Play

1. **Start the Game**: Click the "Start" button on the main menu
2. **Movement**: Use WASD or Arrow Keys to move your character across the grid
3. **Flag Zombies**: Press F to place/remove a flag on your current tile
4. **Listen Carefully**: Audio cues indicate proximity to zombies
5. **Check Distance**: The bottom of the screen shows the distance to the nearest zombie
6. **Win Condition**: Flag all 10 zombies to achieve victory
7. **Avoid Game Over**: Don't stand on a zombie tile for too long!

### Controls

- **WASD / Arrow Keys**: Move player
- **F**: Flag/unflag current tile
- **R**: Restart game (on game over/victory screen)
- **H**: Return to home screen
- **Q**: Quit game

## 📁 Project Structure

```
pesu-apocalypse/
├── main.py              # Entry point
├── game.py              # Main game loop and state management
├── helper.py            # Helper classes (Image, Text, Button)
├── player.py            # Player and Grid classes
├── zombie.py            # Zombie and ZombieManager classes
├── screens/
│   ├── start.py         # Start screen
│   ├── play_board.py    # Main gameplay screen
│   ├── game_over.py     # Game over screen
│   └── victory.py       # Victory screen
├── assets/              # Game assets (images, audio, fonts)
└── README.md
```

## 🔊 Audio Files

The game requires the following audio files in the `assets/` directory:

- `audio_safe.wav` - Plays when zombies are far away (distance > 2)
- `audio_close.wav` - Plays when zombies are moderately close (distance = 2)
- `audio_danger.wav` - Plays when zombies are very close (distance = 1)
- `audio_gameover.wav` - Plays when game over is triggered

**Note**: The game will still run without audio files but you'll see a warning message.

## 🎨 Required Assets

Place these files in the `assets/` directory:

- `background.png` - Start screen background
- `modal_down_trans.png` - Player sprite
- `dboos.jpg` - Game hero image
- `renu.jpg` - Game villain image
- `renu_zombie.png` - Zombie character image
- `ByteBounce.ttf` - Game font
- Audio files (see above)

## 🎓 Game Mechanics

### Zombie Detection

- **10 zombies** are randomly placed on the grid (never on the starting position)
- Zombies remain hidden until flagged
- Distance is calculated using Manhattan distance (|row1 - row2| + |col1 - col2|)

### Inspection Timer

- Standing on a zombie tile for **37 frames** (~0.6 seconds at 60 FPS) triggers game over
- Move away from the tile to reset the timer

### Win Condition

- Successfully flag all 10 zombie locations to win
- Flags can be placed and removed freely

## 🛠️ Technical Details

- **Resolution**: 1280x720
- **Frame Rate**: 60 FPS
- **Grid Size**: 10 rows × 24 columns
- **Cell Size**: 50 pixels
- **Engine**: Pygame

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests

## 📝 Credits

- Audio and distance-finding algorithm generated using AI
- Grid drawing function generated using AI

## 📄 License

This project is open source and available for educational purposes.

---

**Good luck surviving the PESU Apocalypse!** 🧟‍♂️💀
