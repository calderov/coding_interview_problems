# Problem:
# You are given an array of strings tokens that represents an arithmetic
# expression in a Reverse Polish Notation.
# 
# Evaluate the expression. Return an integer that represents the value of the
# expression.
# 
# Note that:
# 1. The valid operators are '+', '-', '*', and '/'.
#
# 2. Each operand may be an integer or another expression.
#
# 3. The division between two integers always truncates toward zero.
#
# 4. There will not be any division by zero.
#
# 5. The input represents a valid arithmetic expression in a reverse polish
#    notation.
#
# 6. The answer and all the intermediate calculations can be represented in a
#    32-bit integer.
#  
# 
# Examples:
# 
#   Input: tokens = ["2","1","+","3","*"]
#   Output: 9
#   Explanation: ((2 + 1) * 3) = 9
# 
#   Input: tokens = ["4","13","5","/","+"]
#   Output: 6
#   Explanation: (4 + (13 / 5)) = 6
# 
#   Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#   Output: 22
#   Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#              = ((10 * (6 / (12 * -11))) + 17) + 5
#              = ((10 * (6 / -132)) + 17) + 5
#              = ((10 * 0) + 17) + 5
#              = (0 + 17) + 5
#              = 17 + 5
#              = 22
#  


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def EvaluateReversePolishExpression(self, tokens):
        stack = []

        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
                continue

            b = stack.pop()
            a = stack.pop()
            
            if t == "+":
                stack.append(a + b)

            elif t == "-":
                stack.append(a - b)

            elif t == "*":
                stack.append(a * b)

            elif t == "/":
                stack.append(int(a / b))

        return stack[0]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tokens = ["2","1","+","3","*"]
    expectedOutput = 9
    output = solution.EvaluateReversePolishExpression(tokens)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    tokens = ["4","13","5","/","+"]
    expectedOutput = 6
    output = solution.EvaluateReversePolishExpression(tokens)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    expectedOutput = 22
    output = solution.EvaluateReversePolishExpression(tokens)
    print(output, expectedOutput, output == expectedOutput)