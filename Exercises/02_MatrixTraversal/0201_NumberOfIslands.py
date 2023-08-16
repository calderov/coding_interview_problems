# Problem:
# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
# count the number of islands in it.
# 
# An island is a connected set of 1s (land) and is surrounded by either an edge
# or 0s (water). Each cell is considered connected to other cells horizontally
# or vertically (not diagonally).
#
# For example, the following matrix contains only 1 island:
#
# matrix = [[0, 1, 1, 1, 0],
#           [0, 0, 0, 1, 1],
#           [0, 1, 1, 1, 0],
#           [0, 1, 1, 0, 0],
#           [0, 0, 0, 0, 0]]
#
# This can be appreciated better if we render the matrix
# using ascii squares instead of 1s and 0s.
# 
# Then, the matrix becomes:
#
# matrix =  |▒ █ █ █ ▒|
#           |▒ ▒ ▒ █ █|
#           |▒ █ █ █ ▒|
#           |▒ █ █ ▒ ▒|
#           |▒ ▒ ▒ ▒ ▒|
#  

class Solution:
    # Solution:
    # Create an empty array named 'visited' to keep the track of all the
    # pieces of land (1s) present in the matrix. Each coordinate must be 
    # represented by a tuple (row, col). Also, initialize an island counter
    # to zero, to keep track of all the islands we'll discover later on.
    # 
    # Then, traverse the island linearly looking for 1s. If a 1 is found, 
    # check if its coordinates have already been visited. If not, it 
    # means that a new island has been found, add 1 to the island counter
    # and use Breadth-First Search (BFS) to explore the island, then add
    # all the explored coordinates to the 'visited' array. Once the
    # matrix has been traversed all of the islands should have been
    # explored. Return the island counter now. 

    # Solution complexity:
    # Time complexity: O(m * n) as this is the complexity of the underlying BFS step.
    # Space complexity: O(m * n)
    def NumberOfIslands(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        visited = []
        islands = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] and (i, j) not in visited:
                    visited += self.ExploreIsland(matrix, i, j)
                    islands += 1

        return islands

    def ExploreIsland(self, matrix, row, col):
        visited = []
        pending = [(row, col)]

        while pending:
            i, j = pending.pop()
            visited.append((i, j))

            up = self.GetUp(matrix, i, j)
            if up and up not in visited:
                pending.append(up)

            down = self.GetDown(matrix, i, j)
            if down and down not in visited:
                pending.append(down)

            left = self.GetLeft(matrix, i, j)
            if left and left not in visited:
                pending.append(left)

            right = self.GetRight(matrix, i, j)
            if right and right not in visited:
                pending.append(right)

        return visited

    def GetUp(self, matrix, i, j):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Return early on invalid input
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return None
        
        # If the current position is already at the top, there is no up
        if i == 0:
            return None
        
        # If there is a something up (besides zero) return its coordinates
        if matrix[i - 1][j]:
            return (i - 1, j)
        
        return None

    def GetDown(self, matrix, i, j):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Return early on invalid input
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return None
        
        # If the current position is already at the bottom, there is no down
        if i == rows - 1:
            return None
        
        # If there is a something down (besides zero) return its coordinates
        if matrix[i + 1][j]:
            return (i + 1, j)
        
        return None

    def GetRight(self, matrix, i, j):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Return early on invalid input
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return None
        
        # If the current position is already at the rightmost position, there is no right
        if j == cols - 1:
            return None
        
        # If there is a something right (besides zero) return its coordinates
        if matrix[i][j + 1]:
            return (i, j + 1)
        
        return None

    def GetLeft(self, matrix, i, j):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Return early on invalid input
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return None
        
        # If the current position is already at the leftmost position, there is no left
        if j == 0:
            return None
        
        # If there is a something left (besides zero) return its coordinates
        if matrix[i][j - 1]:
            return (i, j - 1)
        
        return None

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [[0, 1, 1, 1, 0],
              [0, 0, 0, 1, 1],
              [0, 1, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0]]
    expectedOutput = 1
    output = solution.NumberOfIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    matrix = [[1, 1, 1, 0, 0],
              [0, 1, 0, 0, 1],
              [0, 0, 1, 1, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0]]
    expectedOutput = 3
    output = solution.NumberOfIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)