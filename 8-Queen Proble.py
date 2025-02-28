def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQ(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQ(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

def solve():
    board = [[0 for _ in range(8)] for _ in range(8)]
    if solveNQ(board, 0) == False:
        print("Solution does not exist")
        return False
    print(board)
    return True

solve()
