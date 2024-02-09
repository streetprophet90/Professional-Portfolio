


# Flashy

Flashy is a simple flashcard application built using Python's Tkinter library. The application helps users learn new words or phrases by presenting them with flashcards and allowing them to flip between the front and back sides.

## Features

1. **Flashcard Presentation:** Flashy presents users with flashcards displaying words or phrases in one language on the front side and their corresponding translations in another language on the back side.

2. **Flip Functionality:** Users can flip the flashcards to reveal the translations on the back side by clicking on them.

3. **Learning Mode:** Flashy keeps track of the words or phrases that users are learning and removes them from the list once they are known.

## How to Use

1. **Next Card:**
   - Click the "Next Card" button to display a new flashcard with a word or phrase in one language on the front side.

2. **Flip Card:**
   - Click on the flashcard to flip it and reveal the translation on the back side.

3. **Known Words:**
   - If you know the translation of a word or phrase, click the "I Know It" button to remove it from the learning list.


## Requirements

- Python 3.x
- Tkinter library
- Pandas library

Install the required libraries using the following command:

```bash
pip install pandas
```
## File Structure

- The flashcard data is stored in CSV format.
- The main application file is `flashy.py`.
- Images for the front and back sides of the flashcards are stored in the `images` folder.

## Usage

1. Run the `flashy.py` file to start the Flashy application.
2. Click the "Next Card" button to begin learning new words or phrases.
3. Flip the flashcards to reveal their translations.
4. Click the "I Know It" button for words or phrases that you know to remove them from the learning list.

## Contributions

Contributions are welcome! If you find any bugs, have suggestions for improvements, or want to add new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


This README provides an overview of the Flashy flashcard application, its features, how to use it, requirements, file structure, usage instructions, contributions, and license information.

# Every Line of Code



```python
from tkinter import *
import pandas
import random
```

- `from tkinter import *`: Imports all classes and functions from the tkinter module, which is used to create GUI applications.
- `import pandas`: Imports the pandas library, which is used for data manipulation and analysis.
- `import random`: Imports the random module, which is used for generating random numbers.

```python
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
```

- Defines a constant `BACKGROUND_COLOR` with a hex color code for the background color of the GUI.
- Initializes two dictionaries: `current_card` to store the current flashcard being displayed, and `to_learn` to store the words or phrases that the user needs to learn.

```python
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
```

- Tries to read a CSV file named "words_to_learn.csv" containing words or phrases that the user needs to learn.
- If the file is not found (`FileNotFoundError`), reads the original data from a CSV file named "french_words.csv" and converts it into a dictionary.
- Otherwise, reads the data from the "words_to_learn.csv" file and converts it into a dictionary.

```python
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
```

- Defines a function `next_card()` to display the next flashcard.
- Cancels any existing timer for flipping the card (`flip_timer`) using `after_cancel()`.
- Selects a random card from the `to_learn` list and updates the `current_card`.
- Configures the canvas to display the French text on the front side of the card.
- Configures the canvas to display the French word or phrase from the `current_card`.
- Configures the canvas to display the front side image of the card.
- Sets a timer (`flip_timer`) to automatically flip the card after 3000 milliseconds (3 seconds) using `after()`.

```python
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
```

