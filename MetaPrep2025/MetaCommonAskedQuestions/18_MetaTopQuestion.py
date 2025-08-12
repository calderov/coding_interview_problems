# 921. Minimum Add to Make Parentheses Valid (Medium)
# A parentheses string is valid if and only if:
# 
# - It is the empty string,
# - It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# - It can be written as (A), where A is a valid string.
# 
# You are given a parentheses string s. In one move, you can insert a
# parenthesis at any position of the string.
# 
# For example, if s = "()))", you can insert an opening parenthesis to be
# "(()))" or a closing parenthesis to be "())))".
# Return the minimum number of moves required to make s valid.
# 
# Example 1:
#   Input: s = "())"
#   Output: 1
# 
# Example 2:
#   Input: s = "((("
#   Output: 3
# 
# Constraints:
# - 1 <= s.length <= 1000
# - s[i] is either '(' or ')'.

# Time complexity: O(n)
# Space complexity: O(1)
def minAddToMakeValid(s):
    openP = 0
    closingP = 0

    for c in s:
        if c == "(":
            openP += 1
            continue

        if c == ")":
            if openP:
                openP -= 1
            else:
                closingP += 1

    return openP + closingP
                
    
if __name__ == "__main__":
    # Example 1:
    s = "())"
    expectedOutput = 1
    output = minAddToMakeValid(s)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2:
    s = "((("
    expectedOutput = 3
    output = minAddToMakeValid(s)
    print(output, expectedOutput, output == expectedOutput)