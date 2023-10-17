# Problem:
# Given an array of numbers sorted in ascending order, find the range of a
# given number ‘key’. The range of the ‘key’ will be the first and last
# position of the ‘key’ in the array.
# 
# Write a function to return the range of the ‘key’. If the ‘key’ is not
# present return [-1, -1].
# 
# Examples:
# 
#   Input: [4, 6, 6, 6, 9], key = 6
#   Output: [1, 3]
# 
#   Input: [1, 3, 8, 10, 15], key = 10
#   Output: [3, 3]
# 
#   Input: [1, 3, 8, 10, 15], key = 12
#   Output: [-1, -1]
# 

class Solution:
    # Solution:
    # Use binary search to find the first and last instances of the given key
    # and return [first, last] as the output. Since binary search returns -1
    # if a key is not present in the array, this procedure will return [-1, -1]
    # if there is no range for the given key.
    #
    # Solution complexity:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def NumberRange(self, nums, key):
        return [self.FirstInstance(nums, key), self.LastInstance(nums, key)]

    def FirstInstance(self, nums, key):
        n = len(nums)
        
        left = 0
        right = n - 1

        first = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == key:
                first = mid
                right = mid - 1
                continue

            if nums[mid] < key:
                left = mid + 1

            if nums[mid] > key:
                right = mid - 1

        return first
    
    def LastInstance(self, nums, key):
        n = len(nums)

        left = 0
        right = n - 1

        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == key:
                last = mid
                left = mid + 1
                continue

            if nums[mid] < key:
                left = mid + 1

            if nums[mid] > key:
                right = mid -1 

        return last

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [4, 6, 6, 6, 9]
    key = 6
    expectedOutput = [1, 3]
    output = solution.NumberRange(nums, key)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [1, 3, 8, 10, 15]
    key = 10
    expectedOutput = [3, 3]
    output = solution.NumberRange(nums, key)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    nums = [1, 3, 8, 10, 15]
    key = 12
    expectedOutput = [-1, -1]
    output = solution.NumberRange(nums, key)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 4
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    key = 1
    expectedOutput = [0, 7]
    output = solution.NumberRange(nums, key)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()