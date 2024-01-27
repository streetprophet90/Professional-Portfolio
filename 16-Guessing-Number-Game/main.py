import random

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

# Provide feedback when the game ends.
if turns_remaining == 0:
    print(f"Game over. The correct number was {target_number}.")

play_again = input("Do you want to play again? (yes/no): ")
if play_again.lower() == "yes":
    target_number = random.randint(1, 100)
    turns_remaining = easy_turns  # Reset turns for a new game.
    print("Let's play again!")
else:
    print("Thank you for playing!")