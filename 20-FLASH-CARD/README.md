# Flashy

Flashy is a simple vocabulary flashcard application built using Python's Tkinter library. It helps users learn and memorize new words in a foreign language.

## Features

- **Flashcard Learning**: Flip through flashcards to see the translation of words from one language to another.
- **Randomized Cards**: Cards are presented in a random order for effective learning.
- **User Progress**: Track your progress by marking words you have learned.

## How to Use

1. **Installation**:
   - Make sure you have Python installed on your machine.
   - Clone or download this repository.

2. **Dependencies**:
   - Install the required dependencies by running `pip install pandas` in your terminal.

3. **Run the Application**:
   - Execute the script by running `python flashcards.py` in your terminal.

4. **Learning**:
   - Press the "Next" button to see a new flashcard.
   - Click the checkmark if you know the word, or the "X" if you don't.

5. **Progress**:
   - Your progress is tracked, and words you've learned are saved for future reference.

## Screenshots

![Flashy Screenshot](images/screenshot.png)



## Credits

- This application uses word data from the [French Words Dataset](data/french_words.csv).
- Flashcard images: [SVGRepo](https://www.svgrepo.com/)



### Block 1: Importing Libraries and Setting Constants

```python
# Import required libraries
from tkinter import *
import pandas
import random

# Set background color
BACKGROUND_COLOR = "#B1DDC6"

# Initialize variables for current card and words to learn
current_card = {}
to_learn = {}
```

Explanation:
- Import necessary libraries, including Tkinter for GUI, pandas for data handling, and random for random selection.
- Set a constant for the background color and initialize variables for the current flashcard and words to learn.

### Block 2: Loading Data

```python
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
```

Explanation:
- Attempt to read existing data from a CSV file (`words_to_learn.csv`).
- If the file is not found, load the original French words dataset (`french_words.csv`) and convert it to a dictionary.
- If the file is found, convert the data to a dictionary.

### Block 3: Flashcard Functions
```python
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()
```

Explanation:
- `next_card()`: Displays the next flashcard on the canvas, cancels any existing flip timer, and starts a new timer for automatic flipping after 3 seconds.
- `flip_card()`: Flips the flashcard to reveal the English translation.
- `is_known()`: Removes the current card from the to-learn list, saves the updated list to a CSV file, and shows the next flashcard.

### Block 4: Tkinter GUI Setup
```python
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
# ... (code for loading images and creating canvas items)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0,  command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
```







This application allows users to learn French words interactively through a Tkinter-based flashcard interface. Users can mark words as known or unknown, automatically progress through flashcards, and visualize translations. Images for the front and back of the flashcards are loaded from files, and the flashcard data is managed using pandas.