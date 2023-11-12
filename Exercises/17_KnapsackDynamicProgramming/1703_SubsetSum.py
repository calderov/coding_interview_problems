# Problem Statement
# Given a set of positive numbers, determine if a subset exists whose sum is
# equal to a given number ‘S’.
# 
# Examples:
# 
#   Input: {1, 2, 3, 7}, S=6
#   Output: True
#   Explanation: The given set has a subset whose sum is '6': {1, 2, 3}
# 
#   Input: {1, 2, 7, 1, 5}, S=10
#   Output: True
#   Explanation: The given set has a subset whose sum is '10': {1, 2, 7}
# 
#   Input: {1, 3, 4, 8}, S=6
#   Output: False
#   Explanation: The given set does not have any subset whose sum is equal to '6'.

class Solution:
    # Solution:
    # Generate subsets of the input until the sum of a subset S equals the target sum S
    # Speed up the computation by caching the sum of each explored subset S.
    #
    # Time complexity: O(n * T) where n is the number of elements in the input and T is the target sum of these elements
    # Space complexity: O(n * T)
    def SubsetSumV1(self, nums, s):
        subsetsSumCache = {tuple(): 0}

        for num in nums:
            subsets = list(subsetsSumCache.keys())

            for prevSubset in subsets:
                subset = list(prevSubset) + [num]
                subsetSum = subsetsSumCache[prevSubset] + num

                if subsetSum == s:
                    return True
                
                subsetsSumCache[tuple(subset)] = subsetSum

        return False
    
    # Solution:
    # Use dynamic programming to set a table dp, where dp[i][j] keeps the number of subsets of the first i elements of the input, that add up to the value j which ranges from 0 to S.
    # Build this table iteratively based on whether an element is included in a subset or not.
    #
    # Once the table is populated, return if the value stored in the last cell of the table is greater than zero, as it contains how many subsets add to S.
    #
    # Solution complexity:
    # Time complexity: O(n * s)
    # Space complexity: O(n * s)
    def SubsetSumV2(self, nums, s):
        rows = len(nums)
        cols = s + 1

        # Initialize the dynamic programming table (dp)
        dp = [[0 for col in range(cols)] for row in range(rows)]

        # Base case: Mark the fist colum as the every set has an empty set 
        #            that adds up to zero.
        for row in range(rows):
            dp[row][0] = 1

        # Base case: A set containing only the first element from nums
        #            can add up to the value of the first element of nums,
        #            mark its corresponding colum.
        if nums[0] < cols:
            dp[0][nums[0]] = 1
        
        # For each cell on the dynamic programming table
        for row in range(1, rows):
            for col in range(1, cols):
                element = nums[row]

                # Case 1: Exclude the current element
                dp[row][col] += dp[row - 1][col]

                # Case 2: Include the current element
                if col >= element:
                    dp[row][col] += dp[row - 1][col - element]
    
        # The amount of subsets that add up to S is located
        # in the last cell of the dynamic programming table
        return dp[-1][-1] > 0

    def SubsetSum(self, nums, s):
        return self.SubsetSumV2(nums, s)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 7]
    s = 6
    expectedOutput = True
    output = solution.SubsetSum(nums, s)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [1, 2, 7, 1, 5]
    s = 10
    expectedOutput = True
    output = solution.SubsetSum(nums, s)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    nums = [1, 3, 4, 8]
    s = 6
    expectedOutput = False
    output = solution.SubsetSum(nums, s)
    print(output, expectedOutput, output == expectedOutput)
