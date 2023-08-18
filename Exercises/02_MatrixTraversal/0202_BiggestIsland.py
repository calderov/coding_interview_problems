# Problem:
# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water),
# find the biggest island in it. Write a function to return the area of the 
# biggest island. 
#
# An island is a connected set of 1s (land) and is surrounded by either an edge
# or 0s (water). Each cell is considered connected to other cells horizontally
# or vertically (not diagonally).
#
# Example:
# Take this matrix for example , it has three islands. The biggest island has 5 cells
# thus the expected ouput of the function is 5.
#
# matrix = [[1, 1, 1, 0, 0],
#           [0, 1, 0, 0, 1],
#           [0, 0, 1, 1, 0],
#           [0, 1, 1, 0, 0],
#           [0, 0, 1, 0, 0]]
#
# This is easier to see if we represent the matrix using ASCII squares
#
# matrix =  |█ █ █ ▒ ▒|
#           |▒ █ ▒ ▒ █|
#           |▒ ▒ █ █ ▒|
#           |▒ █ █ ▒ ▒|
#           |▒ ▒ █ ▒ ▒|

class Solution:
    # Solution:
    # Create an empty array named 'visited' to keep track of the coordinates
    # for all the pieces of land (1s) present in the matrix. Each coordinate
    # must be represented by a tuple (row, col). Then, initialize a variable
    # named bigestIslandArea to store the area of the largest island found at
    # any point of the algorithm's execution, have it initialized to zero.
    # 
    # Then, traverse the island linearly looking for 1s. If a 1 is found, 
    # check if its coordinates have already been visited. If not, it 
    # means that a new island has been found, use Breadth-First Search (BFS)
    # to explore the island, make this BFS process return the set of different
    # coordinates that were visited by it. The size of this set is the area of
    # the current island. Compare this area with bigestIslandArea and update
    # bigestIslandArea if needed.
    # 
    # Once the matrix has been completely traversed, all of the islands should 
    # have been and explored and bigestIslandArea should contain the area of the
    # largest one. Return bigestIslandArea.
    #
    # Solution complexity:
    # Time complexity: O(m * n) as this is the complexity of the underlying BFS step.
    # Space complexity: O(m * n)
    def BiggestIsland(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        visited = set()
        biggestIslandArea = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] and (i, j) not in visited:
                    island = self.ExploreIsland(matrix, i, j)
                    visited = visited.union(island)
                    if len(island) > biggestIslandArea:
                        biggestIslandArea = len(island)

        return biggestIslandArea
    
    def ExploreIsland(self, matrix, row, col):
        visited = set()
        pending = set([(row, col)])

        while pending:
            i, j = pending.pop()
            visited.add((i, j))

            up = self.GetUp(matrix, i, j)
            if up and up not in visited:
                pending.add(up)

            down = self.GetDown(matrix, i, j)
            if down and down not in visited:
                pending.add(down)

            left = self.GetLeft(matrix, i, j)
            if left and left not in visited:
                pending.add(left)

            right = self.GetRight(matrix, i, j)
            if right and right not in visited:
                pending.add(right)

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
    
    def GetRight(self, matrix, i, j):
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Return early on invalid input
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return None
        
        # If the current position is already at the rightmost position, there is no right
        if j == cols - 1:
            return None
        
        # If there is a something left (besides zero) return its coordinates
        if matrix[i][j + 1]:
            return (i, j + 1)

        return None


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [[1, 1, 1, 0, 0],
              [0, 1, 0, 0, 1],
              [0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 1, 0, 0]]
    expectedOutput = 5
    output = solution.BiggestIsland(matrix)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    matrix = [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]]
    expectedOutput = 25
    output = solution.BiggestIsland(matrix)
    print(output, expectedOutput, output == expectedOutput)