# Rotting Oranges
# https://neetcode.io/problems/rotting-fruit

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        fruitFound = False
        pending = deque()
        t = -1

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    fruitFound = True

                if grid[row][col] == 2: # rotten
                    grid[row][col] = 1
                    pending.append((row, col))

        if not fruitFound:
            return 0

        while pending:
            t += 1
            n = len(pending) # cells due for rotting at this time t
            for _ in range(n):
                row, col = pending.popleft()

                # if empty or rotten
                if grid[row][col] == 0 or grid[row][col] == 2:
                    continue

                # mark current cell as rotten
                grid[row][col] = 2

                # up
                if row > 0 and grid[row - 1][col] == 1:
                    pending.append((row - 1, col))
                
                # down
                if row < rows - 1 and grid[row + 1][col] == 1:
                    pending.append((row + 1, col))
                
                # left
                if col > 0 and grid[row][col - 1] == 1:
                    pending.append((row, col - 1))
                
                # right
                if col < cols - 1 and grid[row][col + 1] == 1:
                    pending.append((row, col + 1))

            print(f"t = {t}")
            self.printGrid(grid)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return t

    def printGrid(self, grid):
        for row in grid:
            print(row)
        print()

if __name__ == "__main__":
    solution = Solution()

    grid = [[1,1,0],[0,1,1],[0,1,2]]
    expectedOutput = 4
    output = solution.orangesRotting(grid)

    print(output, expectedOutput, output == expectedOutput)
    