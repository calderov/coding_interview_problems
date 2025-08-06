# Question 1: 2D Spiral Array

# Find the pattern and complete the function:
# int[][] spiral(int n);
# where n is the size of the 2D array.
# Sample Result
# input = 3
# 123
# 894
# 765

# input = 4
# 01 02 03 04
# 12 13 14 05
# 11 16 15 06
# 10 09 08 07

# input = 8
# 1 2 3 4 5 6 7 8
# 28 29 30 31 32 33 34 9
# 27 48 49 50 51 52 35 10
# 26 47 60 61 62 53 36 11
# 25 46 59 64 63 54 37 12
# 24 45 58 57 56 55 38 13
# 23 44 43 42 41 40 39 14
# 22 21 20 19 18 17 16 15

def isValid(matrix, row, col, rows, cols):
    return row < rows and col < cols and row >= 0 and col >= 0 and matrix[row][col] == 0

def getSpiral(inputValue):
    matrix = [[0 for col in range(inputValue)] for row in range(inputValue)]
    
    value = 1
    maxValue = inputValue ** 2

    row = -1
    col = -1

    while value < maxValue:
        # Right
        col += 1
        row += 1
        while isValid(matrix, row, col, inputValue, inputValue):
            matrix[row][col] = value
            value += 1
            col += 1

        # Down
        row += 1
        col -= 1
        while isValid(matrix, row, col, inputValue, inputValue):
            matrix[row][col] = value
            value += 1
            row += 1

        # Left
        row -= 1
        col -= 1
        while isValid(matrix, row, col, inputValue, inputValue):
            matrix[row][col] = value
            value += 1
            col -= 1

        # Up
        row -= 1
        col += 1
        while isValid(matrix, row, col, inputValue, inputValue):
            matrix[row][col] = value
            value += 1
            row -= 1

    return matrix

def printMatrix(matrix):
    for row in matrix:
        print([f"{str(col).zfill(2)}" for col in row])

if __name__ == "__main__":
    inputValue = 4
    expectedOutput = [
        [  1,  2,  3,  4],
        [ 12, 13, 14,  5],
        [ 11, 16, 15,  6],
        [ 10,  9,  8,  7]
    ]

    output = getSpiral(inputValue)

    print(inputValue)
    print()
    printMatrix(expectedOutput)
    print()
    printMatrix(output)
    print()
    print(expectedOutput == output)
