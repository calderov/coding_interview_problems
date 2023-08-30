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
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n) as the substring of potential replacements can be as long as the input string
    def MaxLengthAfterReplaceV1(self, inputString, k):
        maxLengthAfterReplace = 0
        start = 0
        end = 0
        
        while end < len(inputString):
            if inputString[start] == inputString[end] or self.potentialReplacements(inputString[start: end + 1]) <= k:
                maxLengthAfterReplace = max(maxLengthAfterReplace, end - start + 1)
            else:
                c = inputString[start]
                while inputString[start] == c:
                    start += 1            
            end += 1
        
        return maxLengthAfterReplace

    def potentialReplacements(self, substring):
        return len([i for i in substring if i != substring[0]])
    

    # Solution:
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1) as the characters dictionary has at most 26 entries, one for every character
    def MaxLengthAfterReplaceV2(self, inputString, k):
        maxLengthAfterReplace = 0
        characters = {}
        start = 0
        end = 0
        
        while end < len(inputString):
            if inputString[end] not in characters:
                characters[inputString[end]] = 0
            characters[inputString[end]] += 1
            
            replacements = (end - start + 1) - characters[inputString[start]]
            
            if replacements <= k:
                maxLengthAfterReplace = max(maxLengthAfterReplace, end - start + 1)
            else:
                c = inputString[start]
                while inputString[start] == c:
                    characters[c] -= 1
                    start += 1
            end += 1
        
        return maxLengthAfterReplace
    

    def MaxLengthAfterReplace(self, inputString, k):
        return self.MaxLengthAfterReplaceV2(inputString, k)

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

    # Example 3
    inputString = "abababab"
    k = 1
    expectedOutput = 3
    output = solution.MaxLengthAfterReplace(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    inputString = "aabbaabbaabb"
    k = 2
    expectedOutput = 6
    output = solution.MaxLengthAfterReplace(inputString, k)
    print(output, expectedOutput, output == expectedOutput)
