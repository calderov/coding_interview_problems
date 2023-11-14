# Sudoku Solver (hard)
# Problem:
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# - Each of the digits 1-9 must occur exactly once in each row.
# - Each of the digits 1-9 must occur exactly once in each column.
# - Each of the digits 1-9 must occur exactly once in each of the 9 3x3
#   sub-boxes of the grid.
# - The '.' character indicates empty cells.
# 
# Example:
#
#   Input:
#             ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
#             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
#             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
#             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
#             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
#             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
#             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
#             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
#             ['.', '.', '.', '.', '8', '.', '.', '7', '9']
#   Output:
# 
#             ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
#             ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
#             ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
#             ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
#             ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
#             ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
#             ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
#             ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
#             ['3', '4', '5', '2', '8', '6', '1', '7', '9']
# 
# Explanation: The given output is the only valid Sudoku solution.

class Solution:
    def __init__(self):
        self.numbers = [str(i) for i in range(1, 10)]
        pass

    def SudokuSolver(self, sudoku):
        result = list(sudoku)
    
    def CheckRow(self, row, sudoku):
        missingNumbers = set(self.numbers)
        
        for num in sudoku[row]:
            if num in missingNumbers:
                missingNumbers.remove(num)

        return missingNumbers

    def CheckCol(self, col, sudoku):
        missingNumbers = set(self.numbers)

        for row in range(len(sudoku)):
            num = sudoku[row][col]
            
            if num in missingNumbers:
                missingNumbers.remove(num)
        
        return missingNumbers

    def CheckSector(self, row, col, sudoku):
        numbers = set(self.numbers)
        sectors = [((0, 3), (0, 3)),
                   ((0, 3), (3, 6)),
                   ((0, 3), (6, 9)),

                   ((3, 6), (0, 3)),
                   ((3, 6), (3, 6)),
                   ((3, 6), (6, 9)),
                  
                   ((6, 9), (0, 3)),
                   ((6, 9), (3, 6)),
                   ((6, 9), (6, 9))]

        # for rowRange, colRange in sectors:
        #     minRow

        

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    sudoku =         [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
                      ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                      ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                      ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                      ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                      ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                      ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                      ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                      ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

    expectedOutput = [['5', '3', '4', '6', '7', '8', '9', '1', '2'],
                      ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                      ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
                      ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                      ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
                      ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                      ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
                      ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                      ['3', '4', '5', '2', '8', '6', '1', '7', '9']]  

    output = solution.SudokuSolver(sudoku)
    for row in range(len(sudoku)):
        print(output[row])
        print(expectedOutput[row])
        print()
    print(output == expectedOutput)
