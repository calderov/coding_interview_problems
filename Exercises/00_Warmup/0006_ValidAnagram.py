# Problem
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

# Solution 1:
# Copy both strings s and t into a couple of lists. Sort those lists and compare them.
# If the sorted lists are equal return True, otherwise return False.
#
# Solution 1 complexity:
# Time complexity: O(nlog(n)) time due to the sorting step.
# Space complexity: O(n) space due to the auxiliary lists.
def IsAnagramV1(s, t):
    return sorted(s) == sorted(t)

# Solution 2:
# Create a frequency map to count how many times each character in s and t appear.
# For each character in s, add 1 to its frequency in the map.
# Similarly, for each character in t, substract to 1 its frequency in the map.
# If the strings are anagrams, the frequency for all characters in the frequency map
# should be zero, as we added 1 for each character in s, and substracted 1 for th
# corresponding character in t.
#
# Solution 2 complexity:
# Time complexity: O(nlog(n)) time due to the sorting step.
# Space complexity: O(n) space due to the auxiliary lists.
def IsAnagramV2(s, t):
    if len(s) != len(t):
        return False

    freqMap = {}
    n = len(s)

    for i in range(n):
        charS = s[i]
        charT = t[i]

        if charS not in freqMap:
            freqMap[charS] = 1
        else:
            freqMap[charS] += 1

        if charT not in freqMap:
            freqMap[charT] = -1
        else:
            freqMap[charT] -= 1

    for c in freqMap:
        if freqMap[c] != 0:
            return False

    return True


if __name__ == "__main__":
    print(IsAnagramV1("listen","silent"), True)
    print(IsAnagramV1("rat","car"), False)
    print(IsAnagramV1("hello","world"), False)

    print(IsAnagramV2("listen","silent"), True)
    print(IsAnagramV2("rat","car"), False)
    print(IsAnagramV2("hello","world"), False)