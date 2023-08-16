# Problem:
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

class Solution:
    # Solution 1:
    # Copy both strings s and t into a couple of lists. Sort those lists and compare them.
    # If the sorted lists are equal return True, otherwise return False.
    #
    # Solution 1 complexity:
    # Time complexity: O(nlog(n)) time due to the sorting step.
    # Space complexity: O(n) space due to the auxiliary lists.
    def IsAnagramV1(self, s, t):
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
    def IsAnagramV2(self, s, t):
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

    def IsAnagram(self, s, t):
        return self.IsAnagramV2(s, t)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    string1 = "listen"
    string2 ="silent"
    expectedOutput = True
    output = solution.IsAnagram(string1, string2)
    print(string1, string2, expectedOutput, output, expectedOutput == output)

    # Example 2
    string1 = "rat"
    string2 ="car"
    expectedOutput = False
    output = solution.IsAnagram(string1, string2)
    print(string1, string2, expectedOutput, output, expectedOutput == output)

    # Example 3
    string1 = "hello"
    string2 ="world"
    expectedOutput = False
    output = solution.IsAnagram(string1, string2)
    print(string1, string2, expectedOutput, output, expectedOutput == output)
