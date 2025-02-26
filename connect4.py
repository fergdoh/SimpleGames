import random

board = ["---", "---", "---", "---", "---", "---", "---",
        "---", "---", "---", "---", "---", "---", "---",
        "---", "---", "---", "---", "---", "---", "---",
        "---", "---", "---", "---", "---", "---", "---",
        "---", "---", "---", "---", "---", "---", "---",
        "---", "---", "---", "---", "---", "---", "---"]

currentPlayer = "-X-"
winner = None
gameRunning = True

def printBoard(board):
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + board[6] + "|")
    print("-----------------------------")
    print("|" + board[7] + "|" + board[8] + "|" + board[9] + "|" + board[10] + "|" + board[11] + "|" + board[12] + "|" + board[13] + "|")
    print("-----------------------------")
    print("|" + board[14] + "|" + board[15] + "|" + board[16] + "|" + board[17] + "|" + board[18] + "|" + board[19] + "|" + board[20] + "|")
    print("-----------------------------")
    print("|" + board[21] + "|" + board[22] + "|" + board[23] + "|" + board[24] + "|" + board[25] + "|" + board[26] + "|" + board[27] + "|")
    print("-----------------------------")
    print("|" + board[28] + "|" + board[29] + "|" + board[30] + "|" + board[31] + "|" + board[32] + "|" + board[33] + "|" + board[34] + "|")
    print("-----------------------------")
    print("|" + board[35] + "|" + board[36] + "|" + board[37] + "|" + board[38] + "|" + board[39] + "|" + board[40] + "|" + board[41] + "|")
    print("-----------------------------")

def playerInput(board, currentPlayer):
    inp = int(input(f"{currentPlayer}, enter a column (1-7): ")) - 1
    
    if inp < 0 or inp > 6:
        print("Invalid column! Choose between 1-7.")
        return False
    
    for row in range(5, -1, -1):
        index = row * 7 + inp
        if board[index] == "---":
            board[index] = currentPlayer
            return True
        
    print("Column full! Choose another column.")
    return False

def checkHorizontal(board):
    global winner
    for row in range(6):
        for col in range(4):
            index = row * 7 + col
            if board[index] == board[index + 1] == board[index + 2] == board[index + 3] and board[index] != "---":
                winner = board[index]
                return True
    return False

def checkVertical(board):
    global winner
    for row in range(3):
        for col in range(7):
            index = row * 7 + col
            if board[index] == board[index + 7] == board[index + 14] == board[index + 21] and board[index] != "---":
                winner = board[index]
                return True
    return False

def checkDiagonal(board):
    global winner
    for row in range(3):
        for col in range(4):
            index = row * 7 + col
            if board[index] == board[index + 8] == board[index + 16] == board[index + 24] and board[index] != "---":
                winner = board[index]
                return True
            elif board[index] == board[index + 6] == board[index + 12] == board[index + 18] and board[index] != "---":
                winner = board[index]
                return True
    return False
    
def checkTie(board):
    global gameRunning
    if "---" not in board:
        printBoard(board)
        print("Tie")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        printBoard(board)
        print(f"Winner is {winner}")
        gameRunning = False

def Player():
    global currentPlayer
    valid_move = False
    while not valid_move:
        valid_move = playerInput(board, currentPlayer)

def computer(board):
    while True and currentPlayer == "-O-":
        position = random.randint(0, 6)
        for row in range(5, -1, -1):
            index = row * 7 + position
            if board[index] == "---":
                    board[index] = "-O-"
                    return True
            
def swtichPlayer():
    global currentPlayer
    if currentPlayer == "-X-":
        currentPlayer = "-O-"
    else:
        currentPlayer = "-X-"

def resetGame():
    return ["---"] * 42, "-X-", None, True

def singlePlayer():
    while gameRunning:
        printBoard(board)
        Player()
        swtichPlayer()
        if checkWin():
            break
        if checkTie(board):
            break
        valid_move = False
        while not valid_move:
            valid_move = computer(board)
        swtichPlayer()
        if checkWin():
            break
        if checkTie(board):
            break

def multiPlayer():
    while gameRunning:
        printBoard(board)
        Player()
        if checkWin():
            break
        if checkTie(board):
            break
        swtichPlayer()
        if checkWin():
            break
        if checkTie(board):
            break

while True:
    board, currentPlayer, winner, gameRunning = resetGame()
    print(f"Welcome to Fergal's Connect4!")
    mode = input(f"Would you like to play single player or multiplayer? (S/M) ").strip().upper()
    if mode == "S":
        singlePlayer()
    elif mode == "M":
        multiPlayer()
    elif mode != "S" or "M":
        mode = input(f"Single Player (S) or Multiplayer (M): ").strip().upper()

    newgame = input("Would you like to play again? (Y/N): ").strip().upper()
    if newgame != "Y":
        print("Thanks for playing!")
        break
