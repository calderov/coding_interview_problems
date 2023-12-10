def PlaceNQueens(board, queens):
    if queens == 0:
        return True
    
    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        for col in range(cols):
            if IsValid(board, row, col):
                board[row][col] = 1
                
                if PlaceNQueens(board, queens - 1):
                    return True

                board[row][col] = 0 # backtrack
    
    return False

def IsValid(board, targetRow, targetCol):
    rows = len(board)
    cols = len(board[0])

    # Check cell
    if board[targetRow][targetCol]:
        return False
    
    # Check row
    for row in range(rows):
        if board[row][targetCol]:
            return False

    # Check col
    for col in range(cols):
        if board[targetRow][col]:
            return False

    # Check top left diagonal
    row = targetRow
    col = targetCol
    while row >= 0 and col >= 0:
        if board[row][col]:
            return False
        row -= 1
        col -= 1

    # Check top right diagonal
    row = targetRow
    col = targetCol
    while row >= 0 and col < cols:
        if board[row][col]:
            return False
        row -= 1
        col += 1

    # Check bottom left diagonal
    row = targetRow
    col = targetCol
    while row < rows and col >= 0:
        if board[row][col]:
            return False
        row += 1
        col -= 1

    # Check bottom right diagonal
    row = targetRow
    col = targetCol
    while row < rows and col < cols:
        if board[row][col]:
            return False
        row += 1
        col += 1

    return True

def PrintBoard(board):
    for row in board:
        print(row)

def MakeBoard(n, m):
    return [[0 for col in range(m)] for row in range(n)]

if __name__ == "__main__":
    n = 8 # Number of queens and board size (n x n)
    board = MakeBoard(n, n)
    if PlaceNQueens(board, n):
        PrintBoard(board)
    else:
        print("No solution found")