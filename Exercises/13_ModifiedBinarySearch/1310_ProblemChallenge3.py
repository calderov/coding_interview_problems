# Problem:
# Given an array of numbers which is sorted in ascending order and is rotated
# ‘k’ times around a pivot, find ‘k’.
# 
# You can assume that the array does not have any duplicates.
# 
# Examples:
# 
#   Input: [10, 15, 1, 3, 8]
#   Output: 2
#   Explanation: The array has been rotated 2 times.
#  
#   Input: [4, 5, 7, 9, 10, -1, 2]
#   Output: 5
#   Explanation: The array has been rotated 5 times.

class Solution:
    # Solution:
    # Traverse the nums array from beginning to end, comparing each element i with its next element i + 1.
    # if nums[i] > nums[i + 1], return i + 1. If the nums array has been fully traversed and no return has
    # happened yet, return 0, as it means that no rotation has been performed on the array.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def RotationCountV1(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i + 1
        return 0
    
    # Solution:
    #
    # Solution complexity:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def RotationCountV2(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[left] > nums[left + 1]:
                return left + 1

            if nums[left] == nums[mid]:
                left = mid + 1
            elif nums[left] < nums[mid]:
                left = mid
            else: # nums[left] > nums[mid]
                right = mid

        return (left + 1) % len(nums)
    
    def RotationCount(self, nums):
        return self.RotationCountV2(nums)
    

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [10, 15, 1, 3, 8]
    expectedOutput = 2
    output = solution.RotationCount(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [4, 5, 7, 9, 10, -1, 2]
    expectedOutput = 5
    output = solution.RotationCount(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 3, 8, 10]
    expectedOutput = 0
    output = solution.RotationCount(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = [10, 15, 1, 3, 8]
    expectedOutput = 2
    output = solution.RotationCount(nums)
    print(output, expectedOutput, output == expectedOutput)