def isBoardValid(board, row, column):
    dimension = len(board)
    for i in range(column):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row), range(column)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row + 1, dimension), range(column - 1, -1, -1)):
        if board[i][j] == 1:
            return False          
    return True 

def NQueen(board, column):
    if len(board) == column:
        print(board)
    else:
        for row in range(len(board)):
            board[row][column] = 1
            if isBoardValid(board, row, column) == True:
                NQueen(board, column + 1)
            board[row][column] = 0
            print(board)

dimension = 5
board = [[0]*dimension]*dimension
NQueen(board, 0)
# print(isBoardValid(board_2, 2, 2))
# isBoardValid(board_2, 2, 2)