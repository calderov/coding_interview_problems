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

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def calculate(self, s):
        def applyOperator(operator, value, stack):
            if operator == "+": stack.append(value)
            if operator == "-": stack.append(-value)
            if operator == "*": stack.append(stack.pop() * value)
            if operator == "/": stack.append(int(stack.pop() / value))

        i = 0
        num = 0
        stack = []
        operator = "+"
        
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            if s[i] in "+-*/":
                applyOperator(operator, num, stack)
                num = 0
                operator = s[i]
            
            i += 1
        
        applyOperator(operator, num, stack)
        return sum(stack)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s = "3+2*2"
    expectedOutput = 7
    output = solution.calculate(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    s = " 3/2 "
    expectedOutput = 1
    output = solution.calculate(s)
    print(output, expectedOutput, output == expectedOutput)
 
    # Example 3
    s = " 3+5 / 2 "
    expectedOutput = 5
    output = solution.calculate(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    s = "14-3/2"
    expectedOutput = 13
    output = solution.calculate(s)
    print(output, expectedOutput, output == expectedOutput)
    