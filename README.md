# 🐍 Snake Game (Python Turtle)

This is a classic **Snake Game** implemented using Python's built-in `turtle` graphics module. The player controls the snake using arrow keys or `WASD`, eats food to grow longer, and tries to avoid hitting itself.

![snake-turtle-demo](https://img.shields.io/badge/Built%20With-Python%203.x-blue?style=flat&logo=python)

## 🎮 Gameplay Features

- Snake moves inside a resizable window
- Randomly colored food blocks
- Score tracking with a highest score counter
- Snake body increases with each food eaten
- Self-collision resets the game while retaining the high score

## 📦 Requirements

- Python 3.x (preferably 3.6 or newer)
- No external libraries required (uses only the `turtle`, `random`, and `time` modules)

## 🚀 How to Run

1. Clone or download this repository.
2. Run the `snake_game.py` file:

```bash
python snake_game.py
🎮 Controls
W or ↑ : Move Up

S or ↓ : Move Down

A or ← : Move Left

D or → : Move Right

Esc : Pause / Stop movement
📁 File Structure
bash
Copy
Edit
snake-game/
├── snake_game.py      # Main game script
├── README.md          # Game instructions & info
🧠 Game Logic Overview
The snake's head is a turtle that moves based on keyboard input.
📄 License
This project is open-source and free to use under the MIT License.



Every time it eats food:

The food changes to a random color and location.

A new body segment is added.

Score increases.

If the snake hits its own body, it resets (except the highest score).
