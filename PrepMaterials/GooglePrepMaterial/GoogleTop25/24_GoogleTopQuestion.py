# Minimum Path Sum
# MEDIUM

# Description
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example 1:
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 200
#     0 <= grid[i][j] <= 200

# Time: O(2 ** (m * n))
# Space: O(m + n)
def MinPathSumRecursive(grid, row=0, col=0):
    rows = len(grid)
    cols = len(grid[0])

    if row == rows - 1 and col == cols - 1:
        return grid[row][col]

    bottom = MinPathSumRecursive(grid, row + 1, col) if row + 1 < rows else float("inf")
    right =  MinPathSumRecursive(grid, row, col + 1) if col + 1 < cols else float("inf")

    return grid[row][col] + min(bottom, right)

# Time: O(m * n)
# Space: O(m * n) due to memo
def MinPathSumMemoized(grid):
    rows = len(grid)
    cols = len(grid[0])

    memo = [[-1] * cols for _ in range(rows)]

    def compute(row, col):
        nonlocal rows
        nonlocal cols
        nonlocal grid
        nonlocal memo

        if row == rows - 1 and col == cols - 1:
            return grid[row][col]
        
        if memo[row][col] != -1:
            return memo[row][col]
        
        bottom = compute(row + 1, col) if row + 1 < rows else float("inf")
        right = compute(row, col + 1) if col + 1 < cols else float("inf")
        
        memo[row][col] = grid[row][col] + min(bottom, right)
        return memo[row][col]

    return compute(0, 0)

# Time: O(m * n)
# Space: O(1)
def MinPathSumInPlaceDP(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Update first row
    for col in range(1, cols):
        grid[0][col] += grid[0][col - 1]

    # Update first col
    for row in range(1, rows):
        grid[row][0] += grid[row - 1][0]

    # Update the rest of the grid
    for row in range(1, rows):
        for col in range(1, cols):
            grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

    return grid[rows - 1][cols - 1]

def MinPathSum(grid):
    return MinPathSumInPlaceDP(grid)

if __name__ == "__main__":
    # Example 1:
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    expected = 7
    output = MinPathSum(grid)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    grid = [[1,2,3],[4,5,6]]
    expected = 12
    output = MinPathSum(grid)
    print(expected)
    print(output)
    print(expected == output)
    print()
