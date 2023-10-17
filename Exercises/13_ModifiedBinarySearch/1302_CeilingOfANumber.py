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
    # Solution:
    # 1. Return 0 if the first element of the sorted array is greater
    #    than or equal to the given key.
    #
    # 2. Initialize 'left' and 'right' pointers.
    #    left = 0
    #    right = len(nums) - 1
    #
    # 3. Initialize the 'prevMid' pointer, to keep track of the smallest item
    #    on the array that is greater than or less than the given key.
    #    prevMid = -1
    #
    # 4. While the 'left' pointer is less than or equal to the 'right' pointer.
    #
    #   4.1 Compute the 'middle' pointer (it should stand between 'left' and 'right').
    #
    #   4.2 If the element at the 'middle' is equal to our given key, return 'middle' and finish.
    #
    #   4.3 If the item at 'middle' is less than the given key, move 'left' one position to the right of 'middle'.
    #
    #   4.4 If the item at 'middle' is greater than the given key, save the 'middle' pointer as 'prevMid' and move
    #       the 'right' pointer one position to the left of 'middle'.
    #
    # 5. Return 'prevMid' and finish 
    #
    # Solution complexity:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def CeilingOfANumber(self, nums, key):
        # Return early if the first element of the sorted array is greater
        # than or equal to the given key
        if nums[0] >= key:
            return 0
        
        # Initialize 'left' and 'right' pointers
        left = 0
        right = len(nums) - 1

        # Initialize the 'prevMid' pointer, it will keep track of the smallest item
        # on the array that is greater than or less than the given key
        prevMid = -1

        # While the 'left' pointer is less than or equal to the 'right' pointer
        while left <= right:
            # Compute the 'middle' pointer (it should stand between 'left' and 'right')
            mid = (right + left) // 2

            # If the element at the 'middle' is equal to our given key, return 'middle' and finish
            if nums[mid] == key:
                return mid

            # If the item at 'middle' is less than the given key, move 'left' one position to the right of 'middle'
            if nums[mid] < key:
                left = mid + 1

            # If the item at 'middle' is greater than the given key, save the 'middle' pointer as 'prevMid' and
            # move the 'right' pointer one position to the left of 'middle'
            if nums[mid] > key:
                prevMid = mid
                right = mid - 1
        
        # Return 'prevMid' and finish
        return prevMid

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [4, 6, 10]
    key = 6
    expectedOutput = 1
    output = solution.CeilingOfANumber(nums, key)
    print(output, expectedOutput, output == expectedOutput)
  
    # Example 2
    nums = [1, 3, 8, 10, 15]
    key = 12
    expectedOutput = 4
    output = solution.CeilingOfANumber(nums, key)
    print(output, expectedOutput, output == expectedOutput)
  
    # Example 3
    nums = [4, 6, 10]
    key = 17
    expectedOutput = -1
    output = solution.CeilingOfANumber(nums, key)
    print(output, expectedOutput, output == expectedOutput)
  
    # Example 4
    nums = [4, 6, 10]
    key = -1
    expectedOutput = 0
    output = solution.CeilingOfANumber(nums, key)
    print(output, expectedOutput, output == expectedOutput)
