# Problem:
# You are given a 2D matrix containing only 1s (land) and 0s (water).
#
# An island is a connected set of 1s (land) and is surrounded by either
# an edge or 0s (water). Each cell is considered connected to other cells
# horizontally or vertically (not diagonally).
#
# Two islands are considered the same if and only if they can be translated
# (not rotated or reflected) to equal each other.
#
# Write a function to find the number of distinct islands in the given matrix.
#
# Example:
#
# Input: matrix = [[1, 1, 0, 1, 1],
#                  [1, 1, 0, 1, 1],
#                  [0, 0, 0, 0, 0],
#                  [0, 1, 1, 0, 1],
#                  [0, 1, 1, 0, 1]]
#
# Output: 2

class Solution:
    # Solution:
    # Linearly traverse the matrix looking for land (1s). Once found, use Depth-First Search (DFS)
    # to explore each island, keep track of the directions taken by DFS in every step so the shape
    # of the island can be encoded as a sequence, lets call any of this sequences a signature.
    # 
    # Take for example the signature "SDRU", it encodes a 2x2 square as it implies that DFS would
    # start from position (S), then go down (D), then go right (R) and then go up (U), before finishing
    # exploring.
    # 
    # Store the signatures of all the islands that you find in a set, once the matrix has been fully
    # traversed, return the cardinality (length) of such set. Since sets do not allow for repetition
    # that should be the total number of unique island shapes in the matrix.
    #  
    # Solution complexity:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def FindDistinctIslands(self, matrix):
        rows, cols = self.GetDimensions(matrix)
        
        islandsSignatures = set()
        visited = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and (i, j) not in visited:
                    island = set()
                    signature = []
                    
                    self.ExploreIsland(matrix, i, j, island, signature)

                    visited = visited.union(island)
                    islandsSignatures.add(''.join(signature))

        print(islandsSignatures)
        return len(islandsSignatures)
    
    def GetDimensions(self, matrix):
        return len(matrix), len(matrix[0])
    
    def IsInMatrix(self, matrix, row, col):
        rows, cols = self.GetDimensions(matrix)
        return not (row < 0 or col < 0 or row > rows - 1 or col > cols - 1)
    
    def ExploreIsland(self, matrix, row, col, visited, signature, direction='S'):
        if self.IsInMatrix(matrix, row, col) and matrix[row][col] == 1 and (row, col) not in visited:      
            # Mark the current cell as visited and update the signature
            visited.add((row, col))
            signature.append(direction)

            # Explore UP
            self.ExploreIsland(matrix, row - 1, col, visited, signature, 'U')

            # Explore DOWN
            self.ExploreIsland(matrix, row + 1, col, visited, signature, 'D')

            # Explore LEFT
            self.ExploreIsland(matrix, row, col - 1, visited, signature, 'L')

            # Explore RIGHT
            self.ExploreIsland(matrix, row, col + 1, visited, signature, 'R')


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [[1, 1, 0, 1, 1],
              [1, 1, 0, 1, 1],
              [0, 0, 0, 0, 0],
              [0, 1, 1, 0, 1],
              [0, 1, 1, 0, 1]]

    expectedOutput = 2
    output = solution.FindDistinctIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)

    print()

    # Example 2
    matrix = [[1, 1, 0, 1],
              [0, 1, 1, 0],
              [0, 0, 0, 0],
              [1, 1, 0, 0],
              [0, 1, 1, 0]]

    expectedOutput = 2
    output = solution.FindDistinctIslands(matrix)
    print(output, expectedOutput, output == expectedOutput)
