# FIX grid checking
board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

def isSafe (row, col, board, num):
    # check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # check column
    for i in range(9):
        if board[i][col] == num:
            return False

    return True

def find_empty_location (board, l):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False

def solveSudoku (board):
    l = [0, 0]
    if find_empty_location(board, l) == False:
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if isSafe(row, col, board, num) == True:
            board[row][col] = num
            if solveSudoku(board) == True:
                return True
            board[row][col] = 0
    return False


def prettyPrint (board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print("")

if solveSudoku(board) == True:
    print(True)
else:
    print(False)

prettyPrint(board)
