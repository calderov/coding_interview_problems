# First Missing Positive
# HARD
# https://scaleengineer.com/dsa/problems/first-missing-positive

# Description
# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


# Constraints:
#     1 <= nums.length <= 105
#     -2**31 <= nums[i] <= 2**31 - 1

# Time: O(n)
# Space: O(n)
def FirstMissingPositiveHashSet(nums):
    n = len(nums)
    seen = set(nums)
    for i in range(1, n + 1):
        if i not in seen:
            return i
    return n + 1

# Time: O(n)
# Space: O(1)
def FirstMissingPositiveCyclicSort(nums):
    n = len(nums)

    # Cyclic sort
    i = 0
    while i < n:
        correctIndex = nums[i] - 1
        if 1 <= nums[i] and nums[i] <= n and nums[i] != nums[correctIndex]:
            nums[i], nums[correctIndex] = nums[correctIndex], nums[i]
            continue
        i += 1

    # Find missing
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1


def FirstMissingPositive(nums):
    return FirstMissingPositiveCyclicSort(nums)

if __name__ == "__main__":
    # Example 1:
    nums = [1,2,0]
    expected = 3
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nums = [3,4,-1,1]
    expected = 2
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    nums = [7,8,9,11,12]
    expected = 1
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4
    nums = [2,1]
    expected = 3
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5
    nums = [1,1,0]
    expected = 2
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6
    nums = [-1,-2,-3]
    expected = 1
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7
    nums = [1,2,3,4,5]
    expected = 6
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4
    nums = [2,2,2]
    expected = 1
    output = FirstMissingPositive(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()
