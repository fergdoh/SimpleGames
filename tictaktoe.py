import random

board = ["---", "---", "---",
        "---", "---", "---",
        "---", "---", "---"]

currentPlayer = "-X-"
winner = None
gameRunning = True

def printBoard(board):
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-------------")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-------------")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "---":
        board[inp-1] = currentPlayer
    else:
        print("Find another spot")

def checkHoritzontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "---":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "---":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "---":
        winner = board[6] 
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "---":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "---":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "---":
        winner = board[2] 
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != "---":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "---":
        winner = board[4] 
        return True
    
def checkTie(board):
    global gameRunning
    if "---" not in board:
        printBoard(board)
        print("Tie")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHoritzontal(board) or checkRow(board):
        print(f"Winner is {winner}")
        gameRunning = False

def swtichPlayer():
    global currentPlayer
    if currentPlayer == "-X-":
        currentPlayer = "-O-"
    else:
        currentPlayer = "-X-"

def computer(board):
    while currentPlayer == "-O-":
        position = random.randint(0, 8)
        if board[position] == "---":
            board[position] = "-O-"
            swtichPlayer()

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    swtichPlayer()
    computer(board)
    checkWin()
    checkTie(board)

