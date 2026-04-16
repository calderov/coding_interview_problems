# Maximum Subarray
# MEDIUM
# https://scaleengineer.com/dsa/problems/maximum-subarray

# Description
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Constraints:
#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104

# Time: O(n ** 2)
# Space: O(1)
def MaximumSubarraySumBruteForce(nums):
    if not nums:
        return 0

    maxSum = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums) + 1):
            maxSum = max(maxSum, sum(nums[i:j]))

    return maxSum

# Time: O(n)
# Space: O(1)
def MaximumSubarraySumKadane(nums):
    if not nums:
        return 0
    
    globalMax = nums[0]
    currentMax = nums[0]

    for i in range(1, len(nums)):
        currentMax = max(currentMax + nums[i], nums[i])
        globalMax = max(globalMax, currentMax)
    
    return globalMax

def MaximumSubarraySum(nums):
    return MaximumSubarraySumKadane(nums)

if __name__=="__main__":
    # Example 1:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    expected = 6
    output = MaximumSubarraySum(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nums = [1]
    expected = 1
    output = MaximumSubarraySum(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    nums = [5,4,-1,7,8]
    expected = 23
    output = MaximumSubarraySum(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4:
    nums = [-2, -3, -1, -5]
    expected = -1
    output = MaximumSubarraySum(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5:
    nums = [0, -1, 0, -2, 0]
    expected = 0
    output = MaximumSubarraySum(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()
