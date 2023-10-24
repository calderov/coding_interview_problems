# Problem: 
# Given a square binary matrix representing an image, we want to flip the
# image horizontally, then invert it.
# 
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].
# 
# To invert an image means that each 0 is replaced by 1, and each 1 is
# replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].
# 
# Example:
# 
#   Input:  [[1,0,1],
#            [1,1,1],
#            [0,1,1]]
# 
#   Output: [[0,1,0],
#            [0,0,0],
#            [0,0,1]]
# 
#   Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then,
#                invert the image: [[0,1,0],[0,0,0],[0,0,1]]
# 

import copy

class Solution:
    # Solution:
    # 1. Initialize an empty list to store our result.
    #    result = []
    #
    # 2. Invert and add each row on the original matrix to the result matrix.
    #
    # 3. Traverse each cell in the result matrix and invert it by XORing its value with 1.
    #
    # 4. Return the result matrix and finish.
    #
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def FlipAndInvert(self, matrix):
        result = []

        # Flip
        for row in matrix:
            result.append(list(reversed(row)))

        # Invert
        rows = len(result)
        cols = len(result[0])

        for i in range(rows):
            for j in range(cols):
                result[i][j] = result[i][j] ^ 1

        return result

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [[1,0,1],
             [1,1,1],
             [0,1,1]]

    expectedOutput = [[0,1,0],
                      [0,0,0],
                      [0,0,1]]
    
    output = solution.FlipAndInvert(matrix)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    matrix = [[1,1,0,0],
             [1,0,0,1],
             [0,1,1,1], 
             [1,0,1,0]]

    expectedOutput = [[1,1,0,0],
                      [0,1,1,0],
                      [0,0,0,1],
                      [1,0,1,0]]

    output = solution.FlipAndInvert(matrix)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()