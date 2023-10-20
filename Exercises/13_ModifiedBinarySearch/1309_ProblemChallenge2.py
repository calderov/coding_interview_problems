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
    # 1. Find the rotation point (that point i where nums[i] > nums[i + 1])
    #
    # 2. Search key in first half (nums[0 : rotationPoint + 1]). If the key is present, 
    #    return its position and finish. Otherwise proceed to the next step.
    #
    # 3. Search key in second half (nums[rotationPoint + 1 : len(nums)]). If the key is present,
    #    add rotationPoint + 1 to its position and return it.
    #
    # 4. Return -1 as the key was not found in neither one of both halves.
    #
    # Solution complexity:
    # Time complexity: O(n)   // Note: As it is implemented here, finding the rotation point takes O(n) operations.
    #                                  Thus the overall complexity of this algorithm is O(n). Perhaps this step
    #                                  can be achieved in O(log(n))?
    # Space complexity: O(1)
    def FindKeyInRotatedArrayV1(self, nums, key):
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
    
    # Solution:
    # The problem follows the Binary Search pattern. We can use a similar
    # approach as discussed in Order-agnostic Binary Search and modify it similar
    # to Search Bitonic Array to search for the ‘key’ in the rotated array.
    # 
    # After calculating the middle, we can compare the numbers at indices start
    # and middle. This will give us two options:
    # 
    # 1. If arr[start] <= arr[middle], the numbers from start to middle are
    #    sorted in ascending order.
    # 
    # 2. Else, the numbers from middle+1 to end are sorted in ascending order.
    # 
    # Once we know which part of the array is sorted, it is easy to adjust our
    # ranges. For example, if option-1 is true, we have two choices:
    # 
    # 1. By comparing the ‘key’ with the numbers at index start and middle we
    #    can easily find out if the ‘key’ lies between indices start and middle; if
    #    it does, we can skip the second part => end = middle -1.
    # 
    # 2. Else, we can skip the first part => start = middle + 1.
    # 
    # Solution complexity:
    # Time complexity: O(lon(n))
    # Space complexity: O(1)
    def FindKeyInRotatedArrayV2(self, nums, key):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == key:
                return mid

            ascending = nums[start] <= nums[mid]

            if ascending:
                if key >= nums[start] and key < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if key > nums[mid] and key <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

    def FindKeyInRotatedArray(self, nums, key):
        return self.FindKeyInRotatedArrayV2(nums, key)

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