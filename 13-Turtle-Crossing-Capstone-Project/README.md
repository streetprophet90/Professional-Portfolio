# Turtle Crossing Game

## Overview
This Python program implements a simple turtle crossing game using the Turtle graphics library. The player (turtle) moves upwards to cross a busy road while avoiding cars. The game becomes progressively challenging as the player successfully crosses the road.

## Files
### `main.py`
- Initializes the game window, player, car manager, and scoreboard.
- Listens for the "Up" arrow key to move the player.
- Manages the game loop, updating the screen, creating and moving cars, and handling collisions and successful crossings.

### `player.py`
- Defines the `Player` class, which represents the player's turtle.
- Handles the turtle's appearance, movement, and position.
- Provides a method to check if the turtle has reached the finish line.

### `car_manager.py`
- Defines the `CarManager` class, responsible for managing cars in the game.
- Handles the creation, movement, and level-up logic for cars.

### `scoreboard.py`
- Defines the `Scoreboard` class, displaying the current level and handling level increases and game over scenarios.

## How to Play
1. Run `main.py`.
2. Use the "Up" arrow key to move the turtle upwards.
3. Avoid colliding with cars while crossing the road.
4. Successfully crossing the road increases the level, making the game more challenging.
5. If the turtle collides with a car, the game ends, and "GAME OVER" is displayed.

## Dependencies
- Python 3
- Turtle graphics library

## Attribution
The project is inspired by the Turtle Crossing game from the Python course on [Replit](https://replit.com/@appbrewery/day-23-4). The code structure and logic are adapted and extended for educational purposes.