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
    def MaxLengthAfterReplace(self, inputString, k):
        maxLengthAfterReplace = 0
        start = 0
        end = 0
        
        while end < len(inputString):
            if self.potentialReplacements(inputString[start: end + 1]) <= k:
                maxLengthAfterReplace = max(maxLengthAfterReplace, end - start + 1)
            else:
                c = inputString[start]
                while inputString[start] == c:
                    start += 1            
            end += 1
        
        return maxLengthAfterReplace

    def potentialReplacements(self, substring):
        return len([i for i in substring if i != substring[0]])

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    inputString = "aabccbb"
    k = 2  
    expectedOutput = 5
    output = solution.MaxLengthAfterReplace(inputString, k)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    inputString = "abbcb"
    k = 1  
    expectedOutput = 4
    output = solution.MaxLengthAfterReplace(inputString, k)
    print(output, expectedOutput, output == expectedOutput)