# Problem:
# Given an array of words (strings) and two different strings word1 and word2,
# return the shortest distance between these two words in the list.

class Solution:
    # Solution:
    # Declare two pointers to keep track of the positions of word1 and word2 in the array.
    # Lets call them word1Index and word2Index. Lets also declare a variable named minDistance
    # to keep track of the minimum distance between the words found so far.
    #
    # Traverse the array and update the two pointers any time either word1 or word2 is found.
    # If both words have been found compute the distance between them as the abs(word1Index - word2Index)
    # and compare it with the current value of minDistance. If the distance is smaller than
    # the current minDistance, update it.
    #
    # In the end, minDistance should contain the minimum
    # distance between word1 and word2 in the array. Return it! 
    #
    # Solution complexity:
    # Time complexity: O(n) linear time.
    # Space complexity: O(1) constant.
    def ShortestWordDistance(self, words, word1, word2):
        n = len(words)
        word1Index = -1
        word2Index = -1
        minDistance = n

        for i in range(n):
            if words[i] == word1:
                word1Index = i

            if words[i] == word2:
                word2Index = i

            if word1Index > -1 and word2Index > -1:
                distance = abs(word1Index - word2Index)
                if distance < minDistance:
                    minDistance = distance
        
        return minDistance

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    word1 = "fox"
    word2 = "dog"
    expectedOutput = 5
    output = solution.ShortestWordDistance(words, word1, word2)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    words = ["a", "c", "d", "b", "a"]
    word1 = "a"
    word2 = "b"
    expectedOutput = 1
    output = solution.ShortestWordDistance(words, word1, word2)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    words = ["a", "b", "c", "d", "e"]
    word1 = "a"
    word2 = "e"
    expectedOutput = 4
    output = solution.ShortestWordDistance(words, word1, word2)
    print(output, expectedOutput, output == expectedOutput)
