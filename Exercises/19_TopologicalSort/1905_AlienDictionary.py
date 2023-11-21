# Problem:
# There is a dictionary containing words from an alien language for which we
# don’t know the ordering of the letters. Write a method to find the correct
# order of the letters in the alien language. It is given that the input is a
# valid dictionary and there exists an ordering among its letters.
# 
# Example:
# 
# Input: words: ["ba", "bc", "ac", "cab"]
# Output: ["b", "a", "c"]
# Explanation: Given that the words are sorted lexicographically by the rules
#              of the alien language, so from the given words we can conclude
#              the following ordering among its characters:
# 
#              1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
#              2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
# 
#              From the above two points, we can conclude that the correct character order
#              is: "bac"
#

class Solution():
    # Solution:
    # For each pair of consecutive words, compare the characters in both from left to right
    # until a different char is found. This difference can be interpreted as an edge on a
    # directed graph, such that a node 'v' representing the character from the first word
    # connects to a node 'u' representing the character of the second word. This encodes the
    # fact that 'u' comes after 'v' in our alien lexicographical order. Thus, to get the total
    # order of characters, it would sufice to return the topoligical sort of the nodes representing
    # all of the characters.
    #  
    # Solution complexity:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def FindAlphabetOrder(self, words):
        if not words:
            return ""

        # Initialize graph and in-degree tracker
        graph = {}
        inDegree = {}
        
        for word in words:
            for character in word:
                graph[character] = []
                inDegree[character] = 0

        
        # Populate graph
        for i in range(len(words) - 1):
            # Find ordering of characters from adjacent words
            word1 = words[i]
            word2 = words[i + 1]

            # Compare the characters in both words until a difference is found
            for j in range(min(len(word1), len(word2))):
                u = word1[j]
                v = word2[j]

                # When the first difference between both words is found
                # register it as an edge on the graph, starting from
                # the node corresponding to the char on the first word
                # to that of the char of the second word. Then, update the
                # in-degree tracker and break.
                if u != v:
                    graph[u].append(v)
                    inDegree[v] += 1
                    break 

        # Find source nodes (those with no incoming edges)
        sources = []
        for v in inDegree:
            if inDegree[v] == 0:
                sources.append(v)

        # Sort the characters in the graph in topological order and place them in a list
        sortedCharacters = []
        while sources:
            v = sources.pop(0)
            sortedCharacters.append(v)

            for u in graph[v]:
                inDegree[u] -= 1
                if inDegree[u] == 0:
                    sources.append(u)

        # If there are missing characters from the sorted order, then, there is a cycle in the graph
        # return an empty string if this is the case (unlikely)
        if len(sortedCharacters) != len(graph.keys()):
            return ""

        # Return the sorted characters as a single string
        return "".join(sortedCharacters)

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    words = ["ba", "bc", "ac", "cab"]
    expectedOutput = "bac"
    output = solution.FindAlphabetOrder(words)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    words = ["cab", "aaa", "aab"]
    expectedOutput = "cab"
    output = solution.FindAlphabetOrder(words)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3:
    words = ["ywx", "wz", "xww", "xz", "zyy", "zwz"]
    expectedOutput = "ywxz"
    output = solution.FindAlphabetOrder(words)
    print(output, expectedOutput, output == expectedOutput)
