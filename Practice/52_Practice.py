from collections import deque

class Solution:
    def dfsLength(self, graph, node, labels, result):
        longest = 0
        second_longest = 0

        for neighbor in graph[node]:
            neighbor_branch = self.dfsLength(graph, neighbor, labels, result)

            if labels[neighbor] != labels[node]:
                if neighbor_branch == longest:
                    second_longest = neighbor_branch
                    continue

                if neighbor_branch > longest:
                    second_longest = longest
                    longest = neighbor_branch
                    continue

                if neighbor_branch > second_longest:
                    second_longest = neighbor_branch
                    continue

        result[0] = max(result[0], 1 + longest + second_longest)

        return longest + 1

    # Time complexity: 
    # Space complexity: 
    def longestPath(self, parents, labels):
        graph = {i:set() for i in range(len(parents))}
        
        for i in range(1, len(parents)):
            graph[parents[i]].add(i)
        
        result = [0]
        self.dfsLength(graph, 0, labels, result)

        return result[0]
        
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    parents = [-1,0,0,1,1,2]
    labels = "abacbe"
    expectedOutput = 3
    output = solution.longestPath(parents, labels)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    parents = [-1,0,0,0]
    labels = "aabc"
    expectedOutput = 3
    output = solution.longestPath(parents, labels)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    parents = [-1,0,1,2]
    labels = "aabb"
    expectedOutput = 2
    output = solution.longestPath(parents, labels)
    print(output, expectedOutput, output == expectedOutput)