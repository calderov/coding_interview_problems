# Problem:
# Given an m x n grid of characters board and a string word, return true if
# the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Examples:
#
#   word = "ABCCED"
#   board = [['A', 'B', 'C', 'E'],
#            ['S', 'F', 'C', 'S'],
#            ['A', 'D', 'E', 'E']]
#   expectedOutput = True
#   
#   word = "SEE"
#   board = [['A', 'B', 'C', 'E'],
#            ['S', 'F', 'C', 'S'],
#            ['A', 'D', 'E', 'E']]
#   expectedOutput = True

# Solution:
# Use a modified version of DFS to traverse the board looking for the characters in the given word.
# Thus, this DFS will run from all the cells of the board, as deep as the lenght of the given word.
# 
# To avoid keeping an expensive set of visited cells, we can mark the board as we move forward, and
# unmark it as we backtrack.
# 
# Solution complexity:
# Time complexity: O(4 ^ n) where n is the number of cells in the board
# Space complexity: O(n)
class Solution:
    def IsWordInBoard(self, word, board):
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if self.Backtrack(board, row, col, word, 0):
                    return True
        
        return False

    def Backtrack(self, board, row, col, targetWord, depth):
        # If the current cell is off-limits return False
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False

        # If the value at the current cell doesn't match our expected value, return False
        if board[row][col] != targetWord[depth]:
            return False

        # If the we have reached the end of the target word, return True
        if depth == len(targetWord) - 1:
            return True
        
        # Mark the current cell with a '#' and save its value
        old, board[row][col] = board[row][col], "#"

        # Recursively explore the adjacent cells (up, down, left, right)
        result = self.Backtrack(board, row - 1, col, targetWord, depth + 1) or \
                 self.Backtrack(board, row + 1, col, targetWord, depth + 1) or \
                 self.Backtrack(board, row, col - 1, targetWord, depth + 1) or \
                 self.Backtrack(board, row, col + 1, targetWord, depth + 1) 

        # Backtrack by restoring the original value of the current cell
        board[row][col] = old

        # Return the computed result
        return result

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    word = "ABCCED"
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    expectedOutput = True
    output = solution.IsWordInBoard(word, board)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    word = "SEE"
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    expectedOutput = True
    output = solution.IsWordInBoard(word, board)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    word = "zabcd"
    board = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y'], ['z', 'a', 'b', 'c', 'd']]
    expectedOutput = True
    output = solution.IsWordInBoard(word, board)
    print(output, expectedOutput, output == expectedOutput)