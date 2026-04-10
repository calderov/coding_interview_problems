# 3Sum Closest
# MEDIUM

# Description
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Example 2:
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

# Constraints:
#     3 <= nums.length <= 500
#     -1000 <= nums[i] <= 1000
#     -104 <= target <= 104

# Time: O(n ** 3)
# Space: O(1)
def threeSumBruteForce(nums, target):
    n = len(nums)
    closestSum = float("inf")

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == target:
                    return target
                if abs(target - currSum) < abs(target - closestSum):
                    closestSum = currSum
    
    return closestSum

# Time: O(n log(n)) + O(n ** 2) -> O(n ** 2)
# Space: O(1)
def threeSumBetter(nums, target):
    n = len(nums)
    nums.sort()

    closestSum = nums[0] + nums[1] + nums[2]

    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            currentSum = nums[i] + nums[left] + nums[right]

            if currentSum == target:
                return target
            
            if abs(target - currentSum) < abs(target - closestSum):
                closestSum = currentSum

            if currentSum < target:
                left += 1
            else:
                right -= 1
    
    return closestSum


def threeSum(nums, target):
    return threeSumBetter(nums, target)

if __name__ == "__main__":
    # Example 1:
    nums = [-1,2,1,-4]
    target = 1
    expected = 2
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nums = [0,0,0]
    target = 1
    expected = 0
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3: Exact match with target
    nums = [1, 2, 3, 4, 5]
    target = 9
    expected = 9  # 2 + 3 + 4 = 9
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: All negative numbers
    nums = [-5, -3, -2, -1]
    target = -6
    expected = -6  # -5 + -3 + 2 would give -6, but we pick -5 + -2 + -1 = -8
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print()

    # Example 5: Large target with positive numbers
    nums = [100, 200, 300, 400]
    target = 1000
    expected = 700  # 100 + 200 + 400 = 700
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print()

    # Example 6: Mix with zeros
    nums = [-10, -8, 0, 5, 9]
    target = 0
    expected = 0  # -10 + 0 + 9 = -1, but -8 + 0 + 5 = -3, but we need -1?
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print()

    # Example 7: Small array with minimum size
    nums = [1, 1, 1]
    target = 0
    expected = 3  # 1 + 1 + 1 = 3
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 8: Negative target
    nums = [-5, -4, -3, -2, -1]
    target = -9
    expected = -9  # -5 + -4 + 0 or -5 + -3 + -1 = -9
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print()

    # Example 9: Mixed signs with duplicates
    nums = [-2, -2, 0, 1, 2, 2]
    target = 5
    expected = 4  # 0 + 2 + 2 = 4
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print()

    # Example 10: Large difference from target
    nums = [1, 1, 1, 1]
    target = -100
    expected = 3  # 1 + 1 + 1 = 3
    output = threeSum(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()
