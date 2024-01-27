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