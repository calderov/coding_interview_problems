# N-Queens II
# HARD
# https://scaleengineer.com/dsa/problems/n-queens-ii

# Description
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example 1:
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# □ ♔ □ ■
# ■ □ ■ ♔
# ♔ ■ □ ■
# ■ □ ♔ □

# □ ■ ♔ ■
# ♔ □ ■ □
# □ ■ □ ♔
# ■ ♔ ■ □

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
#     1 <= n <= 9

class Solution:

    def __init__(self):
        self.n = 0
        self.count = 0
        self.queens = []

    def totalNQueens(self, n):
        self.n = n
        self.count = 0
        self.queens = []
        self.backtrack(0)
        return self.count
    
    def IsValid(self, n, queens):
        # Verify rows and cols
        seenRows = set()
        seenCols = set()
        for row, col in queens:
            if row in seenRows or col in seenCols:
                return False
            seenRows.add(row)
            seenCols.add(col)

        # Verify diagonals for each queen
        for queenRow, queenCol in queens:
            # Verify top-left
            row = queenRow - 1
            col = queenCol - 1
            while row >= 0 and col >= 0:
                if (row, col) in queens:
                    return False
                row -= 1
                col -= 1

            # Verify top-right
            row = queenRow - 1
            col = queenCol + 1
            while row >= 0 and col < n:
                if (row, col) in queens:
                    return False
                row -= 1
                col += 1

            # Verify bottom-left
            row = queenRow + 1
            col = queenCol - 1
            while row < n and col >= 0:
                if (row, col) in queens:
                    return False
                row += 1
                col -= 1
                        
            # Verify bottom-right
            row = queenRow + 1
            col = queenCol + 1
            while row < n and col < n:
                if (row, col) in queens:
                    return False
                row += 1
                col += 1

        return True

    def backtrack(self, row):
        if row == self.n and self.IsValid(self.n, self.queens):
            self.count += 1
            print(self.queens)
            return

        for col in range(self.n):
            if not self.IsValid(self.n, self.queens):
                continue

            # Place queen
            self.queens.append((row, col))

            # Recurse for the next row
            self.backtrack(row + 1)

            # Backtrack (remove queen)
            self.queens.pop()
        
        return
    
app = Solution()
print(app.totalNQueens(4))
