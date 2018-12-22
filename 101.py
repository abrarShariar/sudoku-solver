# NEED TO FIX
# check test.py for new code
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


def fillUpRow (row, col, board):
    if row >= 9:
        return True

    if board[row][col] == 0:
        for n in range(1, 10):
            if isSafe(row, col, board, n):
                board[row][col] = n
                if fillUpRow(row + 1, col, board) == True:
                    return True
                else:
                    board[row][col] = 0
    else:
        if fillUpRow(row + 1, col, board) == True:
            return True

    # return False

# FIX this
def generateSolution (board, row, col):
    if col >= 9:
        return True
    if row >= 9 or row < 0:
        return True

    if fillUpRow(row, col, board) == True:
        if generateSolution(board, row, col + 1) == True:
            return True
    else:
        print("Here")
        board[row-1][col] = 0
        generateSolution(board, row - 1, col)

def prettyPrint (board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print("")

start = 0
generateSolution(board, start, start)
prettyPrint(board)
