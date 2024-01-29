

### `main.py`


# The Street Game

This Python script implements a simple Snake game using the Turtle graphics library. The player controls a snake that moves around the screen, consumes food to grow, and must avoid collisions with walls and itself.

## How to Play
- Use the arrow keys (Up, Down, Left, Right) to control the snake's direction.
- Consume blue food to increase the score.
- Avoid collisions with the walls and the snake's own tail.

## Dependencies
- Python 3.x
- Turtle graphics library

## Usage
Run the script, and the game window will appear. Use the arrow keys to control the snake. Have fun playing!


### `scoreboard.py`


# The Street Game - Scoreboard

This module defines the `Scoreboard` class, responsible for displaying and updating the player's score in the Snake game.

## Usage
Create an instance of the `Scoreboard` class and use its methods to update the score during the game.

```python
scoreboard = Scoreboard()
scoreboard.increase_score()
```

## Dependencies
```markdown
- Python 3.x
- Turtle graphics library

```

### `snake.py`


# The Street Game - Snake

This module defines the `Snake` class, which represents the snake in the Snake game.

## Features
- The snake can move in four directions: Up, Down, Left, and Right.
- The snake can grow in length by consuming food.

## Usage
Create an instance of the `Snake` class to control the snake's behavior during the game.

```python
snake = Snake()
snake.up()
snake.move()
```

## Dependencies
- Python 3.x
- Turtle graphics library



### `food.py`


# The Street Game - Food

This module defines the `Food` class, representing the food that the snake consumes to grow in the Snake game.

## Features
- The food appears at random positions on the screen.

## Usage
Create an instance of the `Food` class to manage the appearance of food during the game.

```python
food = Food()
food.refresh()
```

## Dependencies
- Python 3.x
- Turtle graphics library

```

Feel free to customize these README files based on your preferences and any additional information you want to provide.

