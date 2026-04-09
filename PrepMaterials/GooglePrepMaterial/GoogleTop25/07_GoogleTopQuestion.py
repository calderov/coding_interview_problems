# Longest Common Prefix
# EASY
# https://scaleengineer.com/dsa/problems/longest-common-prefix

# Description
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strings = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strings = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
#     1 <= strings.length <= 200
#     0 <= strings[i].length <= 200
#     strings[i] consists of only lowercase English letters if it is non-empty.

def LongestCommonPrefix(strings):
    smallestS = min(strings, key=len)
   
    for i in range(len(smallestS)):
        c = smallestS[i]
        for s in strings:
            if s[i] == c:
                continue
            else:
                return smallestS[:i]
    
    return smallestS

if __name__ == "__main__":
    # Example 1:
    strings = ["flower","flow","flight"]
    expected = "fl"
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    strings = ["dog","racecar","car"]
    expected = ""
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3: All strings are the same
    strings = ["test", "test", "test"]
    expected = "test"
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: Single string
    strings = ["hello"]
    expected = "hello"
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Strings with different lengths
    strings = ["a", "ab", "abc"]
    expected = "a"
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: No common prefix
    strings = ["abc", "def", "ghi"]
    expected = ""
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: One empty string
    strings = ["", "abc"]
    expected = ""
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 8: All empty strings
    strings = ["", "", ""]
    expected = ""
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 9: Prefix longer than some strings
    strings = ["abcd", "abc", "ab"]
    expected = "ab"
    output = LongestCommonPrefix(strings)
    print(expected)
    print(output)
    print(expected == output)
    print()
