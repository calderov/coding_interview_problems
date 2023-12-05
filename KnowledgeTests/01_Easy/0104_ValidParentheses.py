# Problem:
# Determine if an input string containing only the characters '(', ')', '{',
# '}', '[', and ']' is valid. A string is considered valid if:
# 
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Each close bracket has a corresponding open bracket of the same type.
#
# Examples
# 
#   Input: "(]"
#   Expected Output: false
#   Justification: The opening parenthesis '(' is not closed by its
#                  corresponding closing parenthesis.
# 
#   Input: "{[]}"
#   Expected Output: true
#   Justification: The string contains pairs of opening and closing brackets in
#                  the correct order.
# 
#   Input: "[{]}"
#   Expected Output: false
#   Justification: The opening square bracket '[' is closed by a curly brace
#                  '}', which is incorrect.

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def IsValidParentheses(self, inputString):
        closingCharacters = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        openingCharacters = set(closingCharacters.keys())
        stack = []

        for i in range(len(inputString)):
            character = inputString[i]

            if character in openingCharacters:
                stack.append(closingCharacters[character])
                continue
            
            if not stack:
                return False
            
            if stack[-1] == character:
                stack.pop()
            else:
                return False

        return len(stack) == 0

if __name__ == "__main__":
    solution = Solution()

    inputString = "(]"
    expectedOutput = False
    output = solution.IsValidParentheses(inputString)
    print(output, expectedOutput, output == expectedOutput)

    inputString = "{[]}"
    expectedOutput = True
    output = solution.IsValidParentheses(inputString)
    print(output, expectedOutput, output == expectedOutput)

    inputString = "[{]}"
    expectedOutput = False
    output = solution.IsValidParentheses(inputString)
    print(output, expectedOutput, output == expectedOutput)