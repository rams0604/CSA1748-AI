# Tic-Tac-Toe game in Python

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check for a win or tie
def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    for row in board:
        if any([spot == " " for spot in row]):
            return False
    return True

# Function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That spot is already taken. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

# Start the game
play_tic_tac_toe()
