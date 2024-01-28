
### `main.py`

```markdown
# Pong Game - main.py

This is the main script for a simple Pong game implemented in Python using the Turtle graphics library.

## How to Run

Make sure you have Python installed. Execute the `main.py` file to start the game.

```bash
python main.py
```

## Dependencies

- Python
- Turtle graphics library

## Controls

- Player on the right:
  - Move up: Up arrow key
  - Move down: Down arrow key

- Player on the left:
  - Move up: W key
  - Move down: S key

## Gameplay

- The game starts with two paddles and a ball.
- Players control the paddles to hit the ball back and forth.
- If the ball passes a paddle, the opponent scores a point.
- The game continues until manually closed.

## Acknowledgments

This project is inspired by the classic Pong game.


### `paddle.py`

```markdown
# Pong Game - paddle.py

This module defines the `Paddle` class used in the Pong game.

## Paddle Class

### Methods

- `__init__(self, position)`: Initializes a paddle object at the specified position.
- `go_up(self)`: Moves the paddle upward.
- `go_down(self)`: Moves the paddle downward.

### Attributes

- `shape`: Square
- `color`: White
- `Size`: Stretch width = 5, stretch length = 1

## Usage

Create instances of the `Paddle` class in the main script (`main.py`) to represent the left and right paddles.

```

### `ball.py`

```markdown
# Pong Game - ball.py

This module defines the `Ball` class used in the Pong game.

## Ball Class

### Methods

- `__init__(self)`: Initializes a ball object with initial attributes.
- `move(self)`: Moves the ball.
- `bounce_y(self)`: Bounces the ball vertically.
- `bounce_x(self)`: Bounces the ball horizontally.
- `reset_position(self)`: Resets the ball's position and speed.

### Attributes

- `color`: White
- `shape`: Circle
- `Initial Speed`: x_move = 3, y_move = 3
- `Initial Move Speed`: 0.1

## Usage

Create an instance of the `Ball` class in the main script (`main.py`) to represent the game ball.

```
### `scoreboard.py`

```markdown
# Pong Game - scoreboard.py

This module defines the `Scoreboard` class used in the Pong game.

## Scoreboard Class

### Methods

- `__init__(self)`: Initializes a scoreboard object with initial attributes.
- `update_scoreboard(self)`: Clears and updates the scoreboard display.
- `l_point(self)`: Increments the left player's score.
- `r_point(self)`: Increments the right player's score.

### Attributes

- `color`: White
- `Font`: Courier, 80, normal
- `l_score`: Left player's score (initialized to 0)
- `r_score`: Right player's score (initialized to 0)

## Usage

Create an instance of the `Scoreboard` class in the main script (`main.py`) to keep track of scores.

```
# each line of code 

### `main.py`

```python
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
```

- **Imports**: Import necessary modules and classes from Turtle graphics library, including `Screen`, `Turtle`, `Paddle`, `Ball`, and `Scoreboard`.

```python
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
```

- **Screen Setup**: Initialize a Turtle screen with specific configurations, such as background color, dimensions, and title. `tracer(0)` turns off automatic screen updates.

```python
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
```

- **Object Initialization**: Create instances of `Paddle`, `Ball`, and `Scoreboard` classes.

```python
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
```

- **Key Event Listeners**: Set up key event listeners for paddle movement using the `listen()` method and `onkey()` method to bind keys to paddle methods.

```python
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # ... (collision detection and game logic)
```

- **Game Loop**: Start the main game loop. It continuously updates the screen, moves the ball, and checks for collisions and game events.

```python
screen.exitonclick()
```

- **Exit on Click**: Close the game window when clicked.

### `paddle.py`

```python
from turtle import Turtle
```

- **Import Turtle**: Import the `Turtle` class.

```python
class Paddle(Turtle):
```

- **Class Definition**: Define a new class `Paddle` that inherits from `Turtle`.

```python
def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.color("white")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.penup()
    self.goto(position)
```

- **Constructor**: Initialize a new paddle with specific attributes, including shape, color, size, and starting position.

```python
def go_up(self):
    new_y = self.ycor() + 20
    self.goto(self.xcor(), new_y)

def go_down(self):
    new_y = self.ycor() - 20
    self.goto(self.xcor(), new_y)
```

- **Movement Methods**: Define methods for moving the paddle up (`go_up`) and down (`go_down`).

### `ball.py`

```python
from turtle import Turtle
```

- **Import Turtle**: Import the `Turtle` class.

```python
class Ball(Turtle):
```

- **Class Definition**: Define a new class `Ball` that inherits from `Turtle`.

```python
def __init__(self):
    super().__init__()
    self.color("white")
    self.shape("circle")
    self.penup()
    self.x_move = 3
    self.y_move = 3
    self.move_speed = 0.1
```

- **Constructor**: Initialize a new ball with specific attributes, including color, shape, initial movements, and speed.

```python
def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)
```

- **Movement Method**: Define a method (`move`) for moving the ball.

```python
def bounce_y(self):
    self.y_move *= -1

def bounce_x(self):
    self.x_move *= -1
    self.move_speed *= 0.9
```

- **Bounce Methods**: Define methods (`bounce_y` and `bounce_x`) for bouncing the ball vertically and horizontally.

```python

def reset_position(self):
    self.goto(0, 0)
    self.move_speed = 0.1
    self.bounce_x()
```

- **Reset Position Method**: Define a method (`reset_position`) for resetting the ball's position and speed.

### `scoreboard.py`

```python
from turtle import Turtle
```

- **Import Turtle**: Import the `Turtle` class.

```python
class Scoreboard(Turtle):
```

- **Class Definition**: Define a new class `Scoreboard` that inherits from `Turtle`.

```python
def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update_scoreboard()
```

- **Constructor**: Initialize a new scoreboard with specific attributes, including color, hidden turtle, and initial scores.

```python
def update_scoreboard(self):
    self.clear()
    self.goto(-100, 200)
    self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
    self.goto(100, 200)
    self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
```

- **Update Scoreboard Method**: Define a method (`update_scoreboard`) for clearing and updating the scoreboard display.

```python
