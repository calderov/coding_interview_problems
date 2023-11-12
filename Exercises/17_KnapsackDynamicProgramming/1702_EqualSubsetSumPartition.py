# Statement
# Given a set of positive integers, find if we can partition it into two
# subsets such that the sum of elements in both subsets is equal.
# 
# Examples:
# 
#   Input: {1, 2, 3, 4}
#   Output: True
#   Explanation: The given set can be partitioned into two subsets with equal
#                sum: {1, 4} & {2, 3}
# 
#   Input: {1, 1, 3, 4, 7}
#   Output: True
#   Explanation: The given set can be partitioned into two subsets with equal
#                sum: {1, 3, 4} & {1, 7}
# 
#   Input: {2, 3, 4, 6}
#   Output: False
#   Explanation: The given set cannot be partitioned into two subsets with equal sum.

class Solution:
    # Solution:
    # Generate subsets of the input until the sum of a subset S equals the sum
    # of all the elements in the input divided by two, as S' should also add to the
    # same sum. Speed up the computation by caching the sum of each explored subset S.
    #
    # Time complexity: O(n * T) where n is the number of elements in the input and T is the total sum of these elements
    # Space complexity: O(n * T)
    def CanPartitionV1(self, nums):
        if not nums:
            return True

        targetSum = sum(nums) / 2
        subsetsSumsCache = {tuple(): 0}

        for num in nums:
            subsets = list(subsetsSumsCache.keys())

            for subset in subsets:
                newSubset = list(subset) + [num]
                newSubsetSum = subsetsSumsCache[subset] + num

                if newSubsetSum == targetSum:
                    return True
                
                subsetsSumsCache[tuple(newSubset)] = newSubsetSum
        
        return False
    
    # Solution:
    # Use dynamic programming to set a table dp, where dp[i][j] keeps the number of subsets of the first i elements of the input
    # that add up to the value j which ranges from 0 to sum(nums) / 2.
    #
    # Build this table iteratively based on whether an element is included in a subset or not.
    #
    # Once the table is populated, return True if the value stored in the last cell of the table is greater than zero, as it contains
    # how many subsets add up to sum(nums) / 2.
    #
    # Solution complexity:
    # Time complexity: O(n * s)
    # Space complexity: O(n * s)
    def CanPartitionV2(self, nums):
        # Return early if the problem cannot be solved
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        # Compute target sum
        targetSum = totalSum // 2

        rows = len(nums)
        cols = targetSum + 1
        
        # Initialize 2D dynamic programming table (dp)
        dp = [[0 for col in range(cols)] for row in range(rows)]
    
        # Base case: There is always an empty subset for every set
        for row in range(rows):
            dp[row][0] = 1

        # Base case: A set k with just the first element of the input can always produce a sum(k) = nums[0]
        if nums[0] < cols:
            dp[0][nums[0]] = 1

        # For each cell in the dp table
        for row in range(1, rows):
            for col in range(1, cols):
                element = nums[row]

                # Case 1: Exclude element from count
                dp[row][col] += dp[row - 1][col]

                # Case 2: Include elemenet in count
                if col >= element:
                    dp[row][col] = dp[row - 1][col - element]

        return dp[-1][-1] > 0

    def CanPartition(self, nums):
        return self.CanPartitionV2(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 4]
    expectedOutput = True
    output = solution.CanPartition(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [1, 1, 3, 4, 7]
    expectedOutput = True
    output = solution.CanPartition(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    nums = [2, 3, 4, 6]
    expectedOutput = False
    output = solution.CanPartition(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 4
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expectedOutput = False
    output = solution.CanPartition(nums)
    print(output, expectedOutput, output == expectedOutput)
    