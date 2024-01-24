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
    # Time complexity: 
    # Space complexity: 
    def EvaluateReversePolishExpression(self, tokens):
        operators = ['+', '-', '*', '/']
        tokens.reverse()
        
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                tokens[i] = int(tokens[i])
        
        operands = []
        while len(tokens) > 1 or tokens[0] in operators:
            if tokens[-1] not in operators:
                operands.append(tokens.pop())
                continue

            operandB = operands.pop()
            operandA = operands.pop()
            operator = tokens.pop()

            if operator ==  '+':
                tokens.append(operandA + operandB)
                continue

            if operator == '-':
                tokens.append(operandA - operandB)
                continue

            if operator == '*':
                tokens.append(operandA * operandB)
                continue

            if operator == '/':
                tokens.append(int(operandA / operandB))
                continue
        
        return tokens[0]

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