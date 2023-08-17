# Problem:
# Any image can be represented by a 2D integer array (i.e., a matrix) where
# each cell represents the pixel value of the image.
#
# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color.
# The given color is applied to all horizontally and vertically connected
# cells with the same color as that of the starting cell. Recursively,
# the algorithm fills cells with the new color until it encounters a cell
# with a different color than the starting cell.
#
# Given a matrix, a starting cell, and a color, flood fill the matrix.
#
# Example:
#
# Input: matrix =  [[0, 1, 1, 1, 0],
#                   [0, 0, 0, 1, 1],
#                   [0, 1, 1, 1, 0],
#                   [0, 1, 1, 0, 0],
#                   [0, 0, 0, 0, 0]]
#
# starting cell = (1, 3)
# new color = 2
#
# Output: matrix = [[0, 2, 2, 2, 0],
#                   [0, 0, 0, 2, 2],
#                   [0, 2, 2, 2, 0],
#                   [0, 2, 2, 0, 0],
#                   [0, 0, 0, 0, 0]]
# 

class Solution:
    def floodFill(self, matrix, row, col, newColor):
        self.FloodFill(matrix, row, col, newColor)
        return matrix

    # Solution:
    # Solution complexity:
    # Time complexity: O(m * n)
    # Space complexity: O(1)
    def FloodFill(self, matrix, row, col, newColor):
        rows = len(matrix)
        cols = len(matrix[0])

        # Return early if x or y are out of bounds
        if row < 0 or col < 0 or row > rows - 1 or col > cols - 1:
            return

        # Save the old color for reference and apply the new color to the cell
        oldColor = matrix[row][col]
        matrix[row][col] = newColor

        # Color UP
        if row > 0 and matrix[row - 1][col] == oldColor:
            self.FloodFill(matrix, row - 1, col, newColor)

        # Color DOWN
        if row < rows - 1 and matrix[row + 1][col] == oldColor:
            self.FloodFill(matrix, row + 1, col, newColor)

        # Color LEFT
        if col > 0 and matrix[row][col - 1] == oldColor:
            self.FloodFill(matrix, row, col - 1, newColor)

        # Color RIGHT
        if col < cols - 1 and matrix[row][col + 1] == oldColor:
            self.FloodFill(matrix, row, col + 1, newColor)

def PrintMatrix(matrix):
    for row in matrix:
        print(row)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = \
    [[0, 1, 1, 1, 0],
     [0, 0, 0, 1, 1],
     [0, 1, 1, 1, 0],
     [0, 1, 1, 0, 0],
     [0, 0, 0, 0, 0]]

    cell = (1, 3)
    newColor = 2

    expectedOutput = \
    [[0, 2, 2, 2, 0],
     [0, 0, 0, 2, 2],
     [0, 2, 2, 2, 0],
     [0, 2, 2, 0, 0],
     [0, 0, 0, 0, 0]]
    
    print("Input")
    PrintMatrix(matrix)
    print(cell, newColor)

    print()
    solution.FloodFill(matrix, cell[0], cell[1], newColor)

    print("Output")
    PrintMatrix(matrix)

    print("\nSuccess:", matrix == expectedOutput)

    # Example 2
    matrix = \
    [[1, 2, 1],
     [0, 1, 0],
     [1, 2, 1]]
    
    cell = (0, 1)
    newColor = 3

    expectedOutput = \
    [[1, 3, 1],
     [0, 1, 0],
     [1, 2, 1]]

    print("Input")
    PrintMatrix(matrix)
    print(cell, newColor)

    print()
    solution.FloodFill(matrix, cell[0], cell[1], newColor)

    print("Output")
    PrintMatrix(matrix)

    print("\nSuccess:", matrix == expectedOutput)
