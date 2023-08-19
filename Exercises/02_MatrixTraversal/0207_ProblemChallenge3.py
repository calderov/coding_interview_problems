# Problem: 
# You are given a 2D matrix containing different characters, you need to find
# if there exists any cycle consisting of the same character in the matrix.
#
# A cycle is a path in the matrix that starts and ends at the same cell and has
# four or more cells. From a given cell, you can move to one of the cells adjacent
# to it - in one of the four directions (up, down, left, or right), if it has the
# same character value of the current cell.
#
# Write a function to find if the matrix has a cycle.
#
# Example:
#
# Input: matrix = [["a", "a", "a", "a"],
#                  ["b", "a", "c", "a"],
#                  ["b", "a", "c", "a"],
#                  ["b", "a", "a", "a"]]
# 
# Output: true

class Solution:
    # Solution:
    #
    # Solution complexity:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def HasCycle(self, matrix):
        rows, cols = self.GetDimensions(matrix)
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    if self.FindCycleDFS(matrix, visited, matrix[i][j], i, j):
                        return True
        return False

    def FindCycleDFS(self, matrix, visited, symbol, row, col, prevRow = None, prevCol = None):
        if not self.IsInMatrix(matrix, row, col):
            return False
        
        if matrix[row][col] != symbol:
            return False
        
        if (row, col) in visited:
            return True
            
        visited.add((row, col))

        # Explore Up
        if row - 1 != prevRow and self.FindCycleDFS(matrix, visited, symbol, row - 1, col, row, col):
            return True

        # Explore Down
        if row + 1 != prevRow and self.FindCycleDFS(matrix, visited, symbol, row + 1, col, row, col):
            return True

        # Explore Left
        if col - 1!= prevCol and self.FindCycleDFS(matrix, visited, symbol, row, col - 1, row, col):
            return True

        # Explore Right
        if col + 1 != prevCol and self.FindCycleDFS(matrix, visited, symbol, row, col + 1, row, col):
            return True
        
        return False

    def IsInMatrix(self, matrix, row, col):
        rows, cols = self.GetDimensions(matrix)
        return not (row < 0 or col < 0 or row > rows - 1 or col > cols - 1)

    def GetDimensions(self, matrix):
        return len(matrix), len(matrix[0])

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [["a", "a", "a", "a"],
              ["b", "a", "c", "a"],
              ["b", "a", "c", "a"],
              ["b", "a", "a", "a"]]

    expectedOutput = True
    output = solution.HasCycle(matrix)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    matrix = [["a", "b", "e", "b"],
              ["b", "b", "c", "b"],
              ["b", "c", "c", "d"],
              ["d", "c", "d", "d"]]

    expectedOutput = False
    output = solution.HasCycle(matrix)
    print(output, expectedOutput, output == expectedOutput)
