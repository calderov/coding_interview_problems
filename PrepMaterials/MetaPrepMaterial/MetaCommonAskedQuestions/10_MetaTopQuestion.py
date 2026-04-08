# 227. Basic Calculator II (Medium)
# Given a string s which represents an expression, evaluate this expression
# and return its value. 
# 
# The integer division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-231, 231 - 1].
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
#  
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# 
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# 
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#  
# Constraints:
# - 1 <= s.length <= 3 * 10 ^ 5
#
# - s consists of integers and operators ('+', '-', '*', '/') separated by some
#   number of spaces.
#
# - s represents a valid expression.
#
# - All the integers in the expression are non-negative integers in the range [0, 231 - 1].
#
# - The answer is guaranteed to fit in a 32-bit integer.

def applyOp(op, num, stack):
    if   op == "+": stack.append(num)
    elif op == "-": stack.append(-num)
    elif op == "*": stack.append(stack.pop() * num)
    elif op == "/": stack.append(int(stack.pop() / num))

def calculate(s):
    stack = []
    num = 0
    op = "+"

    for c in s:
        if c == " ":
            continue

        if c.isdigit():
            num = num * 10 + int(c)
            continue

        if c in "+-*/":
            applyOp(op, num, stack)
            num = 0
            op = c

    applyOp(op, num, stack)

    return sum(stack)

if __name__ == "__main__":
    # Example 1
    s = "3+2*2"
    expectedOutput = 7
    output = calculate(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    s = " 3/2 "
    expectedOutput = 1
    output = calculate(s)
    print(output, expectedOutput, output == expectedOutput)
 
    # Example 3
    s = " 3+5 / 2 "
    expectedOutput = 5
    output = calculate(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    s = "14-3/2"
    expectedOutput = 13
    output = calculate(s)
    print(output, expectedOutput, output == expectedOutput)
    