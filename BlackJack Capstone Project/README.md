# Blackjack Game

This Python script implements a simple text-based Blackjack game following certain house rules. The game allows the user to play against the computer dealer, following the standard Blackjack rules with some variations.

## House Rules

1. The deck is unlimited in size.
2. There are no jokers.
3. The Jack/Queen/King all count as 10.
4. The Ace can count as 11 or 1.

## How to Play

1. Run the script.
2. The game will deal two cards to both the player and the computer.
3. The player can choose to draw additional cards ('y') or pass ('n').
4. If the player chooses to draw, new cards are added to their hand.
5. The game automatically calculates the scores.
6. The computer will play automatically, drawing cards until its score is at least 17.
7. The winner is determined based on the scores.

## Project Structure

- **`deal_card()`**: Function to return a random card from the deck.
- **`calculate_score(cards)`**: Function to calculate the score of a hand.
- **`compare(user_score, computer_score)`**: Function to compare the scores and determine the winner.
- **`play_game()`**: Function to orchestrate the entire game.
- **`logo`**: ASCII art for the Blackjack game logo.

## How to Run

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/streetprophet90/BlackJackCapstoneProject.git
   cd blackjack_game.py
   ```

2. Run the script.
   ```bash
   python blackjack_game.py
   ```

3. Follow the on-screen instructions to play the game.

**Note**: Adjustments may be needed based on user preferences or additional features. The game provides a basic structure that can be expanded or modified as desired.

Sure, let's go through the code and explain each part:

```python
import random
from replit import clear
from art import logo
```

- `import random`: Imports the `random` module for generating random numbers, which is used for dealing cards.
- `from replit import clear`: Imports the `clear` function from the `replit` module to clear the console screen between game rounds.
- `from art import logo`: Imports ASCII art for the Blackjack game logo, enhancing the user interface.

```python
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
```

- `deal_card()`: Function to return a random card from the deck. The deck is represented by the `cards` list, and `random.choice(cards)` is used to select a random card.

```python
def calculate_score(cards):  
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
```



- This part initiates a loop to ask the user if they want to play another round. If the user enters 'y,' the console is cleared, and a new game is started by calling `play_game()`.

This script combines functions and game logic to create a simple Blackjack game with a console-based interface. The game flow is controlled by user input, and the logic adheres to the specified Blackjack rules.