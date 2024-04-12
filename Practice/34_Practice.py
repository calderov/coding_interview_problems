# 76. Minimum Window Substring (Hard)
# Given two strings s and t of lengths m and n respectively, return the
# minimum window substring of s such that every character in t (including
# duplicates) is included in the window. If there is no such substring,
# return the empty string "".
# 
# The testcases will be generated such that the answer is unique.
# 
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
# 
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# 
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
# 
# Constraints:
# - m == s.length
# - n == t.length
# - 1 <= m, n <= 105
# - s and t consist of uppercase and lowercase English letters.
#  
# 
# Follow up: Could you find an algorithm that runs in O(m + n) time?
#
# NOTE: 
# This solution is based on the one presented by Neetcode here: 
# https://www.youtube.com/watch?v=jSto0O4AJbM
#

class Solution:
    # Time complexity: O(n + m)
    # Space complexity: O(1)
    def minWindow(self, s, t):
        if not s or not t or len(s) < len(t):
            return ""
        
        # Initialize two pointers to delimit the shortest substring of s that contains all
        # the characters in t including duplicates. We assume our initial substring to
        # be of infinite length as this is a minimization problem.
        start = 0
        end = float('inf')

        # Initialize two dictionaries to keep track of the characters we need (those in t)
        # and those characters we have (those inside the sliding window s[left:right + 1]
        # that are also in need).
        have = {}
        need = {}

        # Initialize two counters to track how many character requirements we have (haveSum)
        # and how many of those have been satisfied (needSum)
        haveSum = 0
        needSum = 0

        # For each character c in t add an entry into need and have, and keep a count
        # of character instances in need. Also, add 1 to needSum for each different
        # character entry.
        for c in t:
            if c not in need:
                need[c] = 0
                have[c] = 0
                needSum += 1
            need[c] += 1
        
        # Initialize the left and right pointers to delimit the sliding window that
        # will produce candidate substrings
        left = 0
        right = 0

        # While the right pointer has not reached the end
        while right < len(s):
            # If the character on the right c is needed, add 1 to its entry in the "have" dictionary.
            c = s[right]
            if c in need:
                have[c] += 1

                # If there are as many instances of c as they are needed, increment the
                # sum of satisfied requirements by one (haveSum += 1).
                if need[c] == have[c]:
                    haveSum += 1

            # While all of the character requirements are met
            while needSum == haveSum:
                # Check if the length of the current window is less
                # than the shortest substring that we have found so far
                # that contains all the cars of t in s. If the window
                # is shorter, update the pointers of the shortest substring
                # accordingly.
                if  right - left + 1 < end - start + 1:
                    start, end = left, right
                
                # If the character at the left of the window is needed.
                # Decrease its ammount by one from the "have" dictionary.
                #
                # If this leaves less of these characters in the "have" dictionary
                # than in the "need" dictionary, then the requirement for this
                # character has been broken, remove 1 from the haveSum count.
                if s[left] in need:
                    have[s[left]] -= 1

                    if have[s[left]] < need[s[left]]:
                        haveSum -= 1
                
                # Move the left pointer one position to the left
                left += 1

            # Move the right pointer one position to the left
            right += 1

        # Return the substring delimited by the start and end pointers unless the
        # endpointer is still infinite, if this is the case, return an empty string
        # as this means that no substring of s contains all the characters in t
        return s[start:end + 1] if end != float('inf') else ""