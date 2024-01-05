The key lines of the Tic Tac Toe Python script

1. `print_board(board)`: This function prints the current state of the Tic Tac Toe board to the console. It uses a nested loop to iterate over each cell in the 3x3 grid.

2. `check_winner(board, player)`: This function checks if the specified player has won the game by examining the rows, columns, and diagonals of the board.

3. `is_board_full(board)`: This function checks if the board is full, meaning there are no empty cells left. If the board is full and there is no winner, the game is considered a tie.

4. `play_tic_tac_toe()`: This is the main function that orchestrates the entire game. It initializes the board, sets the current player to 'X', and enters into a loop where players take turns making moves until there is a winner or a tie.

5. `print_board(board)`: This line prints the current state of the board before each move.

6. `row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))`: This line prompts the current player to enter the row where they want to place their symbol ('X' or 'O'). The `int(input(...))` part is used to get an integer input from the user.

7. `col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))`: Similar to the previous line, this prompts the player for the column input.

8. `if board[row][col] == ' ':`: Checks if the selected cell is empty before making a move. If the cell is empty, the move is valid; otherwise, the player is prompted to try again.

9. `board[row][col] = current_player`: Updates the board with the player's move.

10. `if check_winner(board, current_player):`: Checks if the current player has won after making a move.

11. `if is_board_full(board):`: Checks if the board is full, indicating a tie if there is no winner.

12. `current_player = 'O' if current_player == 'X' else 'X'`: Switches the current player for the next turn.

13. `print("Cell already taken. Try again.")`: Informs the player that the chosen cell is already occupied.

The game continues in the loop until there is a winner or a tie, and the final state of the board is printed accordingly.
