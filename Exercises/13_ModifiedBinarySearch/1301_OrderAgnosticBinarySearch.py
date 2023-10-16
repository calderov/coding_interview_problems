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
    # 1. Initialize 'left' and 'right' pointers.
    #    left = 0
    #    right = n - 1, where n is the length of the given array.
    #
    # 2. Check if the array is sorted in ascending order (or not).
    #    ascending = nums[left] < nums[rigth]
    #
    # 3. While the 'left' pointer is less than or equal to the 'right' pointer.
    #
    #   3.1 Compute the 'middle' pointer (that at the middle of the search window).
    #   
    #   3.2 If the item at the 'middle' is our desired key, return the 'middle' pointer.
    #
    #   3.3 If the item at the 'middle' is less than our desired key.
    #
    #     3.3.1 If the input array is sorted in ascending order, move the 'left' pointer
    #           one position to the right of the 'middle' pointer.
    #
    #     3.3.2 Otherwise, move the 'right' pointer one position to the left of the 'middle'
    #           pointer.
    #
    #   3.4 If the item at the 'middle' is greater than our desired key.
    #
    #     3.4.1 If the input array is sorted in ascending order, move the 'right' pointer
    #           one position to the left of the 'middle' pointer.
    #
    #     3.4.2 Otherwise, move the 'left' pointer one position to the right of the 'middle' pointer.
    #
    #   3.5 Repeat step 3 until 'left' == 'right'.
    #
    # 4. If the algorithm did not return anything on step 3 it means that the given key is not in the input
    #    array. If this is the case, return -1 and finish.
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def BinarySearch(self, nums, key):
        if not nums:
            return -1

        # Initialize 'left' and 'right' pointers
        left = 0
        right = len(nums) - 1

        # Check if the array is sorted in ascending order (or not)
        ascending = nums[left] < nums[right]

        # While the 'left' pointer is less than or equal to the 'right' pointer
        while left <= right:
            # Compute the middle pointer (that at the middle of the search window)
            mid = (right + left) // 2

            # If the item at the 'middle' is our desired key, return the 'middle' pointer
            if nums[mid] == key:
                return mid

            # If the item at the 'middle' is less than our desired key
            if nums[mid] < key:
                # If the input array is sorted in ascending order, move the 'left' pointer
                # one position to the right of the 'middle' pointer
                if ascending: left = mid + 1
                # Otherwise, move the 'right' pointer one position to the left of the
                # 'middle' pointer
                else: right = mid - 1
                continue

            # If the item at the 'middle' is greater than our desired key
            if nums[mid] > key:
                # If the input array is sorted in ascending order, move the 'right' pointer
                # one position to the left of the 'middle' pointer
                if ascending: right = mid - 1
                # Otherwise, move the 'left' pointer one position to the right of the 'middle' pointer
                else: left = mid + 1
                continue
        
        # Return -1 as the key given has not been found on the array up to this point
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
