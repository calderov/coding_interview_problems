# Problem:
# For a given number N, write a function to generate all combination of N
# pairs of balanced parentheses.
# 
# Example 1:
# 
# Input: N=2
# Output: (()), ()()
# 
# Example 2:
# 
# Input: N=3
# Output: ((())), (()()), (())(), ()(()), ()()()
# 

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n * 2 ^ (2 * n))
    # Space complexity: O(n * 2 ^ (2 * n))
    def BalancedParentheses(self, n):
        if not n:
            return [""]

        permutations = []

        for i in range(2 ** (2 * n)):
            permutation = bin(i)[2:].zfill(2 * n)
            permutation = permutation.replace('0', '(')
            permutation = permutation.replace('1', ')')

            if self.IsBalanced(permutation):
                permutations.append(permutation)

        return permutations

    def IsBalanced(self, parentheses):
        stack = []
        for i in range(len(parentheses)):
            if parentheses[i] == '(':
                stack.append('(')
                continue

            if stack:
                stack.pop()
                continue
        
            return False

        return len(stack) == 0

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    n = 2
    expectedOutput = ["(())", "()()"]
    output = solution.BalancedParentheses(n)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    n = 3
    expectedOutput = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    output = solution.BalancedParentheses(n)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
