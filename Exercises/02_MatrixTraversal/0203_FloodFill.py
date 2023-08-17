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
    # Solution:
    # Use Depth-First Search (DFS) to traverse the matrix from the given
    # starting cell replacing the color of those adjacent cells that are
    # of the original color of the starting one. 
    #
    # Solution complexity:
    # Time complexity: O(m * n) as that is the complexity of DFS
    # Space complexity: O(1)
    def FloodFill(self, matrix, row, col, newColor):
        if self.IsInMatrix(matrix, row, col):
            self.FloodFillDFS(matrix, row, col, matrix[row][col], newColor)
        return matrix

    def FloodFillDFS(self, matrix, row, col, oldColor, newColor):
        # Return early if row or col are out of bounds
        # or the color of the cell is not that of the
        # color we want to change.
        if not self.IsInMatrix(matrix, row, col) or matrix[row][col] != oldColor:
            return

        # Change the color of the current cell
        matrix[row][col] = newColor

        self.FloodFillDFS(matrix, row - 1, col, oldColor, newColor) # Color UP
        self.FloodFillDFS(matrix, row + 1, col, oldColor, newColor) # Color DOWN
        self.FloodFillDFS(matrix, row, col - 1, oldColor, newColor) # Color LEFT
        self.FloodFillDFS(matrix, row, col + 1, oldColor, newColor) # Color RIGHT

    def IsInMatrix(self, matrix, row, col):
        rows = len(matrix)
        cols = len(matrix[0])
        return not (row < 0 or col < 0 or row > rows - 1 or col > cols - 1)

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

    print("\nSuccess:", matrix == expectedOutput, "\n")

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
