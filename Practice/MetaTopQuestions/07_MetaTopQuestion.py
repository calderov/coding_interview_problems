# 680. Valid Palindrome II (Easy)
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
#
# Example 1:
# Input: s = "aba"
# Output: true
#
# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
#
# Example 3:
# Input: s = "abc"
# Output: false

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def ValidPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue

            # Skip the character to the 'right' and check if the section
            # between the left and right pointers is a palindrome
            skipRight = s[left : right]
            if skipRight == skipRight[::-1]:
                return True

            # Skip the character to the 'left' and check if the section
            # between the left and right pointers is a palindrome
            skipLeft = s[left + 1 : right + 1]
            if skipLeft == skipLeft[::-1]:
                return True

            # If no character skiping made the section between the left and right
            # pointers a palindrome, return False
            return False

        return True

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s = "aba"
    expectedOutput = True
    output = solution.ValidPalindrome(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    s = "abca"
    expectedOutput = True
    output = solution.ValidPalindrome(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    s = "abc"
    expectedOutput = False
    output = solution.ValidPalindrome(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    s = "eeccccbebaeeabebccceea"
    expectedOutput = False
    output = solution.ValidPalindrome(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    expectedOutput = True
    output = solution.ValidPalindrome(s)
    print(output, expectedOutput, output == expectedOutput)
