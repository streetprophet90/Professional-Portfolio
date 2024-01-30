
# Pomodoro Timer

A simple Pomodoro timer application with a graphical user interface built using Python's Tkinter library.

## Features
- Work sessions of 25 minutes followed by a 5-minute short break.
- Every fourth break is a longer break of 20 minutes.
- Tracks the number of work sessions completed and displays checkmarks for each completed session.
- Start and reset buttons to control the timer.


## How to Use
1. Run the script.
2. Click the "Start" button to begin the Pomodoro timer.
3. Click the "Reset" button to stop the timer and reset the session count.

## Timer States
- **Work Session:** 25 minutes (Green color)
- **Short Break:** 5 minutes (Pink color)
- **Long Break:** 20 minutes (Red color)

## Dependencies
- Python 3.x
- Tkinter library

## Preview
![Pomodoro Timer](Tomato.jpg)

## Acknowledgments
- Tomato image by [Pexels](https://www.pexels.com/photo/red-tomato-fruit-on-brown-tree-wooden-branch-190615/)




# Every Line of Code

```python
from tkinter import *
import math
```
- These lines import the necessary modules: `tkinter` for creating the GUI and `math` for mathematical operations.

```python
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
```
- These lines define color constants in hexadecimal format for use in the UI.

```python
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
```
- These lines set constants for font name, work, short break, and long break durations. `reps` and `timer` are initialized as global variables.

```python
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
```
- This function (`reset_timer`) resets the timer, cancels any ongoing timer events, and resets session-related UI elements.

