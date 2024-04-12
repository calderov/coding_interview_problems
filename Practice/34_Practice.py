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
        
        have = {}
        need = {}
        haveSum = 0
        needSum = 0

        for c in t:
            if c not in need:
                need[c] = 0
                have[c] = 0
                needSum += 1
            need[c] += 1

        left = 0
        right = 0
        start = 0
        end = float('inf')

        while left <= right and right < len(s):
            c = s[right]
            if c in need:
                have[c] += 1
                if need[c] == have[c]:
                    haveSum += 1

            while needSum == haveSum:
                if  right - left + 1 < end - start + 1:
                    start, end = left, right
                
                if s[left] in need:
                    have[s[left]] -= 1
                    if have[s[left]] < need[s[left]]:
                        haveSum -= 1
                left += 1

            right += 1

        return s[start:end + 1] if end != float('inf') else ""