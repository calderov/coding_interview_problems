# Find the Duplicate Number (easy)
# Problem Statement
# 
# We are given an unsorted array containing n + 1 numbers taken from the range
# 1 to n. The array has only one duplicate but it can be repeated multiple
# times. Find that duplicate number without using any extra space. You are,
# however, allowed to modify the input array.
# 
# Examples:
# 
#   Input: [1, 4, 4, 3, 2]
#   Output: 4
# 
#   Input: [2, 1, 3, 3, 5, 4]
#   Output: 3
# 
#   Input: [2, 4, 1, 4, 4]
#   Output: 4
# 

class Solution:
    # Solution:
    # Use cyclic to sort the array in place. Since cyclic sort is intended to
    # sort arrays of n elements on the range 1 to n (inclusive) and our input
    # has n + 1 elements in the same range, the algorithm will place all the
    # elements in their proper place and the move the duplicate to the end of
    # the array. Then return the end of the input array.
    # 
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindDuplicateValue(self, nums):
        self.cyclicSort(nums)
        return nums[-1]

    # Given an array of n numbers in the range 1 to n (inclusive) sorts the array
    # in linear time. If the array contains duplicates and by extension is missing
    # items from the range, this algorithm places the duplicates in the places that
    # would correspond to the missing numbers.
    #
    # Time complexity: O(n)
    # Space complexity: O(1)
    def cyclicSort(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i] # swap
                continue
            i += 1

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 4, 4, 3, 2]
    expectedOutput = 4
    output = solution.FindDuplicateValue(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [2, 1, 3, 3, 5, 4]
    expectedOutput = 3
    output = solution.FindDuplicateValue(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [2, 4, 1, 4, 4]
    expectedOutput = 4
    output = solution.FindDuplicateValue(nums)
    print(output, expectedOutput, output == expectedOutput)
