# Search in Rotated Sorted Array
# MEDIUM
# https://scaleengineer.com/dsa/problems/search-in-rotated-sorted-array

# Description
# There is an integer array nums sorted in ascending order (with distinct values). 

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and
# become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1

# Constraints:
#     1 <= nums.length <= 5000
#     -104 <= nums[i] <= 104
#     All values of nums are unique.
#     nums is an ascending array that is possibly rotated.
#     -104 <= target <= 104

# Time: O(log(n))
# Space: O(1)
def SearchInRotated(nums, target, low=None, high=None):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid

        # If left part is softed
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # If right side is sorted
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        
    return -1

if __name__ == "__main__":
    # Example 1:
    nums = [4,5,6,7,0,1,2]
    target = 0
    expected = 4
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nums = [4,5,6,7,0,1,2]
    target = 3
    expected = -1
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    nums = [1]
    target = 0
    expected = -1
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: Target at the beginning
    nums = [4,5,6,7,0,1,2]
    target = 4
    expected = 0
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Target at the end
    nums = [4,5,6,7,0,1,2]
    target = 2
    expected = 6
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: Minimal rotation (one element)
    nums = [2,1]
    target = 1
    expected = 1
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: No rotation (sorted array)
    nums = [1,2,3,4,5,6,7]
    target = 5
    expected = 4
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 8: Larger array with rotation in middle
    nums = [5,6,7,8,9,10,0,1,2]
    target = 8
    expected = 3
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 9: Larger array, target in rotated part
    nums = [5,6,7,8,9,10,0,1,2]
    target = 0
    expected = 6
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 10: Two element array
    nums = [3,1]
    target = 1
    expected = 1
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 11: Negative numbers with rotation
    nums = [-5,-4,-3,-2,-1,0,1,2]
    target = -4
    expected = 1
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 12: Large rotation (most elements are considered "rotated")
    nums = [8,9,10,0,1,2,3,4,5,6,7]
    target = 3
    expected = 6
    output = SearchInRotated(nums, target)
    print(expected)
    print(output)
    print(expected == output)
    print()
