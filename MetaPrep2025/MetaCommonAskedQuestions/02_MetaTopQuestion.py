# 408. Valid Word Abbreviation (Easy)
# A string can be abbreviated by replacing any number of non-adjacent,
# non-empty substrings with their lengths. The lengths should not have
# leading zeros.
# 
# For example, a string such as "substitution" could be abbreviated as (but
# not limited to):
# 
#   "s10n" ("s ubstitutio n")
#   "sub4u4" ("sub stit u tion")
#   "12" ("substitution")
#   "su3i1u2on" ("su bst i t u ti on")
#   "substitution" (no substrings replaced)
# 
# The following are not valid abbreviations:
# 
#   "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
#   "s010n" (has leading zeros)
#   "s0ubstitution" (replaces an empty substring)
# 
# Given a string word and an abbreviation abbr, return whether the string
# matches the given abbreviation.
# 
# A substring is a contiguous non-empty sequence of characters within a
# string.
#  
# 
# Example 1:
#   Input: word = "internationalization", abbr = "i12iz4n"
#   Output: true
#   Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
#
# Example 2:
#   Input: word = "apple", abbr = "a2e"
#   Output: false
#   Explanation: The word "apple" cannot be abbreviated as "a2e".
#  

def isValidAbbreviation(word, abbr):
    if len(abbr) >= len(word):
        return False
    
    i = 0
    j = 0
    while i < len(word) and j < len(abbr):
        if word[i].isalpha() and abbr[j].isalpha():
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            else:
                return False
        
        if abbr[j] == "0":
            return False # Leading zero
        
        k = j
        while k < len(abbr) and abbr[k].isdigit():
            k += 1
        
        i += int(abbr[j:k])
        j = k
    
    return i == len(word) and j == len(abbr)

if __name__ == "__main__":
    # Example 1
    word = "internationalization"
    abbr = "i12iz4n"
    expected = True
    output = isValidAbbreviation(word, abbr)
    
    print(word)
    print(abbr)
    print(expected)
    print(output)
    print(output == expected)

    print()

    # Example 2
    word = "apple"
    abbr = "a2e"
    expected = False
    output = isValidAbbreviation(word, abbr)
    
    print(word)
    print(abbr)
    print(expected)
    print(output)
    print(output == expected)

    print()

    # Example 3
    word = "substitution"
    abbr = "sub4u4"
    expected = True
    output = isValidAbbreviation(word, abbr)
    
    print(word)
    print(abbr)
    print(expected)
    print(output)
    print(output == expected)

    print()