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

# Time: O(m * n)
# Space: O(m * n) due to memo
def MinPathSumMemo(grid):
    rows = len(grid)
    cols = len(grid[0])
    memo = [[float("inf")] * cols for _ in range(rows)]

    pending = [(0,0,0)]
    while pending:
        row, col, cost = pending.pop()

        cost += grid[row][col]
        memo[row][col] = min(memo[row][col], cost)

        if row < rows - 1 and memo[row][col] < memo[row + 1][col]:
            pending.append((row + 1, col, cost))
        
        if col < cols - 1 and memo[row][col] < memo[row][col + 1]:
            pending.append((row, col + 1, cost))

    return memo[rows - 1][cols - 1]

# Time: O(m * n)
# Space: O(1)
def MinPathSumInPlaceDP(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Initialize first row
    for col in range(1, cols):
        grid[0][col] += grid[0][col - 1]

    # Initialize first column
    for row in range(1, rows):
        grid[row][0] += grid[row - 1][col]

    for row in range(1, rows):
        for col in range(1, cols):
            grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])

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
