# Problem:
# Given a string, find the length of the longest substring in it with no more
# than K distinct characters.
#
# You can assume that K is less than or equal to the length of the given string.
#
# Examples:
#
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
#
# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

class Solution:
    # Solution:
    # 1. Initialize a variable to keep track of the length of the longest substring
    #    that matches our criteria. These are, those substrings with at most k distinct
    #    characters. Since we have not explored any substring yet, initialize this variable
    #    to zero.
    #      longestSubstringLength = 0
    # 
    # 2. Initialize a couple of pointers to mark the start and the end of the sliding window.
    #    start = 0
    #    end = 0
    #
    # 3. Initialize an empty list named substring, we will use it to keep a copy of the
    #    substring being evaluated (it is a list so we can add or remove items from the
    #    beginning or the end at low cost).
    #
    # 4. While the end of the sliding window is still within the limits of the input string 
    #   (inputString) append inputString[end] to the substring list.
    # 
    # 5. If the number of distinct characters in the substring is less than k, check if the
    #    length of the substring is greater than longestSubstringLength, and update it if needed.
    #      longestSubstringLength = max(longestSubstringLength, len(substring))
    #
    # 6. If the number of distinct characters in the substring is greater than k, remove the first
    #    element of the substring until this is no longer the case. Do this using a while loop 
    #    and add 1 to the start pointer on each iteration.
    #
    # 7. Add 1 to the end pointer and loop back to step 4, unless the end pointer has passed
    #    the end of the string.
    #
    # 8. Return longestSubstringLength and finish.
    #    
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n) as the support substring can be as long as the original string
    def LongestSubstringWithKDistinctCharacters(self, inputString, k):
        longestSubstringLength = 0
        start = 0
        end = 0

        substring = []

        while end < len(inputString):
            substring.append(inputString[end])

            if len(set(substring)) <= k:
                longestSubstringLength = max(longestSubstringLength, len(substring))

            while len(set(substring)) > k:
                substring.pop(0)
                start += 1

            end += 1

        return longestSubstringLength


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    inputString = "araaci"
    k = 2
    expectedOutput = 4
    output = solution.LongestSubstringWithKDistinctCharacters(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    inputString = "araaci"
    k = 1
    expectedOutput = 2
    output = solution.LongestSubstringWithKDistinctCharacters(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    inputString = "cbbebi"
    k = 3
    expectedOutput = 5
    output = solution.LongestSubstringWithKDistinctCharacters(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    inputString = "aabbccdd"
    k = 2
    expectedOutput = 4
    output = solution.LongestSubstringWithKDistinctCharacters(inputString, k)
    print(output, expectedOutput, output == expectedOutput)
