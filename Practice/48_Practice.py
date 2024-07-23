# Word Ladder (Hard)
# https://neetcode.io/problems/word-ladder

from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:
        def isViableNeighbor(word1, word2):
            d = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    d += 1
                    if d > 1:
                        return False
            return True

        graph = {word:[] for word in wordList}
        graph[beginWord] = []

        for i in range(len(graph)):
            for j in range(i + 1, len(graph)):
                word1 = list(graph.keys())[i]
                word2 = list(graph.keys())[j]

                if isViableNeighbor(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)

        pending = deque([beginWord])
        level = 0
        visited = set()

        while pending:
            level += 1
            nodesInLevel = len(pending)
            for _ in range(nodesInLevel):
                node = pending.popleft()

                if node == endWord:
                    return level

                if node in visited:
                    continue

                visited.add(node)

                for neighbor in graph[node]:
                    if isViableNeighbor(node, neighbor):
                        pending.append(neighbor)

        return 0


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    beginWord="cat"
    endWord="sag"
    wordList=["bat","bag","sag","dag","dot"]
    expectedOutput = 4

    output = solution.ladderLength(beginWord, endWord, wordList)
    print(output, expectedOutput, output == expectedOutput)