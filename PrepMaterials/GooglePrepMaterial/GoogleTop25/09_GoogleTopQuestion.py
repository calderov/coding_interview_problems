# 4Sum
# MEDIUM
# https://scaleengineer.com/dsa/problems/4sum

# Description
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

# Constraints:
#     1 <= nums.length <= 200
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109

# Time: O(n ** 4)
# Space = O(n)
def fourSumBruteForce(nums, target):
    n = len(nums)
    quadruplets = []

    for h in range(n):
        for i in range(h + 1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    quad = [nums[h], nums[i], nums[j], nums[k]]
                    quadSum = sum(quad)
                    if quadSum == target:
                        quad.sort() # Optional
                        if quad not in quadruplets:
                            quadruplets.append(quad)
    
    return quadruplets

# Time: O(n ** 3)
# Space: O(n)
def fourSumOptimal(nums, target):
    nums.sort()
    n = len(nums)
    result = []
    
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    # Skip duplicates for left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
    
    return result

def fourSum(nums, target):
    return fourSumBruteForce(nums, target)

if __name__ == "__main__":
    # Example 1:
    print("Example 1")
    nums = [1,0,-1,0,-2,2]
    target = 0
    expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()
    
    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    print("Example 2")
    nums = [2,2,2,2,2]
    target = 8
    expected = [[2,2,2,2]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3: No solution
    print("Example 3")
    nums = [1,2,3,4]
    target = 20
    expected = []
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: All negative numbers
    print("Example 4")
    nums = [-4,-3,-2,-1]
    target = -10
    expected = [[-4,-3,-2,-1]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Mixed with zeros
    print("Example 5")
    nums = [-2,-1,0,1,2]
    target = 0
    expected = [[-2,-1,1,2]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: Minimum array size
    print("Example 6")
    nums = [1,2,3,4]
    target = 10
    expected = [[1,2,3,4]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: Large numbers
    print("Example 7")
    nums = [100,200,300,400]
    target = 1000
    expected = [[100,200,300,400]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 8: Multiple solutions
    print("Example 8")
    nums = [-3,-2,-1,0,1,2,3]
    target = 0
    expected = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 9: Duplicates with different target
    print("Example 9")
    nums = [1,1,1,1,2,2,2,2]
    target = 6
    expected = [[1,1,2,2]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 10: Negative target
    print("Example 10")
    nums = [-5,-4,-3,-2,-1,0]
    target = -6
    expected = [[-3,-2,-1,0]]
    output = fourSum(nums, target)

    expected.sort()
    output.sort()

    print(target)
    print(expected)
    print(output)
    print(expected == output)
    print()
