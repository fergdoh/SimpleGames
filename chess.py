WHITE_PIECES = {"P", "R", "N", "B", "Q", "K"}
BLACK_PIECES = {"p", "r", "n", "b", "q", "k"}

currentPlayer = "White"

if currentPlayer == "White":
    valid_pieces = WHITE_PIECES
else:
    valid_pieces = BLACK_PIECES

winner = None
gameRunning = True

def initialise_board(board):

    for col in range(8):
        board[8 + col] = " p "

    for col in range(8):
        board[48 + col] = " P "

    piece_positions = {
        " r ": [0, 7, 56, 63],
        " n ": [1, 6, 57, 62],
        " b ": [2, 5, 58, 61],
        }

    for piece, positions in piece_positions.items():
        for pos in positions:
            board[pos] = piece.upper() if pos >= 56 else piece.lower()

    board[3] = " q "
    board[59] = " Q "

    board[4] = " k "
    board[60] = " K "

    column_labels = "  a   b   c   d   e   f   g   h"
    print(column_labels)
    print("  ---------------------------------")

    for row in range(8):
        row_label = 8 - row
        start = row * 8
        row_data = "|".join(board[start:start + 8])
        
        print(f"{row_label} |{row_data}|")
        print("  ---------------------------------")

board = ["---", "-+-", "---", "-+-", "---", "-+-", "---", "-+-",
            "-+-", "---", "-+-", "---", "-+-", "---", "-+-", "---",
            "---", "-+-", "---", "-+-", "---", "-+-", "---", "-+-",
            "-+-", "---", "-+-", "---", "-+-", "---", "-+-", "---",
            "---", "-+-", "---", "-+-", "---", "-+-", "---", "-+-",
            "-+-", "---", "-+-", "---", "-+-", "---", "-+-", "---",
            "---", "-+-", "---", "-+-", "---", "-+-", "---", "-+-",
            "-+-", "---", "-+-", "---", "-+-", "---", "-+-", "---"]

# def piece_move(board, pieces):
#     for pieces in WHITE_PIECES and BLACK_PIECES:

def is_valid_move(start_pos, end_pos):
    piece = board[start_pos]
    
    # Ensure a piece exists at the chosen position
    if piece == "---" or "-+-":
        print("No piece at this position!")
        return False

    # Ensure the correct player is moving their own piece
    if currentPlayer == "White" and piece not in WHITE_PIECES:
        print("White can only move White pieces!")
        return False
    if currentPlayer == "Black" and piece not in BLACK_PIECES:
        print("Black can only move Black pieces!")
        return False

    return True

# Work in progress from here.

def playerInput(board, currentPlayer, start_pos, end_pos):
    inp = input(f"{currentPlayer}, choose a piece ({valid_pieces}): ")
    if inp == "p" or "P":
        print(f"Pawn{board[start_pos]}")
        move = input(f"Select ")

    

while gameRunning:
        initialise_board(board)
        playerInput()
        # swtichPlayer()
        # if checkWin():
        #     break
        # if checkTie(board):
        #     break
        # valid_move = False
        # while not valid_move:
        #     valid_move = computer(board)
        # swtichPlayer()
        # if checkWin():
        #     break
        # if checkTie(board):
        break


# def switchPlayer():
#     global currentPlayer
#     currentPlayer = "Black" if currentPlayer == "White" else "White"
