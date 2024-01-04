import random

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    return False

def is_board_full(board):
    return ' ' not in board

def play_tic_tac_toe():
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board([str(i + 1) for i in range(9)])

    while True:
        # Computer's move
        computer_move = random.randint(1, 9)
        while board[computer_move - 1] != ' ':
            computer_move = random.randint(1, 9)
        board[computer_move - 1] = 'X'
        print(f"\nComputer's move:")
        print_board(board)

        # Check if the game is over
        if check_winner(board):
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        # User's move
        try:
            user_move = int(input("\nEnter your move (1-9): "))
            if not 1 <= user_move <= 9 or board[user_move - 1] != ' ':
                raise ValueError("Invalid move. Try again.")
        except ValueError as e:
            print(e)
            continue

        board[user_move - 1] = 'O'
        print_board(board)

        # Check if the game is over
        if check_winner(board):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
