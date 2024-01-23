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