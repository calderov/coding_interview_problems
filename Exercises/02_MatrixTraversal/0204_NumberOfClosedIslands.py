# Problem:
# You are given a 2D matrix containing only 1s (land) and 0s (water).
# An island is a connected set of 1s (land) and is surrounded by either
# an edge or 0s (water). Each cell is considered connected to other cells
# horizontally or vertically (not diagonally).
#
# A closed island is an island that is totally surrounded by 0s (i.e., water).
# This means all horizontally and vertically connected cells of a closed island
# are water. This also means that, by definition, a closed island can't touch
# an edge (as then the edge cells are not connected to any water cell).
#
# Write a function to find the number of closed islands in the given matrix.
#
# Example:
#
# Input: matrix = [[1, 1, 0, 0, 0],
#                  [0, 1, 0, 0, 0],
#                  [0, 0, 1, 1, 0],
#                  [0, 1, 1, 0, 0],
#                  [0, 0, 0, 0, 0]]
# Output: 1

class Solution:
    # Solution:
    # Create an empty array named 'visited' to keep track of the all the cells
    # in the matrix that represent land (1s). Each cell is a coordinate that
    # must be represented by a tuple (row, col). Then, initialize a variable
    # named closedIslandsCount to zero, it will count how many different
    # closed islands have been found at any point of the algorithm's execution.
    # 
    # Then, traverse the island linearly looking for 1s. If a 1 is found, 
    # check if its cell has already been visited. If not, it means that a new
    # island has been found, use Breadth-First Search (BFS) to explore the 
    # rest of the island, make this BFS process return the set of visited
    # cells that constitute the island, and if the island is closed or not.
    # An island is closed if none of its cells are on the edges of the matrix.
    # 
    # If a discovered island is closed, add 1 to the closedIslandsCount variable.
    #
    # Once the matrix has been completely traversed, all of the islands should 
    # have been and explored and the number of closed islands should be stored
    # in closedIslandsCount. Return closedIslandsCount and exit.
    #
    # Solution complexity:
    # Time complexity: O(m * n) as this is the complexity of the underlying BFS step.
    # Space complexity: O(m * n)
    def CountClosedIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        visited = set()
        closedIslandsCount = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and (i, j) not in visited:
                    island, isClosed = self.ExploreIsland(matrix, i, j)
                    visited = visited.union(island)
                    if isClosed:
                        closedIslandsCount += 1
    
        return closedIslandsCount
    
    def ExploreIsland(self, matrix, row, col):
        isClosed = True
        visited = set()
        pending = set([(row, col)])

        while pending:
            i, j = pending.pop()
            visited.add((i, j))
            isClosed = isClosed and not self.IsEdge(matrix, i, j)

            directions = [
                self.GetUp(matrix, i, j),
                self.GetDown(matrix, i, j),
                self.GetLeft(matrix, i, j),
                self.GetRight(matrix, i, j)
            ]

            for direction in directions:
                if direction and direction not in visited:
                    pending.add(direction)

        return visited, isClosed 
    
    def GetUp(self, matrix, i, j):
        if self.IsInMatrix(matrix, i - 1, j) and matrix[i - 1][j] == 1:
            return (i - 1, j)
        return None

    def GetDown(self, matrix, i, j):
        if self.IsInMatrix(matrix, i + 1, j) and matrix[i + 1][j] == 1:
            return (i + 1, j)
        return None
    
    def GetLeft(self, matrix, i, j):
        if self.IsInMatrix(matrix, i, j - 1) and matrix[i][j - 1] == 1:
            return (i, j - 1)
        return None

    def GetRight(self, matrix, i, j):
        if self.IsInMatrix(matrix, i, j + 1) and matrix[i][j + 1] == 1:
            return (i, j + 1)
        return None

    def IsEdge(self, matrix, i, j):
        rows = len(matrix)
        cols = len(matrix[0])
        return i == 0 or j == 0 or i == rows - 1 or j == cols - 1
    
    def IsInMatrix(self, matrix, row, col):
        rows = len(matrix)
        cols = len(matrix[0])
        return not (row < 0 or col < 0 or row > rows - 1 or col > cols - 1)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [[1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0]]

    expectedOutput = 1
    output = solution.CountClosedIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    matrix = [[0, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 0]]

    expectedOutput = 2
    output = solution.CountClosedIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    matrix = [[1, 0, 1, 0, 1],
              [0, 0, 0, 0, 0],
              [1, 0, 1, 0, 1]]

    expectedOutput = 0
    output = solution.CountClosedIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)

    matrix = [[1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0],
              [0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0]]
    expectedOutput = 1
    output = solution.CountClosedIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)
