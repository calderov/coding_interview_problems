# Problem:
# Given a sorted array of numbers, find if a given number ‘key’ is present in
# the array. Though we know that the array is sorted, we don’t know if it’s
# sorted in ascending or descending order. You should assume that the array
# can have duplicates.
# 
# Write a function to return the index of the ‘key’ if it is present in the
# array, otherwise return -1.
# 
# Examples:
# 
#  Input: [4, 6, 10], key = 10
#  Output: 2
# 
#  Input: [1, 2, 3, 4, 5, 6, 7], key = 5
#  Output: 4
# 
#  Input: [10, 6, 4], key = 10
#  Output: 0
# 
#  Input: [10, 6, 4], key = 4
#  Output: 2
# 

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def BinarySearch(self, nums, key):
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        ascending = nums[left] < nums[right]

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == key:
                return mid

            if nums[mid] < key:
                if ascending: left = mid + 1
                else: right = mid - 1
                continue

            if nums[mid] > key:
                if ascending: right = mid - 1
                else: left = mid + 1
                continue
            
        return -1

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [4, 6, 10]
    key = 10
    expectedOutput = 2
    output = solution.BinarySearch(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    nums = [1, 2, 3, 4, 5, 6, 7]
    key = 5
    expectedOutput = 4
    output = solution.BinarySearch(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3:
    nums = [10, 6, 4]
    key = 10
    expectedOutput = 0
    output = solution.BinarySearch(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4:
    nums = [10, 6, 4]
    key = 4
    expectedOutput = 2
    output = solution.BinarySearch(nums, key)
    print(output, expectedOutput, output == expectedOutput)
