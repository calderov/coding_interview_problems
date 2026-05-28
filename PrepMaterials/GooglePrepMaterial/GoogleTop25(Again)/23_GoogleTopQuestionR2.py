# Spiral Matrix II
# MEDIUM
# https://scaleengineer.com/dsa/problems/spiral-matrix-ii

# Description
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n**2 in spiral order.

# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
#  1 <= n <= 20

# Time: O(n ** 2)
# Space: O(1) excluding the output matrix
def SpiralMatrix(n):
    if n == 1:
        return [[1]]

    M = [[0] * n for _ in range(n)]
    
    val = 1
    row = 0
    col = 0

    while val <= n ** 2:
        # Move right
        while col < n and M[row][col] == 0:
            M[row][col] = val
            val += 1
            col += 1
        col -= 1
        row += 1

        # Move down
        while row < n and M[row][col] == 0:
            M[row][col] = val
            val += 1
            row += 1
        col -= 1
        row -= 1

        # Move left
        while col >= 0 and M[row][col] == 0:
            M[row][col] = val
            val += 1
            col -= 1
        col += 1
        row -= 1

        # Move up
        while row >= 0 and M[row][col] == 0:
            M[row][col] = val
            val += 1
            row -= 1
        col += 1
        row += 1

    return M

def PrintMatrix(M):
    for row in M:
        print(row)
    
if __name__ == "__main__":
    # Example 1:
    n = 1
    expected = [[1]]
    output = SpiralMatrix(n)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    n = 2
    expected = [[1, 2], [4, 3]]
    output = SpiralMatrix(n)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    n = 3
    expected = [[1,2,3],[8,9,4],[7,6,5]]
    output = SpiralMatrix(n)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4:
    n = 4
    expected = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    output = SpiralMatrix(n)
    print(expected)
    print(output)
    print(expected == output)
    print()
    
    # Example 5:
    n = 5
    expected = [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
    output = SpiralMatrix(n)
    print(expected)
    print(output)
    print(expected == output)
    print()
