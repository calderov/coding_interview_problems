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
        self.numbers = set([str(i) for i in range(1, 10)])
        self.sectors = [((0, 3), (0, 3)),
                        ((0, 3), (3, 6)),
                        ((0, 3), (6, 9)),

                        ((3, 6), (0, 3)),
                        ((3, 6), (3, 6)),
                        ((3, 6), (6, 9)),
                        
                        ((6, 9), (0, 3)),
                        ((6, 9), (3, 6)),
                        ((6, 9), (6, 9))]
        self.minPending = 100

    def SudokuSolver(self, sudoku):
        result = [[0 for i in range(9)] for j in range(9)]
        
        firstMissing = self.FindNextMissing(sudoku)
        if not firstMissing:
            return result

        row, col = firstMissing
        pending = self.CountMissing(sudoku)
        
        self.Backtrack(sudoku, row, col, pending, result)

        return result

        
    def Backtrack(self, sudoku, row, col, pending, result):
        # Return early if there are no more pending substitutions
        if pending == 1:
            for i in range(9):
                for j in range(9):
                    result[i][j] = sudoku[i][j]
            return

        numbersInRow = self.GetNumbersInRow(row, sudoku)
        numbersInCol = self.GetNumbersInCol(col, sudoku)
        numbersInSector = self.GetNumbersInSector(row, col, sudoku)

        candidates = set(self.numbers)
        candidates = candidates.difference(numbersInRow)
        candidates = candidates.difference(numbersInCol)
        candidates = candidates.difference(numbersInSector)

        for number in candidates:
            old, sudoku[row][col] = sudoku[row][col], number

            nextMissing = self.FindNextMissing(sudoku)
            if nextMissing:
                newRow, newCol = nextMissing
                self.Backtrack(sudoku, newRow, newCol, pending - 1, result)

            sudoku[row][col] = old

    def GetNumbersInRow(self, row, sudoku):
        return set(sudoku[row]).difference(set(['.']))

    def GetNumbersInCol(self, col, sudoku):
        numbersInCol = set()
        for row in range(9):
            numbersInCol.add(sudoku[row][col])
        return numbersInCol.difference(['.'])

    def GetNumbersInSector(self, row, col, sudoku):
        minRow = -1
        maxRow = -1
        minCol = -1
        maxCol = -1
        for rowRange, colRange in self.sectors:
            minRow, maxRow = rowRange
            minCol, maxCol = colRange
            if (minRow <= row < maxRow) and (minCol <= col < maxCol):
                break

        numbersInSector = set()

        for row in range(minRow, maxRow):
            for col in range(minCol, maxCol):
                numbersInSector.add(sudoku[row][col])

        return numbersInSector.difference(set(['.']))

    def FindNextMissing(self, sudoku):
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == '.':
                    return (row, col)
        return None
    
    def CountMissing(self, sudoku):
        totalMissing = 0
        for row in range(9):
            for col in range(9):
                if sudoku[row][col] == '.':
                    totalMissing += 1
        return totalMissing

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
    
    # Print solution
    for row in range(9):
        print(output[row])

    # Verify solution
    solutionMatch = True
    for row in range(9):
        for col in range(9):
            if output[row][col] != expectedOutput[row][col]:
                print(output[row][col], expectedOutput[row][col])
                solutionMatch = False
                break

    print(solutionMatch)
