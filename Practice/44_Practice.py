# Number of islands
# https://neetcode.io/problems/count-number-of-islands

class Solution:
    def isUnknownIsland(self, grid, startRow, startCol, visited):
        rows = len(grid)
        cols = len(grid[0])
        
        pending = [(startRow, startCol)]
        landFound = False

        while pending:
            row, col = pending.pop()

            if grid[row][col] == "0": # Explore current cell
                continue

            if (row, col) in visited:
                continue

            visited.add((row, col))
            landFound = True

            if row > 0:        pending.append((row - 1, col)) # up
            if row < rows - 1: pending.append((row + 1, col)) # down
            if col > 0:        pending.append((row, col - 1)) # left
            if col < cols - 1: pending.append((row, col + 1)) # right

        return landFound

    def numIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands = islands + 1 if self.isUnknownIsland(grid, row, col, visited) else islands

        return islands
    
if __name__ == "__main__":
    solution = Solution()

    grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    expectedOutput = 4
    output = solution.numIslands(grid)
    print(output, expectedOutput, output == expectedOutput)