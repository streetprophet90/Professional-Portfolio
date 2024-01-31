
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

```python
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
```
- This function (`start_timer`) handles the logic for starting the timer based on the session count (`reps`). It determines the session type (work, short break, long break) and updates the UI accordingly.

```python
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
```
- This function (`count_down`) implements the countdown mechanism. It updates the timer display, continues counting down, and triggers the start of a new session or break when the countdown reaches zero.

```python
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
```
- These lines create the main Tkinter window, set its title, and configure its padding and background color.

```python
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)
```
- This line creates a label (`title_label`) for displaying the timer or break, configures its text, color, font, and position within the grid.

```python
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Tomato.jpg")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
```
- These lines create a canvas (`canvas`) for displaying the timer image, timer text, and the tomato image. The canvas is positioned within the grid layout.

```python
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
```
- This line creates a button (`start_button`) with the label "Start". It's configured with no border (`highlightthickness=0`) and linked to the `start_timer` function.

```python
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)
```
- This line creates a button (`reset_button`) with the label "Reset". It's configured with no border (`highlightthickness=0`) and linked to the `reset_timer` function.

```python
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)
```
- This line creates a label (`check_marks`) for displaying checkmarks. It's positioned within the grid and configured with the color.

```python
window.mainloop()
```
- This line starts the Tkinter main loop, allowing the GUI to run and respond to user actions.
