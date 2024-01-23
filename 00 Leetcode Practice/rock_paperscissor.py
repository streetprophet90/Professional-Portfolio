def rps(p1, p2):
    # Define the winning combinations
    winning_combinations = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    # Check for a draw
    if p1 == p2:
        return "Draw!"

    # Check for the winner
    if winning_combinations[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"