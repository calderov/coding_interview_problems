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
        self.sectors = [((0, 3), (0, 3)),
                        ((0, 3), (3, 6)),
                        ((0, 3), (6, 9)),

                        ((3, 6), (0, 3)),
                        ((3, 6), (3, 6)),
                        ((3, 6), (6, 9)),

                        ((6, 9), (0, 3)),
                        ((6, 9), (3, 6)),
                        ((6, 9), (6, 9))]

    def IsNumberInRow(self, num, row, sudoku):
        return num in sudoku[row]

    def IsNumberInCol(self, num, col, sudoku):
        for row in range(9):
            if sudoku[row][col] == num:
                return True
        return False

    def IsNumberInSector(self, num, row, col, sudoku):
        for rowRange, colRange in self.sectors:
            minRow, maxRow = rowRange
            minCol, maxCol = colRange
            if (minRow <= row < maxRow) and (minCol <= col < maxCol):
                break

        for row in range(minRow, maxRow):
            for col in range(minCol, maxCol):
                if num == sudoku[row][col]:
                    return True

        return False

    def IsValid(self, num, row, col, sudoku):
        return not self.IsNumberInRow(num, row, sudoku) and \
               not self.IsNumberInCol(num, col, sudoku) and \
               not self.IsNumberInSector(num, row, col, sudoku)

    def SolveSudoku(self, sudoku):
        for row in range(9):
            for col in range(9):

                if sudoku[row][col] == '.':

                    for num in self.numbers:
                        if self.IsValid(num, row, col, sudoku):
                            sudoku[row][col] = num

                            if self.SolveSudoku(sudoku):
                                return True

                            sudoku[row][col] = '.'

                    return False
        return True

def PrintSudoku(sudoku):
    for row in range(9):
        print(sudoku[row])

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    sudoku = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
              ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
              ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
              ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
              ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
              ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
              ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
              ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
              ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    expectedOutput = True
    output = solution.SolveSudoku(sudoku)
    print(output == expectedOutput)
    PrintSudoku(sudoku)
    print()

    # Example 2
    sudoku = [['8', '.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '3', '6', '.', '.', '.', '.', '.'],
              ['.', '7', '.', '.', '9', '.', '2', '.', '.'],
              ['.', '5', '.', '.', '.', '7', '.', '.', '.'],
              ['.', '.', '.', '.', '4', '5', '7', '.', '.'],
              ['.', '.', '.', '1', '.', '.', '.', '3', '.'],
              ['.', '.', '1', '.', '.', '.', '.', '6', '8'],
              ['.', '.', '8', '5', '.', '.', '.', '1', '.'],
              ['.', '9', '.', '.', '.', '.', '4', '.', '.']]
    expectedOutput = True
    output = solution.SolveSudoku(sudoku)
    print(output == expectedOutput)
    PrintSudoku(sudoku)
    print()

    sudoku = [[".","1",".",".","7",".",".","9","."],
              [".",".",".",".",".",".",".",".","."],
              [".",".",".","5",".","9",".",".","."],
              ["9",".",".",".","3",".",".",".","1"],
              [".",".","1",".",".",".","3",".","."],
              ["3",".",".","4",".",".",".",".","7"],
              [".",".",".","9",".","1",".",".","."],
              [".",".",".",".",".",".",".",".","."],
              [".","9",".",".","6",".",".","8","."]]
    expectedOutput = True
    output = solution.SolveSudoku(sudoku)
    print(output == expectedOutput)
    PrintSudoku(sudoku)
    print()