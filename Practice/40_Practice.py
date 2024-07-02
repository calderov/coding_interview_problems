# Search for Word II
# Solved 
# Given a 2-D grid of characters board and a list of strings words, return
# all words that are present in the grid.
# 
# For a word to be present it must be possible to form the word with a path
# in the board with horizontally or vertically neighboring cells. The same
# cell may not be used more than once in a word.

class TrieNode:
    def __init__(self):
        self.root = self
        self.isWord = False
        self.children = {}

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True

class Solution:
    def findWords(self, board, words):
        def dfsSearch(row, col, board, prefixTree, wordsInBoard, visitedCoords, word=""):
            rows, cols = len(board), len(board[0])

            if row < 0 or col < 0 or row == rows or col == cols or \
               board[row][col] not in prefixTree.children or \
               (row, col) in visitedCoords:
                return

            prefixTree = prefixTree.children[board[row][col]]
            word += board[row][col]

            if prefixTree.isWord:
                wordsInBoard.add(word)

            visitedCoords.add((row, col))
            dfsSearch(row - 1, col, board, prefixTree, wordsInBoard, visitedCoords, word)
            dfsSearch(row + 1, col, board, prefixTree, wordsInBoard, visitedCoords, word)
            dfsSearch(row, col - 1, board, prefixTree, wordsInBoard, visitedCoords, word)
            dfsSearch(row, col + 1, board, prefixTree, wordsInBoard, visitedCoords, word)
            visitedCoords.remove((row, col)) # backtrack

        prefixTree = TrieNode()

        for word in words:
            prefixTree.addWord(word)

        rows = len(board)
        cols = len(board[0])

        wordsInBoard = set()
        visitedCoords = set()

        for row in range(rows):
            for col in range(cols):
                dfsSearch(row, col, board, prefixTree, wordsInBoard, visitedCoords)

        wordsInBoard = list(wordsInBoard)

        return wordsInBoard

if __name__ == "__main__":
    solution = Solution()

    board = [["a","b","c","d"], ["s","a","a","t"], ["a","c","k","e"], ["a","c","d","n"]]
    words = ["bat", "cat", "back", "backend", "stack"]
    expectedOutput = sorted(["cat", "back", "backend"])
    output = sorted(solution.findWords(board, words))
    print(expectedOutput)
    print(output)
    print(expectedOutput == output)







