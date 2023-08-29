# Problem:
# Given a string with lowercase letters only, if you are allowed to replace
# no more than ‘k’ letters with any letter, find the length of the longest
# substring having the same letters after replacement.
# 
# Examples:
# 
# Input: String="aabccbb", k=2  
# Output: 5  
# Explanation: Replace the two 'c' with 'b' to have a longest repeating
# substring "bbbbb".
# 
# Input: String="abbcb", k=1  
# Output: 4  
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring
# "bbbb".
# 

class Solution:
    # Solution:
    #
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def foo(self, inputString, k):
        pass

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    inputString = "aabccbb"
    k = 2  
    expectedOutput = 5
    output = solution.foo(inputString, k)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    inputString = "abbcb"
    k = 1  
    expectedOutput = 4
    output = solution.foo(inputString, k)
    print(output, expectedOutput, output == expectedOutput)