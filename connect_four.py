import numpy as np

#initialize the board
def create_board():
    """Create an empty Connect Four board."""
    return np.zeros((6,7))

def drop_piece(board, row, col, piece):
    """Drop a piece onto the board."""
    board[row][col] = piece

def is_valid_location(board, col):
    """Check if a column is valid for dropping a piece."""
    return board[5][col] == 0

def get_next_open_row(board, col):
    """Get the next open row for dropping a piece."""
    for r in range(6):
        if board[r][col] == 0:
            return r

def print_board(board):
    """Print the current state of the board."""
    print(np.flip(board, 0))


def winning_move(board, piece):
    """Check if a player has won the game."""
    # Check horizontal locations
    for c in range(4):
        for r in range(6):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations
    for c in range(7):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonal locations
    for c in range(4):
        for r in range(3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonal locations
    for c in range(4):
        for r in range(3, 6):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def play_game():
    """Play a game of Connect Four."""
    board = create_board()
    game_over = False
    turn = 0

    while not game_over:
        # Player 1 turn
        if turn == 0:
            col = int(input("Player 1 make your selection (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 1)
                if winning_move(board, 1):
                    print("Player 1 wins!")
                    game_over = True

        # Player 2 turn
        else:
            col = int(input("Player 2 make your selection (0-6): "))
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 2)
                if winning_move(board, 2):
                    print("Player 2 wins!")
                    game_over = True
        
        # Print the board
        print_board(board)
        turn = (turn + 1) % 2  # Switch players

#start the game
play_game()
