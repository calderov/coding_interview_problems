# Problem:
# Given an array of numbers sorted in an ascending order, find the ceiling of
# a given number ‘key’. The ceiling of the ‘key’ will be the smallest element
# in the given array greater than or equal to the ‘key’.
# 
# Write a function to return the index of the ceiling of the ‘key’. If there
# isn’t any ceiling return -1.
# 
# Examples:
# 
# Input: [4, 6, 10], key = 6
# Output: 1
# Explanation: The smallest number greater than or equal to '6' is '6' having
# index '1'. 
# 
# Input: [4, 6, 10], key = 17
# Output: -1
# Explanation: There is no number greater than or equal to '17' in the given
# array.
# 

class Solution:
    def GetCeiling(self, nums, key):
        if not nums:
            return -1
        
        if nums[0] >= key:
            return 0

        left = 0
        right = len(nums) - 1

        prevMid = -1

        while left < right:
            mid = left + right // 2

            if nums[mid] == key:
                return mid

            if nums[mid] < key:
                left = mid + 1
            
            else: # nums[mid] > key:
                prevMid = mid
                right = mid - 1

        return prevMid

if __name__ == "__main__":
    solution = Solution()
    
    nums = [4, 6, 10]
    key = 6
    expectedOutput = 1
    output = solution.GetCeiling(nums, key)
    print(output, expectedOutput, output == expectedOutput)
    
    nums = [4, 6, 10]
    key = 17
    expectedOutput = -1
    output = solution.GetCeiling(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    