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

class Solution:
    def IsWordInBoard(self, word, board):
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                if self.Backtrack(board, row, col, set(), "", word):
                    return True
        
        return False

    def Backtrack(self, board, row, col, visited, currentWord, targetWord):
        rows = len(board)
        cols = len(board[0])

        if row < 0 or col < 0 or row >= rows or col >= cols:
            return False

        if (row, col) in visited:
            return False
        
        visited.add((row, col))
        currentWord += board[row][col]

        if currentWord == targetWord:
            return True
        
        result = self.Backtrack(board, row - 1, col, visited, currentWord, targetWord) # up
        result = result or self.Backtrack(board, row + 1, col, visited, currentWord, targetWord) # down
        result = result or self.Backtrack(board, row, col - 1, visited, currentWord, targetWord) # left
        result = result or self.Backtrack(board, row, col + 1, visited, currentWord, targetWord) # right

        visited.remove((row, col))

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