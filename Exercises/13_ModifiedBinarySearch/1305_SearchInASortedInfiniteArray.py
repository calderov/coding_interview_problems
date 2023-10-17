# Problem:
# Given an infinite sorted array (or an array with unknown size), find if a
# given number ‘key’ is present in the array. Write a function to return the
# index of the ‘key’ if it is present in the array, otherwise return -1.
# 
# Since it is not possible to define an array with infinite (unknown) size,
# you will be provided with an interface ArrayReader to read elements of the
# array. ArrayReader.get(index) will return the number at index; if the
# array’s size is smaller than the index, it will return Integer.MAX_VALUE.
# 
# Example 1:
# 
#   Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
#   Output: 6
#   Explanation: The key is present at index '6' in the array.
# 
# Example 2:
# 
#   Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
#   Output: -1
#   Explanation: The key is not present in the array.
# 

import math

class Solution:
    # Solution:
    # Use a regular binary tree search, but instead of initializing the 'right' pointer to the
    # last position of the array (which by definitio does not exist in this case), have it
    # point to a position with a value that is greater or equal than the given key.
    #
    # Solution complexity:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def SearchInInfiniteArray(self, numsReader, key):
        left = 0
        right = 1

        # Point the 'right' pointer to a position with a value greater or equal than the key
        while numsReader.get(right) <= key:
            right *= 2

        first = -1
        while left <= right:
            mid = (left + right) // 2

            if numsReader.get(mid) == key:
                first = mid
                right = mid - 1
                continue
            
            if numsReader.get(mid) < key:
                left = mid + 1
            
            else: # numsReader.get(mid) > key
                right = mid - 1

        return first

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    key = 16
    expectedOutput = 6
    output = solution.SearchInInfiniteArray(ArrayReader(nums), key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    key = 11
    expectedOutput = -1
    output = solution.SearchInInfiniteArray(ArrayReader(nums), key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3:
    nums = [1, 3, 8, 10, 15]
    key = 15
    expectedOutput = 4
    output = solution.SearchInInfiniteArray(ArrayReader(nums), key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4:
    nums = [1, 3, 8, 10, 15]
    key = 200
    expectedOutput = -1
    output = solution.SearchInInfiniteArray(ArrayReader(nums), key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5
    nums = [1, 1, 1, 1, 1, 1, 1, 2]
    key = 1
    expectedOutput = 0
    output = solution.SearchInInfiniteArray(ArrayReader(nums), key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 6
    nums = [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    key = 16
    expectedOutput = 6
    output = solution.SearchInInfiniteArray(ArrayReader(nums), key)
    print(output, expectedOutput, output == expectedOutput)
    