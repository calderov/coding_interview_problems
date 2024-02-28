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

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def minRemoveToMakeValid(self, inputString):
        validString = list(inputString)
        stack = []

        for i in range(len(inputString)):
            c = inputString[i]

            if c == "(":
                stack.append(i)
                continue
            
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    validString[i] = ""

        for i in stack:
            validString[i] = ""

        return "".join(validString)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    inputString= "lee(t(c)o)de)"
    expectedOutput = "lee(t(c)o)de"
    output = solution.minRemoveToMakeValid(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
 
    # Example 2
    inputString= "a)b(c)d"
    expectedOutput = "ab(c)d"
    output = solution.minRemoveToMakeValid(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    inputString= "))(("
    expectedOutput = ""
    output = solution.minRemoveToMakeValid(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()