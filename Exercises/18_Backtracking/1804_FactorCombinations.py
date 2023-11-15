# Problem:
# Numbers can be regarded as the product of their factors.
#
# For example:
#
#   8 = 2 x 2 x 2
#   8 = 2 x 4
#
# Given an integer n, return all possible combinations of its factors. You
# may return the answer in any order.
# Example 1:
#
# Input: n = 8
# Output: [[2, 2, 2], [2, 4]]
# Example 2:
#
# Input: n = 20
# Output: [[2, 2, 5], [2, 10], [4, 5]]

class Solution:
    def FactorCombinations(self, n):
        pass
        


if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    n = 8
    expectedOutput = [[2, 2, 2], [2, 4]]
    output = solution.FactorCombinations(n)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2:
    n = 20
    expectedOutput = [[2, 2, 5], [2, 10], [4, 5]]
    output = solution.FactorCombinations(n)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
