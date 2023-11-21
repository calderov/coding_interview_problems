# Problem:
# Given a sequence originalSeq and an array of sequences, write a method to
# find if originalSeq can be uniquely reconstructed from the array of
# sequences.
# 
# Unique reconstruction means that we need to find if originalSeq is the only
# sequence such that all sequences in the array are subsequences of it.
# 
# Examples:
# 
#   Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
#   Output: true
#   Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely
#                reconstruct [1, 2, 3, 4], in other words, all the given
#                sequences uniquely define the order of numbers in the
#                'originalSeq'.
#
#   Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
#   Output: false
#   Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely
#                reconstruct [1, 2, 3, 4]. There are two possible sequences
#                we can construct from the given sequences:
#                  1) [1, 2, 3, 4]
#                  2) [1, 2, 4, 3]
#

class Solution:
    # Solution:
    # Build a graph connecting all the numbers as they appear in the candidate subsequences
    # and compute the topoligical order of this graph. If this topological order matches
    # the target sequence, and at no poit we saw more than two simultaneous sources (nodes
    # with 0 incident edges), then the subsequences can uniquely construct the target sequence.
    # 
    # Solution complexity:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def CanSequenceBeConstructedBySubsequences(self, sequence, subsequences):
        # Initialize graph and in-degree tracker
        graph = {}
        inDegree = {}

        for subsequence in subsequences:
            for v in subsequence:
                graph[v] = []
                inDegree[v] = 0

        # Populate graph and in-degree tracker
        for subsequence in subsequences:
            for i in range(len(subsequence) - 1):
                v = subsequence[i]
                u = subsequence[i + 1]

                graph[v].append(u)
                inDegree[u] += 1

        # Find sources
        sources = []
        for v in inDegree:
            if inDegree[v] == 0:
                sources.append(v)

        # Compute topological sort
        sortedNums = []
        while sources:
            # If is more than one source, there is more than one way to reconstruct the sequence
            if len(sources) > 1:
                return False
            
            v = sources.pop(0)
            sortedNums.append(v)
            for u in graph[v]:
                inDegree[u] -= 1
                if inDegree[u] == 0:
                    sources.append(u)

        return sortedNums == sequence

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    sequence = [1, 2, 3, 4]
    subsequences = [[1, 2], [2, 3], [3, 4]]
    expectedOutput = True
    output = solution.CanSequenceBeConstructedBySubsequences(sequence, subsequences)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    sequence = [1, 2, 3, 4]
    subsequences = [[1, 2], [2, 3], [2, 4]]
    expectedOutput = False
    output = solution.CanSequenceBeConstructedBySubsequences(sequence, subsequences)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3:
    sequence = [3, 1, 4, 2, 5]
    subsequences = [[3, 1, 5], [1, 4, 2, 5]]
    expectedOutput = True
    output = solution.CanSequenceBeConstructedBySubsequences(sequence, subsequences)
    print(output, expectedOutput, output == expectedOutput)
