# Problem Statement
# Given a set of positive numbers, partition the set into two subsets with
# minimum difference between their subset sums and return the difference.
# 
# Examples:
# 
#   Input: {1, 2, 3, 9}
#   Output: 3
#   Explanation: We can partition the given set into two subsets where minimum
#                absolute difference between the sum of numbers is '3'. 
#                Following are the two subsets: {1, 2, 3} and {9}.
# 
#   Input: {1, 2, 7, 1, 5}
#   Output: 0
#   Explanation: We can partition the given set into two subsets where minimum
#                absolute difference between the sum of number is '0'.
#                Following are the two subsets: {1, 2, 5} and {7, 1}.
# 
#   Input: {1, 3, 100, 4}
#   Output: 92
#   Explanation: We can partition the given set into two subsets where minimum
#                absolute difference between the sum of numbers is '92'. 
#                Here are the two subsets: {1, 3, 4} and {100}.

class Solution:
    def MinimumSubsetSumDifference(self, nums):
        totalSum = sum(nums)
        halfSum = totalSum // 2

        dp = [[False for i in range(halfSum + 1)] for _ in range(len(nums) + 1)]

        for row in range(len(nums) + 1):
            dp[row][0] = True

        if nums[0] <= halfSum:
            dp[0][nums[0]] = True

        for row in range(1, len(nums)):
            for col in range(1, halfSum + 1):
                if dp[row - 1][col]:
                    dp[row][col] = dp[row - 1][col]
                    continue

                if col >= nums[row]:
                    dp[row][col] = dp[row - 1][col - nums[row]]
                
        subsetSum = 0
        for col in range(halfSum, -1, -1):
            if dp[len(nums) - 1][col]:
                subsetSum = col
                break

        complementSum = totalSum - subsetSum
        return abs(complementSum - subsetSum)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 9]
    expectedOutput = 3
    output = solution.MinimumSubsetSumDifference(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 2, 7, 1, 5]
    expectedOutput = 0
    output = solution.MinimumSubsetSumDifference(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 3, 100, 4]
    expectedOutput = 92
    output = solution.MinimumSubsetSumDifference(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [i for i in range(50)]
    expectedOutput = 1
    output = solution.MinimumSubsetSumDifference(nums)
    print(output, expectedOutput, output == expectedOutput)