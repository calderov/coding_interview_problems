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

def isValidPalindrome(s, left, right):  
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Time complexity: O(n)
# Space complexity: O(1)
def canBecomeValidPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue
       
        return isValidPalindrome(s, left + 1, right) or isValidPalindrome(s, left, right - 1)

    return True

if __name__ == "__main__":
    # Example 1
    s = "aba"
    expectedOutput = True
    output = canBecomeValidPalindrome(s)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")

    # Example 2
    s = "abca"
    expectedOutput = True
    output = canBecomeValidPalindrome(s)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")

    # Example 3
    s = "abc"
    expectedOutput = False
    output = canBecomeValidPalindrome(s)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")

    # Example 4
    s = "eeccccbebaeeabebccceea"
    expectedOutput = False
    output = canBecomeValidPalindrome(s)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")

    # Example 5
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    expectedOutput = True
    output = canBecomeValidPalindrome(s)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")
