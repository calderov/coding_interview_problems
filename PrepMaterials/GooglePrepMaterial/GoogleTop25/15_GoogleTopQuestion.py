# Wildcard Matching
# HARD
# https://scaleengineer.com/dsa/problems/wildcard-matching

# Description
# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
#     '?' Matches any single character.
#     '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aa", p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input: s = "aa", p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input: s = "cb", p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# Constraints:
#     0 <= s.length, p.length <= 2000
#     s contains only lowercase English letters.
#     p contains only lowercase English letters, '?' or '*'.

def PatternMatch(s, p):
    hasCache = [[False] * len(p) for _ in range(len(s))]
    cache = [[None] * len(p) for _ in range(len(s))]
    
    def isMatch(indexS, indexP):
        if indexS == len(s) and indexP == len(p):
            return True
        
        if indexP == len(p):
            return False
        
        if indexS == len(s):
            if p[indexP] == '*':
                return isMatch(indexS, indexP + 1)
            return False
        
        if hasCache[indexS][indexP]:
            return cache[indexS][indexP]

        if s[indexS] == p[indexP] or p[indexP] == '?':
            cache[indexS][indexP] = isMatch(indexS + 1, indexP + 1)
            hasCache[indexS][indexP] = True
            return cache[indexS][indexP]
        
        if p[indexP] == '*':
            cache[indexS][indexP] = isMatch(indexS + 1, indexP) or isMatch(indexS, indexP + 1)
            hasCache[indexS][indexP] = True
            return cache[indexS][indexP]

        cache[indexS][indexP] = False
        hasCache[indexS][indexP] = True
        return cache[indexS][indexP]

    return isMatch(0, 0)

if __name__ == "__main__":
    # Example 1:
    s = "aa"
    p = "a"
    expected = False
    output = PatternMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    s = "aa"
    p = "*"
    expected = True
    output = PatternMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    s = "cb"
    p = "?a"
    expected = False
    output = PatternMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()
