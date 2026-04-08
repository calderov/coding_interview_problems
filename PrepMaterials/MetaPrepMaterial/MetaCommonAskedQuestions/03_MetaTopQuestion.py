# 1249. Minimum Remove to Make Valid Parentheses (Medium)
# Given a string s of '(' , ')' and lowercase English characters.
# 
# Your task is to remove the minimum number of parentheses ( '(' or ')', in
# any positions ) so that the resulting parentheses string is valid and
# return any valid string.
# 
# Formally, a parentheses string is valid if and only if:
# 
# - It is the empty string, contains only lowercase characters, or
# - It can be written as AB (A concatenated with B), where A and B are valid
#   strings, or
# - It can be written as (A), where A is a valid string.
#  
# 
# Example 1:
#   Input: s = "lee(t(c)o)de)"
#   Output: "lee(t(c)o)de"
#   Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
#   
# Example 2:
#   Input: s = "a)b(c)d"
#   Output: "ab(c)d"
#   
# Example 3:
#   Input: s = "))(("
#   Output: ""
#   Explanation: An empty string is also valid.
#  

def fixParentheses(inputString):
    output = list(inputString)
    stack = [] # Tracks the indexes of open parentheses

    for i in range(len(inputString)):
        c = inputString[i]

        if c.isalpha():
            continue

        if c == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                output[i] = ""

    for i in stack:
        output[i] = ""
    
    return "".join(output)

if __name__ == "__main__":
    # Example 1:
    s = "lee(t(c)o)de)"
    expected = "lee(t(c)o)de"
    output = fixParentheses(s)

    print(s)
    print(expected)
    print(output)
    print(output == expected)
    print()

    #   
    # Example 2:
    s = "a)b(c)d"
    expected = "ab(c)d"
    output = fixParentheses(s)

    print(s)
    print(expected)
    print(output)
    print(output == expected)
    print()
    #   
    # Example 3:
    s = "))(("
    expected = ""
    output = fixParentheses(s)

    print(s)
    print(expected)
    print(output)
    print(output == expected)
    print()
