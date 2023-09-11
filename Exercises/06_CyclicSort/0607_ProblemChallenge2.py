# Problem: 
# Given an unsorted array containing numbers, find the smallest missing
# positive number in it.
# 
# Note: Positive numbers start from '1'.
# 
# Example:
# 
#   Input: [-3, 1, 5, 4, 2]
#   Output: 3
#   Explanation: The smallest missing positive number is '3'
# 
#   Input: [3, -2, 0, 1, 2]
#   Output: 4

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def FindSmallestMissingPositiveNumberV1(self, nums):
        # Remove dupes and sort the array
        sortedNums = sorted(list(set(nums)))

        # Find smalles missing number
        i = 1
        for k in range(len(sortedNums)):
            # Skip negative numbers and zero
            if sortedNums[k] <= 0:
                continue

            # If the number at k is not expected, then break the loop as i is the the missing number. 
            if sortedNums[k] != i:
                break
            
            # Otherwise increment i by one
            i += 1

        # Return i (the missing number)
        return i
    
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(1)
    def FindSmallestMissingPositiveNumberV2(self, nums):
        self.CyclicSortExtended(nums)
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums)

    # Given an array of n numbers in the range 1 to n (inclusive) sorts the array
    # in linear time. If the array contains duplicates and by extension is missing
    # items from the range, this algorithm places the duplicates in the places that
    # would correspond to the missing numbers.
    #
    # This version of the algorithm allows numbers outside the [1, n] range (negatives, 
    # zero and numbers greater than n).
    #
    # Time complexity: O(n)
    # Space complexity: O(1)
    def CyclicSortExtended(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i] # swap
                continue
            i += 1

    def FindSmallestMissingPositiveNumber(self, nums):
        return self.FindSmallestMissingPositiveNumberV2(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [-3, 1, 5, 4, 2]
    expectedOutput = 3
    output = solution.FindSmallestMissingPositiveNumber(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [3, -2, 0, 1, 2]
    expectedOutput = 4
    output = solution.FindSmallestMissingPositiveNumber(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [3, 2, 5, 1]
    expectedOutput = 4
    output = solution.FindSmallestMissingPositiveNumber(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = [33, 37, 5]
    expectedOutput = 1
    output = solution.FindSmallestMissingPositiveNumber(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5
    nums = [1, 1, 2, 2, 3, 3]
    expectedOutput = 4
    output = solution.FindSmallestMissingPositiveNumber(nums)
    print(output, expectedOutput, output == expectedOutput)