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
    # Time complexity: O(n) where n is the number of characters in the input S
    # Space complexity: O(n)
    def MaxLengthAfterReplace(self, s, k):
        longest_substring_length = 0

        frequency_map = {}
        max_frequency = 0

        start = 0
        for end in range(len(s)):
            frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

            # Update the maximum frequency we have seen in any window yet
            max_frequency = max(max_frequency, frequency_map[s[end]])

            # Compute the min number of required replacements
            replacements = end - start + 1 - max_frequency

            # If the number of required replacements exceeds k
            # decrease the frequency of the character at the start
            # and move the start pointer one step to the right
            if replacements > k:
                frequency_map[s[start]] -= 1
                start += 1

            # The window is valid at this point, store length
            # size of the window never decreases
            longest_substring_length = end - start + 1

        return longest_substring_length

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

    # Example 5
    inputString = "baaab"
    k = 2
    expectedOutput = 5
    output = solution.MaxLengthAfterReplace(inputString, k)
    print(output, expectedOutput, output == expectedOutput)
