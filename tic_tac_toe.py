# Tic Tac Toe 2 Player Game 

# Function to print the Tic Tac Toe Board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to Check for a win
def check_winner(board, player):
    # Check Rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check Columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check Diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False  # Move this outside the loop

# Function to Check if the Board is full
def is_full(board):
    return all(cell != " " for row in board for cell in row)

# Main function to play Tic Tac Toe 
def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        # Get User Input
        while True:
            try:
                row = int(input("Enter Row (0-2): "))
                col = int(input("Enter Column (0-2): "))

                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = player  # Fix: Update the board
                    break
                else:
                    print("Invalid Move! Try Again.")
            except ValueError:
                print("Please Enter Valid Numbers (0-2).")

        print_board(board)  # Moved here, so it prints after a valid move

        # Check if there's a Winner
        if check_winner(board, player):
            print(f"Congratulations! Player {player} Wins!")
            break

        # Check for a tie
        if is_full(board):
            print("It's a Tie!")
            break

        turn += 1

# Run The Game
play_tic_tac_toe()