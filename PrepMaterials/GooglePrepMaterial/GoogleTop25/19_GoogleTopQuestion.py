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
# {(0, 1), (2, 0), (3, 2), (1, 3)}

# □ ■ ♔ ■
# ♔ □ ■ □
# □ ■ □ ♔
# ■ ♔ ■ □
# {(3, 1), (2, 3), (0, 2), (1, 0)}

# Example 2:
# Input: n = 1
# Output: 1

# Constraints:
#     1 <= n <= 9

class Solution:
    def __init__(self):
        self.n = 0
        self.count = 0
        self.queens = set()

    # Time: O(n!)
    # Space: O(n)
    def totalNQueens(self, n):
        self.n = n
        self.count = 0
        self.queens = set()
        self.backtrack(0)
        return self.count

    def backtrack(self, row):
        if row == self.n:
            self.count += 1
            # print(self.queens)
            return

        for col in range(self.n):
            # Place queen
            self.queens.add((row, col))

            # Recurse for the next row
            if self.IsValid(self.queens):
                self.backtrack(row + 1)

            # Backtrack (remove queen)
            self.queens.remove((row, col))
        
        return

    # Time: O(n) where n is the number of queens
    # Space: O(n) where n is the number of queens
    def IsValid(self, queens):
        cols = set()
        diag1 = set()
        diag2 = set()

        for row, col in queens:
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                return False
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
    
        return True
   
if __name__=="__main__":
    app = Solution()
    
    # Example 1:
    n = 4
    expected = 2
    output = app.totalNQueens(n)
    print(expected)
    print(output)
    print(expected == output)
    print()
    
    # Example 2:
    n = 1
    expected = 1
    output = app.totalNQueens(n)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    n = 5
    expected = 10
    output = app.totalNQueens(n)
    print(expected)
    print(output)
    print(expected == output)
    print()