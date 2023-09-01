# Problem:
# Given a string and a list of words, find all the starting indices of
# substrings in the given string that are a concatenation of all the given
# words exactly once without any overlapping of words. It is given that all
# words are of the same length.
# 
# Examples:
# 
#   Input: String="catfoxcat", Words=["cat", "fox"]  
#   Output: [0, 3]  
#   Explanation: The two substring containing both the words are "catfox" &
#   "foxcat".
#
#   Input: String="catcatfoxfox", Words=["cat", "fox"]  
#   Output: [3]
#   Explanation: The only substring containing both the words is "catfox".

class Solution:
    # Solution:
    # 1. Initialize indexes list.
    #    indexes = []
    #
    # 2. Initialize sliding window pointers.
    #    start = 0
    #    end = 0
    # 
    # 3. While the sliding window is within the range of the input string
    #    check if the substring induced by the sliding window is a concatenation
    #    of the words in the given list. If so, append the start pointer to the
    #    indexes list.
    # 
    # 4. Move the slidng window one element to the left and repeat steps 3 and 4
    #    if the sliding window is still whitin range of the input string.
    # 
    # 5. Return indexes list.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindWordsConcatenation(self, inputString, words):
        # Initialize indexes list
        indexes = []

        # Initialize sliding window
        start = 0
        end = sum([len(word) for word in words]) - 1

        # While the sliding window is within the range of the input string
        while end < len(inputString):
            # Check if the substring induced by the sliding window is a concatenation
            # of the words in the given list. If so, append the start pointer to the
            # indexes list.
            if self.IsConcatenation(inputString[start : end + 1], words):
                indexes.append(start)
            
            # Move the slidng window one element to the left
            end += 1
            start += 1
        
        # Return indexes list
        return indexes
        

    def IsConcatenation(self, inputString, words):
        # Get the word length
        wordLength = len(words[0])

        # Slice input string into particles of the same word length as the first word of the words array
        particles = [inputString[i : i + wordLength] for i in range(0, len(inputString), wordLength)]
        
        # For each word in the word list
        for word in words:
            # If the word is not in the particles list, return False
            if word not in particles:
                return False
            
            # Otherwise, mark the first instance of the word in the particle list with a zero
            index = particles.index(word)
            particles[index] = 0

        # If there is any unmarked particle, return zero
        for particle in particles:
            if particle:
                return False

        # Otherwise return true
        return True

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    inputString = "catfoxcat"
    words = ["cat", "fox"]
    expectedOutput = [0, 3]  
    output = solution.FindWordsConcatenation(inputString, words)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    inputString = "catcatfoxfox"
    words = ["cat", "fox"]
    expectedOutput = [3]
    output = solution.FindWordsConcatenation(inputString, words)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    inputString = "catcatcatcat"
    words = ["cat", "cat"]
    expectedOutput = [0, 3, 6]
    output = solution.FindWordsConcatenation(inputString, words)
    print(output, expectedOutput, output == expectedOutput)
