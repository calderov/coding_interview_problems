# Problem:
# Given a string s, return the maximum number of unique substrings that the
# given string can be split into.
#
# You can split string s into any list of non-empty substrings, where the
# concatenation of the substrings forms the original string. However, you
# must split the substrings such that all of them are unique.
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: s = "aab"
# Output: 2
# Explanation: Two possible ways to split the given string into maximum
# unique substrings are: ['a', 'ab'] & ['aa', 'b'], both have 2 substrings;
# hence the maximum number of unique substrings in which the given string can
# be split is 2.
# Example 2:
#
# Input: s = "abcabc"
# Output: 4
# Explanation: Four possible ways to split into maximum unique substrings
# are: ['a', 'b', 'c', 'abc'] & ['a', 'b', 'cab', 'c'] &  ['a', 'bca', 'b',
# 'c'] & ['abc', 'a', 'b', 'c'], all have 4 substrings.

class Solution:
    def MaxUniqueSubstrings(self, inputString, start=0, substrings=set()):
        # If we have reached the end of the input string, return the length
        # of the substrings set
        if start == len(inputString):
            return len(substrings)

        # Keep count of the substrings
        count = 0

        # Loop through all substrings starting from the current location
        for i in range(start + 1, len(inputString) + 1):
            substring = s[start : 1]

            # If the current substring is not in the substrings set, add it and
            # call this function recursively with the current start position
            if substring not in substrings:
                substrings.add(substring)

                count = max(count, self.MaxUniqueSubstrings(inputString, i, substrings))

                # Backtrack by removing the current substring from the set
                substrings.remove(substring)

        # Return the maximum count of unique substrings found
        return count


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s = "aab"
    expectedOutput = 2
    output = solution.MaxUniqueSubstrings(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    s = "abcabc"
    expectedOutput = 4
    output = solution.MaxUniqueSubstrings(s)
    print(output, expectedOutput, output == expectedOutput)
