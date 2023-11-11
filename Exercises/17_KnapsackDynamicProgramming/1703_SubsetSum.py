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
    def SubsetSum(self, nums, s):
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
