# Number Guessing Game

This is a simple Number Guessing Game implemented in Python. The game generates a random number between 1 and 100, and the player needs to guess the correct number within a limited number of attempts.

## How to Play

1. Run the Python script.
2. The game will display an ASCII art logo.
3. The target number is randomly generated between 1 and 100.
4. You will be prompted to choose a difficulty level:
   - Easy: 10 attempts
   - Hard: 5 attempts
5. You have a limited number of attempts to guess the correct number.
6. Enter your guess when prompted.
7. Receive feedback on whether your guess is too high or too low.
8. Keep guessing until you correctly identify the target number or run out of attempts.

## Script Structure

- The script uses the `random` module to generate a random target number.
- Different difficulty levels have different numbers of allowed guesses.
- The game prompts the player for input and provides feedback based on the comparison between the guess and the target number.
- After the game ends, you can choose to play again or exit.

## Usage

1. Ensure you have Python installed on your machine.
2. Run the script in a Python environment.

Enjoy the game and happy guessing!


# Every line of code

```python
# ASCII art logo
logo = """
  _____ _     _              _                
 / ____| |   (_)            (_)               
| |  __| |__  _ _ __   __ _  _ _ __   __ _  
| | |_ | '_ \| | '_ \ / _` || | '_ \ / _` | 
| |__| | | | | | | | | (_| || | | | | (_| | 
 \_____|_| |_|_|_| |_|\__, ||_|_| |_|\__, | 
                      __/ |         __/ | 
                     |___/         |___/  
"""

print(logo)
print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100 as the target.
target_number = random.randint(1, 100)

# Define different numbers of allowed guesses for each level.
easy_turns = 10
hard_turns = 5

# Set the number of turns based on the selected level.
turns_remaining = easy_turns  # Or hard_turns for hard mode.
```

Explanation:
- The script starts with an ASCII art logo and a welcome message.
- It uses the `random` module to generate a random integer between 1 and 100 as the target number.
- Different difficulty levels (`easy_turns` and `hard_turns`) are defined with varying numbers of allowed guesses.
- `turns_remaining` is set based on the selected difficulty level.

```python
while turns_remaining > 0:
    print(f"You have {turns_remaining} attempts remaining to guess the number.")

    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if user_guess == target_number:
        print(f"Congratulations! You guessed the correct number, which was {target_number}.")
        break
    elif user_guess > target_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

    turns_remaining -= 1
```

