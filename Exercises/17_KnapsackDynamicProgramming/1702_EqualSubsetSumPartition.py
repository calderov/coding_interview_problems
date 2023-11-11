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
    def CanPartition(self, nums):
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
    