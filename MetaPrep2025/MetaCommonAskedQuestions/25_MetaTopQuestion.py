# 1216. Valid Palindrome III
# https://leetcode.ca/2019-03-30-1216-Valid-Palindrome-III/
#
# Given a string s and an integer k, return true if s is a k-palindrome.
# A string is k-palindrome if it can be transformed into a palindrome by
# removing at most k characters from it.
#
# Example 1:
# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
#
# Example 2:
# Input: s = "abbabcba", k = 1
# Output: true
# 
# Constraints:
#  1 <= s.length <= 1000
#  s consists of only lowercase English letters.
#  1 <= k <= s.length

# Time complexity: O(k * n^2)
# Space complexity: O(k * n^2)
def isKPalindrome(s, k, i=None, j=None):
    n = len(s)

    if k >= n - 1:
        return True

    if i == None and j == None:
        i = 0
        j = n - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            break
    
    if i >= j:
        return True
    
    if k == 0:
        return False

    return isKPalindrome(s, k - 1, i + 1, j) or isKPalindrome(s, k - 1, i, j - 1)

if __name__ == "__main__":
    # Example 1
    s = "abcdeca"
    k = 2
    expectedOutput = True
    output = isKPalindrome(s, k)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")

    # Example 2
    s = "abbabcba"
    k = 1
    expectedOutput = True
    output = isKPalindrome(s, k)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")

    # Example 3
    s = "aniztalavalxatinay"
    k = 3
    expectedOutput = True
    output = isKPalindrome(s, k)
    print(f"{output}\t{expectedOutput}\t{output == expectedOutput}")
