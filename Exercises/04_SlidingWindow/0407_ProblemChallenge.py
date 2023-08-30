# Problem:
# Given a string and a pattern, find out if the string contains any 
# permutation of the pattern.
# 
# Permutation is defined as the re-arranging of the characters of the string.
# For example, “abc” has the following six permutations:
# 
#     abc
#     acb
#     bac
#     bca
#     cab
#     cba
# 
# If a string has n distinct characters, it will have n! permutations.
# 
# Example 1:
# 
# Input: String="oidbcaf", Pattern="ABC"   
# Output: true   
# Explanation: The string contains "bca" which is a permutation of the given
# pattern.
# 
# Example 2:
# 
# Input: String="odicf", Pattern="dc"   
# Output: false  
# Explanation: No permutation of the pattern is present in the given string
# as a substring.
# 
# Example 3:
# 
# Input: String="bcdxabcdy", Pattern="bcdyabcdx"  
# Output: true  
# Explanation: Both the string and the pattern are a permutation of each other.
# 
# Example 4:
# 
# Input: String="aaacb", Pattern="abc"  
# Output: true  
# Explanation: The string contains "acb" which is a permutation of the given
# pattern.
# 

class Solution:
    # Solution:
    # 1. Transform input string and pattern into arrays of lowercase chars.
    #
    # 2. Sort pattern array to make it easier to compare.
    #
    # 3. Initialize sliding window limits.
    #      start = 0
    #      end = 0
    #
    # 4. Traverse the input string using the sliding window. If the substring 
    #    between the sliding window is equal to the pattern when both are
    #    sorted, return True, as they are made of the same characters.
    #
    # 5. Otherwise, move the sliding window one position to the right.
    #    Repeat steps 4 and 5 until the sliding window reaches the end
    #    of the inputString array.
    #
    # 6. If no substring permutation matched the pattern (thus, the algorithm
    #    made it this far), return False and finish.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n) due to the array copies of the original string and the pattern
    def IsPatternPermutationInString(self, inputString, pattern):
        # Transform input string and pattern into arrays of lowercase chars
        inputString = [i for i in inputString.lower()]
        pattern = [i for i in pattern.lower()]

        # Sort pattern to make it easier to compare
        pattern.sort()

        # Initialize sliding window
        start = 0
        end = len(pattern) - 1

        # Traverse the input string using the sliding window
        while end < len(inputString):
            # If the substring between the sliding window is equal to the pattern
            # when both are sorted, return True, as they are made of the same
            # characters.
            substring = inputString[start : end + 1]
            if sorted(substring) == pattern:
                return True
            
            # Otherwise, move the sliding window one item to the right
            start += 1
            end += 1

        # If no substring permutation matches the pattern, return False
        return False

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    inputString = "oidbcaf"
    pattern = "ABC"
    expectedOutput = True 
    output = solution.IsPatternPermutationInString(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    inputString = "odicf"
    pattern = "dc"
    expectedOutput = False
    output = solution.IsPatternPermutationInString(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    inputString = "bcdxabcdy"
    pattern = "bcdyabcdx"
    expectedOutput = True
    output = solution.IsPatternPermutationInString(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    inputString = "aaacb"
    pattern = "abc"
    expectedOutput = True  
    output = solution.IsPatternPermutationInString(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput)
