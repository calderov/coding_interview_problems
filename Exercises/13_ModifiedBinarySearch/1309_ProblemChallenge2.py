# Problem:
# Given an array of numbers which is sorted in ascending order and also
# rotated by some arbitrary number, find if a given ‘key’ is present in it.
# 
# Write a function to return the index of the ‘key’ in the rotated array. If
# the ‘key’ is not present, return -1. You can assume that the given array
# does not have any duplicates.
# 
# Examples:
# 
#   Input: [10, 15, 1, 3, 8], key = 15
#   Output: 1
#   Explanation: '15' is present in the array at index '1'.
# 
#   Input: [4, 5, 7, 9, 10, -1, 2], key = 10
#   Output: 4
#   Explanation: '10' is present in the array at index '4'.
# 

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def FindKeyInRotatedArray(self, nums, key):
        # Find rotation point
        rotationPoint = self.FindRotationPosition(nums)
        
        # Search key in first half
        result = self.BinarySearch(nums[0 : rotationPoint + 1], key)
        if result != -1:
            return result
        
        # Search key in second half
        result = self.BinarySearch(nums[rotationPoint + 1: len(nums)], key)
        if result != -1:
            return rotationPoint + result + 1
        
        return -1


    def FindRotationPosition(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

    def BinarySearch(self, nums, key):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == key:
                return mid
            
            if nums[mid] < key:
                left = mid + 1

            else:
                right = mid - 1

        return -1 

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [10, 15, 1, 3, 8]
    key = 15
    expectedOutput = 1
    output = solution.FindKeyInRotatedArray(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [4, 5, 7, 9, 10, -1, 2]
    key = 10
    expectedOutput = 4
    output = solution.FindKeyInRotatedArray(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [4, 5, 6, 7, 0, 1, 2, 3]
    key = 0
    expectedOutput = 4
    output = solution.FindKeyInRotatedArray(nums, key)
    print(output, expectedOutput, output == expectedOutput)