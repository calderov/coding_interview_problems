# Find the Index of the First Occurrence in a String
# EASY
# https://scaleengineer.com/dsa/problems/find-the-index-of-the-first-occurrence-in-a-string

# Description
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

# Constraints:
#     1 <= haystack.length, needle.length <= 104
#     haystack and needle consist of only lowercase English characters.

# Time: O(m * n)
# Space: O(m)
def FindNeedleInHaystack(needle, haystack):
    m = len(needle)
    n = len(haystack)

    if m > n:
        return -1
    
    for i in range(0, n - m + 1):
        if haystack[i : i + m] == needle:
            return i
        
    return -1

if __name__ == "__main__":
    # Example 1:
    haystack = "sadbutsad"
    needle = "sad"
    expected = 0
    output = FindNeedleInHaystack(needle, haystack)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    haystack = "leetcode"
    needle = "leeto"
    expected = -1
    output = FindNeedleInHaystack(needle, haystack)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    haystack = "thequickbrownfoxjumpsoverthelazydog"
    needle = "lazy"
    expected = 28
    output = FindNeedleInHaystack(needle, haystack)
    print(expected)
    print(output)
    print(expected == output)
    print()
