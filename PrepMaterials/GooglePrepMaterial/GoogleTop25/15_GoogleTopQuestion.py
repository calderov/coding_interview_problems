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

# Time: O(m * n) where m = |s| and n = |p|
# Space: O(m * n) for the cache + O(m + n) for the recursion stack
def IsMatch(s, p):
    cache = [[None] * len(p) for _ in range(len(s))]
    
    def PatternMatch(indexS, indexP):
        if indexS == len(s) and indexP == len(p):
            return True
        
        if indexP == len(p):
            return False
        
        if indexS == len(s):
            if p[indexP] == '*':
                return PatternMatch(indexS, indexP + 1)
            return False
        
        if cache[indexS][indexP] is not None:
            return cache[indexS][indexP]

        if s[indexS] == p[indexP] or p[indexP] == '?':
            cache[indexS][indexP] = PatternMatch(indexS + 1, indexP + 1)
            return cache[indexS][indexP]
        
        if p[indexP] == '*':
            cache[indexS][indexP] = PatternMatch(indexS + 1, indexP) or PatternMatch(indexS, indexP + 1)
            return cache[indexS][indexP]

        cache[indexS][indexP] = False
        return cache[indexS][indexP]

    return PatternMatch(0, 0)

if __name__ == "__main__":
    # Example 1:
    s = "aa"
    p = "a"
    expected = False
    output = IsMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    s = "aa"
    p = "*"
    expected = True
    output = IsMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    s = "cb"
    p = "?a"
    expected = False
    output = IsMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: empty string with empty pattern
    s = ""
    p = ""
    expected = True
    output = IsMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: empty string with star pattern
    s = ""
    p = "*"
    expected = True
    output = IsMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: complex star matching
    s = "adceb"
    p = "*a*b"
    expected = True
    output = IsMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: mismatch with question mark and star
    s = "acdcb"
    p = "a*c?b"
    expected = False
    output = IsMatch(s, p)
    print(expected)
    print(output)
    print(expected == output)
    print()
