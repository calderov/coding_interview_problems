# Valid Parentheses
# EASY
# https://scaleengineer.com/dsa/problems/valid-parentheses

# Description
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#     Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Constraints:
#     1 <= s.length <= 104
#     s consists of parentheses only '()[]{}'.

# Time: O(n)
# Space: O(n)
def ValidParentheses(s):
    stack = []

    for c in s:
        if c in "([{":
            stack.append(c)
            continue

        if not stack:
            return False
        
        if stack[-1] == "(" and c == ")":
            stack.pop()
            continue
        
        if stack[-1] == "[" and c == "]":
            stack.pop()
            continue

        if stack[-1] == "{" and c == "}":
            stack.pop()
            continue

    return len(stack) == 0

if __name__=="__main__":
    # Example 1:
    s = "()"
    expected = True
    output = ValidParentheses(s)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    s = "()[]{}"
    expected = True
    output = ValidParentheses(s)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    s = "(]"
    expected = False
    output = ValidParentheses(s)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4:
    s = "([])"
    expected = True
    output = ValidParentheses(s)
    print(expected)
    print(output)
    print(expected == output)
    print()
