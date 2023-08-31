# Problem: 
# Given a string and a pattern, find all anagrams of the pattern in the given
# string.
# 
# Every anagram is a permutation of a string. As we know, when we are not
# allowed to repeat characters while finding permutations of a string, we get
# N! permutations (or anagrams) of a string having N characters. For example,
# here are the six anagrams of the string “abc”:
# 
#   1. abc
#   2. acb
#   3. bac
#   4. bca
#   5. cab
#   6. cba
# 
# Write a function to return a list of starting indices of the anagrams of
# the pattern in the given string.
# 
# Examples:
# 
# Input: String="ppqp", Pattern="pq"  
# Output: [1, 2]  
# Explanation: The two anagrams of the pattern in the given string are "pq"
# and "qp".
# 
# Input: String="abbcabc", Pattern="abc"  
# Output: [2, 3, 4]  
# Explanation: The three anagrams of the pattern in the given string are
# "bca", "cab", and "abc".

class Solution:
    # Solution:
    # 1. Transform input string and pattern into arrays of lowercase characters.
    #
    # 2. Sort the pattern to make it easier to compare.
    #
    # 3. Initialize sliding window and indexes array.
    #    start = 0
    #    end = 0
    #
    # 4. Use a while loop to traverse the input string using the sliding window
    #
    # 5. If the substring between the sliding window and the pattern are
    #    equal when both are sorted, then the substring is an anagram of
    #    the pattern. Add the start pointer to the indexes array, as it
    #    marks the start of an anagram.
    #
    # 6. Move the sliding window one item to the right, and repeat steps 4, 5 and 6
    #    until the sliding reaches the end of the input string.
    #
    # 7. Return the indexes array, by now it will contain the
    #    start indexes of all the anagrams of the pattern in
    #    the input string.
    #
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def FindAllPatternAnagrams(self, inputString, pattern):
        # Transform input string and pattern into arrays of lowercase characters
        inputString = [i for i in inputString.lower()]
        pattern = [i for i in pattern.lower()]

        # Sort the pattern to make it easier to compare
        pattern.sort()
        
        # Initialize sliding window and indexes array
        start = 0
        end = len(pattern) - 1
        indexes = []

        # Traverse the input string using the sliding window
        while end < len(inputString):
            # If the substring between the sliding window and the pattern are
            # equal when both are sorted, then the substring is an anagram of
            # the pattern. Add the start to the indexes array, as it marks the
            # start of an anagram.
            substring = inputString[start : end + 1]
            if sorted(substring) == pattern:
                indexes.append(start)

            # Move the sliding window one item to the right
            start += 1
            end += 1
        
        # Return the indexes array, by now it will contain the
        # start indexes of all the anagrams of the pattern in
        # the input string.
        return indexes

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1:
    inputString = "ppqp"
    pattern = "pq"
    expectedOutput = [1, 2]
    output = solution.FindAllPatternAnagrams(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2:
    inputString = "abbcabc"
    pattern = "abc"
    expectedOutput = [2, 3, 4]
    output = solution.FindAllPatternAnagrams(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput)
