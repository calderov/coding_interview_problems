# Problem:
# You are given a set of positive numbers and a target sum ‘S’. Each number
# should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways
# to assign symbols to make the sum of the numbers equal to the target ‘S’.
# 
# Examples:
# 
#   Input: {1, 1, 2, 3}
#   S = 1
#   Output: 3
#   Explanation: The given set has '3' ways to make a sum of '1': 
#               
#                1 - 1 - 2 + 3 = 1
#               
#               -1 + 1 - 2 + 3 = 1 
#               
#                1 + 1 + 2 - 3 = 1
#   
#   Input: {1, 2, 7, 1}
#   S = 9
#   Output: 2
#   Explanation: The given set has '2' ways to make a sum of '9':
#   
#                1 + 2 + 7 - 1 = 9
#   
#               -1 + 2 + 7 + 1 = 9

class Solution:
    # Solution:
    # This problem can be rephrased as "count the number of partitions P = P1 + P2 of the input array such that sum(P1) - sum(P2) = S".
    # In other words, the problem is asking us to find how to split the input into sets such that the sum of the members of one these
    # subsets equals S when we substract the sum of the members of the other subset.
    #
    # We can simplify this even further by considering the fact that sum(P1) + sum(P2) = T where T is the total sum of the elements in the
    # input array. Now, by adding both equations we get:
    #
    # (sum(P1) + sum(P2)) + (sum(P1) - sum(P2)) = T + S
    #
    # sum(P1) + sum(P2) + sum(P1) - sum(P2) = T + S
    #
    # 2 * sum(P1) = T + S
    #
    # sum(P1) = (T + S) / 2
    #
    # Thus, solving this last equation will answer to the original problem.
    # 
    # To do so, we can use dynamic programming to build a table dp where dp[i][j] keeps the number of subsets of the first i elements of
    # the input, that add up to the value j. This value j ranges from 0 to (T + S) / 2.
    #
    # Once the table is populated, return the value stored in the last cell of the table, as it contains how many subsets add to (T + S) / 2.
    # Or in the original terms, how many subset partitions are equal to S when the sum of one of the subsets is substracted from the sum of
    # the other subset.
    def CountOfSubsetsAddingToSByModifyingOperators(self, nums, s):
        # Return early if the problem can not be solved by this approach
        if (sum(nums) + s) % 2 != 0:
            return 0

        targetSum = (sum(nums) + s) // 2

        rows = len(nums)
        cols = targetSum + 1

        # Initialize 2D dynamic programming table
        dp = [[0 for col in range(cols)] for row in range(rows)]

        # Base case:
        for row in range(rows):
            dp[row][0] = 1
        
        # Base case:
        if nums[0] < cols:
            dp[0][nums[0]] = 1
        
        # For each cell in the dynamic programming table
        for row in range(1, rows):
            for col in range(1, cols):
                element = nums[row]

                # Case 1: Exclude element
                dp[row][col] += dp[row - 1][col]

                # Case 2: Include element if possible
                if col >= element:
                    dp[row][col] += dp[row - 1][col - element]

        # Return the last cell of the dynamic programming table
        return dp[-1][-1]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 1, 2, 3]
    s = 1
    expectedOutput = 3
    output = solution.CountOfSubsetsAddingToSByModifyingOperators(nums, s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 2, 7, 1]
    s = 9
    expectedOutput = 2
    output = solution.CountOfSubsetsAddingToSByModifyingOperators(nums, s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 1, 1, 1, 1]
    s = 2
    expectedOutput = 0
    output = solution.CountOfSubsetsAddingToSByModifyingOperators(nums, s)
    print(output, expectedOutput, output == expectedOutput)