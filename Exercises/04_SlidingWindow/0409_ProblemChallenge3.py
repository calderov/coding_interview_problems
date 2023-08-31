# Problem:
# Given a string and a pattern, find the smallest substring in the given
# string which has all the character occurrences of the given pattern.
# 
# Example:
# 
#   Input: String="aabdec", Pattern="abc"  
#   Output: "abdec"  
#   Explanation: The smallest substring having all characters of the pattern
#   is "abdec"
# 
#   Input: String="aabdec", Pattern="abac"  
#   Output: "aabdec"  
#   Explanation: The smallest substring having all characters occurrences of
#   the pattern is "aabdec"
# 
#   Input: String="abdbca", Pattern="abc"  
#   Output: "bca"  
#   Explanation: The smallest substring having all characters of the pattern
#   is "bca".
# 
#   Input: String="adcad", Pattern="abc"  
#   Output: ""  
#   Explanation: No substring in the given string has all characters of the
#   pattern
# 

class Solution:
    # Solution:
    # 1. Initialize a couple of dictionaries, these will map the characters
    #    of the pattern and a given substring to their frequency (how many
    #    time does each character appear).
    #      
    #      patternFrequencyMap = StringToFrequencyMap(pattern)
    #      substringFrequencyMap = {}
    # 
    # 2. Initialize the smallestSubstring (our value to return) as a string
    #    that is 1 character longer than the input string. This is intentional
    #    as we will use its length to compare against substrings that match
    #    the pattern and later to check if it remained unaltered after
    #    the search, in which case we will return an empty string.
    #
    #      smallestSubstring = inputString + 'x'
    #
    # 3. Initialize two pointers for our sliding window.
    #      start = 0
    #      end = 0
    #
    # 4. Use a while loop to traverse the input string using the sliding window.
    #    It should repeat until the end pointer is within the range of the 
    #    input string.
    #
    # 5. Insert the character at end of the sliding windo into the
    #    substringFrequencyMap.
    #
    # 6. While the substring inputString[start : end + 1] matches the pattern
    #    (has as many of the same characters as the pattern has), update the
    #    smallestSubstring if needed, and shrink the sliding window. 
    # 
    #    Do this by removing the character at the start of the substring from the
    #    substringFrequencyMap and by moving the start pointer one position to the right
    #    in each iteration.
    #
    # 7. Move the end of the sliding window to the next character of the input string
    #    and repeat from step 4 onwards if end is still within the range of the inputString,
    #    otherwise continue to step 8.
    #
    # 8. If the length of the smallestSubstring is longer than the input string it means
    #    that no substring matched the pattern, return an empty string in this case.
    #    Otherwise, return smallestSubstring and finish
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def SmallestSubstringWithAllCharactersInPattern(self, inputString, pattern):
        # Initialize frequency maps
        patternFreqMap = self.StringToFreqMap(pattern)
        substringFreqMap = {}

        # Initialize smallest substring
        smallestSubstring = inputString + 'x'
        
        # Initialize sliding window
        start = 0
        end = 0

        # Traverse input string using the sliding window
        while end < len(inputString):
            # Insert character at end into the substring frequency map
            self.SafeInsert(substringFreqMap, inputString[end])

            # While the substring matches the pattern update the
            # smallest substring and shrink the sliding window
            # by removing characters from the start of the
            # substring and moving the start pointer
            while self.PatternMatch(substringFreqMap, patternFreqMap):
                if end - start + 1 < len(smallestSubstring):
                    smallestSubstring = inputString[start : end + 1]
                
                substringFreqMap[inputString[start]] -= 1
                start += 1

            # Move the end of the sliding window to the next character of
            # the input string
            end += 1

        # If none of the substrings matched the pattern
        # return an empty string
        if len(smallestSubstring) > len(inputString):
            return ''

        # Otherwise, return the smallest substring
        return smallestSubstring

    def PatternMatch(self, substringFreqMap, patternFreqMap):
        for c in patternFreqMap:
            if c not in substringFreqMap:
                return False
            if substringFreqMap[c] < patternFreqMap[c]:
                return False
        return True

    def StringToFreqMap(self, inputString):
        freqMap = {}
        for value in inputString:
            self.SafeInsert(freqMap, value)
        return freqMap

    def SafeInsert(self, freqMap, value):
        if value not in freqMap:
            freqMap[value] = 0
        freqMap[value] += 1

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1:
    inputString = "aabdec"
    pattern = "abc"
    expectedOutput = "abdec"
    output = solution.SmallestSubstringWithAllCharactersInPattern(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput) 
    
    # Example 2:
    inputString = "aabdec"
    pattern = "abac"
    expectedOutput = "aabdec"
    output = solution.SmallestSubstringWithAllCharactersInPattern(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput) 
    
    # Example 3:
    inputString = "abdbca"
    pattern = "abc"
    expectedOutput = "bca"
    output = solution.SmallestSubstringWithAllCharactersInPattern(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput) 
    
    # Example 4:
    inputString = "adcad"
    pattern = "abc"
    expectedOutput = ""
    output = solution.SmallestSubstringWithAllCharactersInPattern(inputString, pattern)
    print(output, expectedOutput, output == expectedOutput) 
