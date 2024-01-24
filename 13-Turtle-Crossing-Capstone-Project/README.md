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



### `main.py`
1. `import` statements:
   - `time`: Module providing various time-related functions.
   - `Screen`: Class from the Turtle module for creating a graphical window.
   - `Player`, `CarManager`, `Scoreboard`: Custom classes defined in other files.

2. `Screen` setup:
   - Creates a Turtle graphics window with a width and height of 600 pixels.
   - `screen.tracer(0)`: Turns off automatic screen updates to speed up animation.

3. Object creation:
   - `player`: An instance of the `Player` class.
   - `car_manager`: An instance of the `CarManager` class.
   - `scoreboard`: An instance of the `Scoreboard` class.

4. Event handling:
   - `screen.listen()`: Listens for events.
   - `screen.onkey(player.go_up, "Up")`: Calls `player.go_up` when the "Up" key is pressed.

5. Game loop (`while` loop):
   - `time.sleep(0.1)`: Pauses for 0.1 seconds to control the game's speed.
   - `screen.update()`: Updates the screen manually.

6. Car management:
   - `car_manager.create_car()`: Creates a new car based on random chance.
   - `car_manager.move_cars()`: Moves all cars.

7. Collision detection:
   - Checks if the player collides with any cars. If true, ends the game and displays the game over message.

8. Successful crossing:
   - Checks if the player has crossed the finish line. If true, resets the player, levels up the car speed, and updates the scoreboard.

9. `screen.exitonclick()`: Closes the window when clicked.

### `player.py`
1. `Player` class:
   - Inherits from `Turtle`.
   - Constants: `STARTING_POSITION`, `MOVE_DISTANCE`, `FINISH_LINE_Y`.
   - Methods: `__init__`, `go_up`, `go_to_start`, `is_at_finish_line`.

### `car_manager.py`
1. `CarManager` class:
   - Manages the creation, movement, and leveling up of cars.
   - Constants: `COLORS`, `STARTING_MOVE_DISTANCE`, `MOVE_INCREMENT`.
   - Methods: `__init__`, `create_car`, `move_cars`, `level_up`.

### `scoreboard.py`
1. `Scoreboard` class:
   - Inherits from `Turtle`.
   - Constant: `FONT`.
   - Methods: `__init__`, `update_scoreboard`, `increase_level`, `game_over`.


## mMin logic of the Turtle game

### `main.py`

```python
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
```

- **Imports:**
  - `time`: Module providing various time-related functions.
  - `Screen`: Class from the Turtle module for creating a graphical window.
  - `Player`, `CarManager`, `Scoreboard`: Custom classes defined in other files.

```python
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
```

- **Screen setup:**
  - Creates a Turtle graphics window with a width and height of 600 pixels.
  - `screen.tracer(0)`: Turns off automatic screen updates to speed up animation.

```python
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
```

- **Object creation:**
  - `player`: An instance of the `Player` class.
  - `car_manager`: An instance of the `CarManager` class.
  - `scoreboard`: An instance of the `Scoreboard` class.



