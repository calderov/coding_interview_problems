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

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def MinAddToMakeValidV2(self, s):
        unpaired = 0
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
                unpaired += 1
                continue

            if c == ')':
                if stack:
                    stack.pop()
                    unpaired -= 1
                else:
                    unpaired += 1

        return unpaired
    
    def MinAddToMakeValidV1(self, s):
        missingOpen = 0
        missingClose = 0
        open = []

        for c in s:
            if c == '(':
                open.append(c)
                continue

            if c == ')':
                if open:
                    open.pop()
                else:
                    missingOpen += 1
        
        missingClose = len(open)
        return missingOpen + missingClose

    def MinAddToMakeValid(self, s):
        return self.MinAddToMakeValidV2(s)
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    s = "())"
    expectedOutput = 1
    output = solution.MinAddToMakeValid(s)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2:
    s = "((("
    expectedOutput = 3
    output = solution.MinAddToMakeValid(s)
    print(output, expectedOutput, output == expectedOutput)