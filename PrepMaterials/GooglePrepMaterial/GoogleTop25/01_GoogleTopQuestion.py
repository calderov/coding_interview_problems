# Two Sum
# EASY
# https://scaleengineer.com/dsa/problems/two-sum

# Description
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def TwoSum(nums):
    n = len(nums)
    seen = {}

    for i in range(n):
        num = nums[i]
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
        

if __name__ == "__main__":
    # Example 1:
    nums = [2,7,11,15]
    target = 9
    expected = [0,1]
    output = TwoSum(nums)
    print(expected)
    print(output)
    print(expected == output)

    print()

    # Example 2:
    nums = [3,2,4]
    target = 6
    expected = [1,2]
    output = TwoSum(nums)
    print(expected)
    print(output)
    print(expected == output)
