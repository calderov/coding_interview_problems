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
    # Solution 1:
    #
    # 1. Initialize a variable to keep track of the length of the longest substring
    #    that matches our criteria maxLengthAfterReplace = 0.
    # 
    # 2. Initialize a couple of pointers to mark the start and the end of a sliding window.
    #    start = 0
    #    end = 0
    #
    # 3. While the end of the sliding window is within the limits of the input string,
    #    check how many characters in the substring between start and + 1 are different
    #    from the first character in that substring. In other words count how many
    #    replacements are needed in the substring for all of its characters to be the
    #    the same as the first. Lets call this number potentialReplacements.
    #
    # 4. If the number of potentialReplacements is less than or equal than k, the
    #    current substring meets our criteria. Check if the substring is longer than
    #    the value at maxLengthAfterReplace, if so, replace maxLengthAfterReplace with
    #    the length of the substring.
    #
    # 5. If the number of potentialReplacements is greater than k, move the start of
    #    the substring until a different character is found.
    #
    # 6. Move the end of the substring one position to the right. If end < len(inputString)
    #    go back to step 3. Otherwise, return maxLengthAfterReplace and finish.
    # 
    # Solution complexity:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n) as the support structure to count the potential replacements can be as long as the input string
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
    

    # Solution 2:
    #
    # 1. Initialize a variable to keep track of the length of the longest substring
    #    that matches our criteria maxLengthAfterReplace = 0.
    # 
    # 2. Initialize a couple of pointers to mark the start and the end of the sliding
    #    window that delimits our explored substrings.
    #    start = 0
    #    end = 0
    # 
    # 3. Initialize a dictionary of characters. This will keep track how many times
    #    a given character appears in the substring induced by the sliding window.
    #    characters = {}
    #
    # 3. While the end of the sliding window is within the limits of the input string,
    #    check if the character at inputString[end] is in the characters dictionary.
    #    If not, add it to the dictionary and map it to a value of 1. Othewise,
    #    add 1 to its mapped value.
    #
    # 4. Compute the number of replacements needed in the substring for all of its
    #    characters to be the same as the first. This can be easily be done by this
    #    expresion:
    #    requiredReplacements = (end - start + 1) - characters[inputString[start]]
    #
    # 5. If the number of requiredReplacements is less than or equal than k, the
    #    current substring meets our criteria. Check if the substring is longer than
    #    the value at maxLengthAfterReplace, if so, replace maxLengthAfterReplace with
    #    the length of the substring.
    #
    # 6. If the number of requiredReplacements is greater than k, move the start of
    #    the substring until a different character is found. Remember decrease
    #    the count of characters accordingly.
    #
    # 7. Move the end of the substring one position to the right. If end < len(inputString)
    #    go back to step 3. Otherwise, return maxLengthAfterReplace and finish.
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
            
            requiredReplacements = (end - start + 1) - characters[inputString[start]]
            
            if requiredReplacements <= k:
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
