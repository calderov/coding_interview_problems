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
    def AreAllUnique(self, entries):
        return len(set(entries)) == len(entries)

    def IsValidRow(self, sudoku, row):
        entries = [entry for entry in sudoku[row] if entry != "."]
        return self.AreAllUnique(entries)
    
    def IsValidCol(self, sudoku, col):
        rows = 9
        entries = [sudoku[row][col] for row in range(rows) if sudoku[row][col] != "."]
        return self.AreAllUnique(entries)
    
    def IsValidQuadrant(self, sudoku, quadrant):
        startRow = (quadrant // 3) * 3
        startCol = (quadrant % 3) * 3

        entries = []

        for row in range(startRow, startRow + 3):
            for col in range(startCol, startCol + 3):
                if sudoku[row][col] != ".":
                    entries.append(sudoku[row][col])

        return self.AreAllUnique(entries)

    # Solution complexity:
    # Time complexity: O(1) as we only iterate through the 9x9 board once
    # Space complexity: O(1) as we use at most 9 memory registers for entries
    def IsValidSudoku(self, sudoku):
        rows = 9
        cols = 9
        quadrants = 9

        # Verify rows
        for row in range(rows):
            if not self.IsValidRow(sudoku, row):
                return False

        # Verify cols
        for col in range(cols):
            if not self.IsValidCol(sudoku, col):
                return False
            
        # Verify quadrants
        for quadrant in range(quadrants):
            if not self.IsValidQuadrant(sudoku, quadrant):
                return False

        return True

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