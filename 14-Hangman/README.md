### `main.py`


# Hangman Game

This is a simple implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list, and the player needs to guess the word by entering letters. The player starts with 6 lives and loses a life for each incorrect guess. The game ends when the player either correctly guesses the entire word or runs out of lives.

```markdown
## How to Play

1. Run the `main.py` file.
2. You will be prompted to guess a letter.
3. If the guessed letter is correct, it will be revealed in the blanks.
4. If the guessed letter is incorrect, you lose a life.
5. The game ends when you correctly guess the entire word or run out of lives.

Feel free to explore the code and modify it to add new words or customize the gameplay.

```

### `hangman_words.py`

```markdown
# Hangman Words List

This file (`hangman_words.py`) contains a list of words used in the Hangman game. You can customize or extend this list to include your own words for the game. Each word in the list is randomly selected for gameplay.

```

### `hangman_art.py`

```markdown
# Hangman Art and Stages

This file (`hangman_art.py`) contains ASCII art representations of the hangman stages and the game logo. The stages are displayed as the player makes incorrect guesses, and the logo is presented at the beginning of the game. Feel free to modify the art or add your own creative elements.

```
Sure, let's go through the code in `main.py` line by line:

```python
# Import necessary modules
from hangman_words import word_list
from hangman_art import stages, logo
import random
```

- **Explanation**: This part imports the required modules. `word_list` and `stages` are lists of words and ASCII art hangman stages, respectively. `logo` is ASCII art for the game's logo. `random` is used to randomly select a word from `word_list`.

```python
# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
```

- **Explanation**: The `chosen_word` variable is assigned a random word from `word_list`. `word_length` stores the length of the chosen word.

```python
# Initialize game variables
end_of_game = False
lives = 6
```

- **Explanation**: `end_of_game` is a boolean variable that tracks whether the game is over. `lives` represents the number of lives the player has.

```python
# Create blanks for the word
display = ["_" for _ in range(word_length)]
```

- **Explanation**: The `display` list is initialized with underscores, representing blanks for each letter in the word.

```python
# Main game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()
```

- **Explanation**: The game enters a loop where the player is prompted to guess a letter. The guessed letter is converted to lowercase.

```python
    # Check if the letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")
```

- **Explanation**: Checks if the guessed letter is already in the `display` list, indicating it has been guessed before. If so, a message is printed.

```python
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
```

- **Explanation**: Iterates through each position in the word and updates the `display` list if the guessed letter matches.

```python
    # Check if the guessed letter is incorrect
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
```

