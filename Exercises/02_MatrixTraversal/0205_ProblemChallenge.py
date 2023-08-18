# Problem:
# You are given a 2D matrix containing only 1s (land) and 0s (water).
# An island is a connected set of 1s (land) and is surrounded by either
# an edge or 0s (water). Each cell is considered connected to other cells
# horizontally or vertically (not diagonally).
#
# There are no lakes on the island, so the water inside the island is not
# connected to the water around it. A cell is a square with a side length
# of 1.
#
# The given matrix has only one island, write a function to find the perimeter
# of that island.

# Example:
# Input: matrix = [[1, 1, 0, 0, 0],
#                  [0, 1, 0, 0, 0],
#                  [0, 1, 0, 0, 0],
#                  [0, 1, 1, 0, 0],
#                  [0, 0, 0, 0, 0]]
# 
# Output: 14
# Explanation: The boundary of the island constitutes 14 sides.

class Solution:
    # Solution:
    # Initialize a perimeter variable to zero.
    # 
    # Traverse the matrix looking for land (1s), every time a cell of land
    # is found, add 4 to the total perimeter and substract the number of
    # neighboring cells with land, as the net contribution of a land-locked
    # cell is zero.
    # 
    # Once the matrix is completely traversed, return the perimeter.
    #
    # This approach exploits the fact that the given matrices will only contain
    # one island.
    #
    # NOTE: This solution did not pass the following test case provided by
    #       Design Gurus
    #       
    #       matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0],
    #                 [1, 0, 1, 0, 1, 0, 1, 0, 1],
    #                 [0, 1, 0, 1, 0, 1, 0, 1, 0]]
    # 
    #       In my opinion this case doesn't follow the restrictions stated
    #       in the problem description. However, I've decided to leave this
    #       solution as valid.
    #
    # Solution complexity:
    # Time complexity: O(m * n) as the whole matrix has to be traversed
    # Space complexity: O(1)
    def GetIslandPerimeterV1(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        perimeter = 0

        for i in range (rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    perimeter += 4 - len(self.GetNeighbors(matrix, i, j))

        return perimeter
    
    # Solution:
    # Initialize a perimeter variable to zero and find the location of the first
    # piece of land in the matrix. Save it to a variable called 'start'.
    # 
    # Use Breadth-First Search (BFS) to explore the island from the 'start'.
    # Updating the perimeter as follows everytime a new cell is visited:
    # 
    #     perimeter = perimeter + 4 - len(neighbors)
    # 
    # Here, 'neighbors' is the set of cells of land that are adjacent to the
    # current cell. Thus, this step is adding to the amount of adjacent sea
    # cells to the perimeter.
    #
    # Once the matrix is completely traversed, return the perimeter.
    #
    # Solution complexity:
    # Time complexity: O(m * n) as that is the complexity of the underlying BFS step.
    # Space complexity: O(m * n)
    def GetIslandPerimeterV2(self, matrix):
        start = self.FindIsland(matrix)

        # Return early if there is no island in the matrix
        if not start:
            return  0

        perimeter = 0
        visited = set()
        pending = set([start])

        while pending:
            i, j = pending.pop()
            visited.add((i, j))

            neighbors = self.GetNeighbors(matrix, i, j)
            pending = pending.union(neighbors).difference(visited)
            perimeter += 4 - len(neighbors)

        return perimeter
    
    def FindIsland(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    return (i, j)

        return None

    def GetNeighbors(self, matrix, row, col):
        neighbors = set()
        if self.IsInMatrix(matrix, row - 1, col) and matrix[row - 1][col] == 1:
            neighbors.add((row - 1, col))
        if self.IsInMatrix(matrix, row + 1, col) and matrix[row + 1][col] == 1:
            neighbors.add((row + 1, col))
        if self.IsInMatrix(matrix, row, col - 1) and matrix[row][col - 1] == 1:
            neighbors.add((row, col - 1))
        if self.IsInMatrix(matrix, row, col + 1) and matrix[row][col + 1] == 1:
            neighbors.add((row, col + 1))
        return neighbors

    def IsInMatrix(self, matrix, row, col):
        rows = len(matrix)
        cols = len(matrix[0])
        return not (row < 0 or col < 0 or row > rows - 1 or col > cols - 1)
    
    def GetIslandPerimeter(self, matrix):
        return self.GetIslandPerimeterV2(matrix)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [[1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0]]
    
    expectedOutput = 14
    output = solution.GetIslandPerimeter(matrix)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    matrix = [[0, 1, 0, 1, 0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1, 0, 1, 0, 1],
              [0, 1, 0, 1, 0, 1, 0, 1, 0]]

    expectedOutput = 4
    output = solution.GetIslandPerimeter(matrix)
    print(output, expectedOutput, output == expectedOutput)