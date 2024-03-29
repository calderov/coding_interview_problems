# Problem:
# Determine if a 9x9 Sudoku board is valid. A valid Sudoku board will hold
# the following conditions:
# 
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. The 9 3x3 sub-boxes of the grid must also contain the digits 1-9 without
#   repetition.
# 
# Note:
# The Sudoku board could be partially filled, where empty cells are filled
# with the character '.'.
#

class Solution:
    def IsValidCollection(self, collection):
        cleanCollection = [value for value in collection if value != '.']
        return len(set(cleanCollection)) == len(cleanCollection)
        
    def AreValidRows(self, board):
        for row in board:
            if not self.IsValidCollection(row):
                return False
        return True

    def AreValidCols(self, board):
        cols = len(board[0])
        for i in range(cols):
            col = [row[i] for row in board]
            if not self.IsValidCollection(col):
                return False
        return True

    def AreValidSquares(self, board):
        for startRow in (0, 3, 6):
            for startCol in (0, 3, 6):
                square = []
                
                for i in range(startRow, startRow + 3):
                    for j in range(startCol, startCol + 3):
                        square.append(board[i][j])
                
                if not self.IsValidCollection(square):
                    return False

        return True
    

    # Solution complexity:
    # Time complexity: O(1) as we only iterate through the 9x9 board once
    # Space complexity: O(1) as we use at most 9 memory registers for entries
    def IsValidSudoku(self, board):
        return self.AreValidRows(board) and \
               self.AreValidCols(board) and \
               self.AreValidSquares(board)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    sudoku = \
    [["5","3",".", ".","7",".", ".",".","."]
    ,["6",".",".", "1","9","5", ".",".","."]
    ,[".","9","8", ".",".",".", ".","6","."]
    ,["8",".",".", ".","6",".", ".",".","3"]
    ,["4",".",".", "8",".","3", ".",".","1"]
    ,["7",".",".", ".","2",".", ".",".","6"]
    ,[".","6",".", ".",".",".", "2","8","."]
    ,[".",".",".", "4","1","9", ".",".","5"]
    ,[".",".",".", ".","8",".", ".","7","9"]]
    expectedOutput = True
    output = solution.IsValidSudoku(sudoku)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    sudoku = \
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    expectedOutput = False
    output = solution.IsValidSudoku(sudoku)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    sudoku = \
    [[".",".","4",".",".",".","6","3","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,["5",".",".",".",".",".",".","9","."]
    ,[".",".",".","5","6",".",".",".","."]
    ,["4",".","3",".",".",".",".",".","1"]
    ,[".",".",".","7",".",".",".",".","."]
    ,[".",".",".","5",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]]
    expectedOutput = False
    output = solution.IsValidSudoku(sudoku)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 4
    sudoku = \
    [["5","3",".", ".","7",".", ".",".","."]
    ,["6",".",".", "1","9","5", ".",".","."]
    ,[".","9","8", ".",".",".", ".","6","."]
    ,["8",".",".", ".","6",".", ".",".","3"]
    ,["4",".",".", "8",".","3", ".",".","1"]
    ,["7",".",".", ".","2",".", ".",".","6"]
    ,[".","6",".", ".",".",".", "2","8","."]
    ,[".",".",".", "4","1","9", ".","2","5"]
    ,[".",".",".", ".","8",".", ".","7","9"]]
    expectedOutput = False
    output = solution.IsValidSudoku(sudoku)
    print(output, expectedOutput, output == expectedOutput)