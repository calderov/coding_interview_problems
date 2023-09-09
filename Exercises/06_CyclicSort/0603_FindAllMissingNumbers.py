# Find all Missing Numbers (easy)
# Problem Statement
# 
# We are given an unsorted array containing numbers taken from the range 1 to
# n. The array can have duplicates, which means some numbers will be
# missing. Find all those missing numbers.
# 
# Examples:
# 
#   Input: [2, 3, 1, 8, 2, 3, 5, 1]
#   Output: 4, 6, 7
#   Explanation: The array should have all numbers from 1 to 8, due to
#   duplicates 4, 6, and 7 are missing.
# 
#   Input: [2, 4, 1, 2]
#   Output: 3
# 
#   Input: [2, 3, 2, 1]
#   Output: 4
# 

class Solution:
    # Solution:
    # 1. Make a set out of all the numbers from 1 to n where n = len(nums) + 1.
    # 
    # 2. Make a set ouf of all the numbers in the nums array.
    #
    # 3. Compute the difference between the set with all the numbers from 1 to n,
    #    and the set with all the numbers in nums.
    # 
    # 4. The resulting set should have all the numbers the range 1 to n that are
    #    mising from the nums array.
    # 
    # 5. Return the missing numbers.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def FindMissingNumbersV1(self, nums):
        return list(set([i for i in range(1, len(nums) + 1)]).difference(set(nums)))
    
    # Solution:
    # 1. Use cyclic sort to place the elements of the input array nums in their
    #    proper place, or duplicate elements in the place of the missing ones.
    #
    # 2. Initialize a list of missing numbers.
    #      missingNumbers = []
    #
    # 3. Traverse the input list (now semi-sorted) finding missing numbers (those
    #    where nums[i] != i + 1). When found, append them to the missing numbers
    #    list.
    #
    # 4. Return the list of missing numbers.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def FindMissingNumbersV2(self, nums):
        # Use cyclic sort to place all elements in their correct place and
        # duplicates in the place of missing values
        self.cyclicSort(nums)
        
        # Initialize a list of missing numbers
        missingNumbers = []

        # Traverse the input list (now semi-sorted)
        # finding missing numbers (those where nums[i] != i + 1).
        # When found, append them to the missing numbers list
        for i in range(len(nums)):
            if nums[i] != i + 1:
                missingNumbers.append(i + 1)
        
        # Return the list of missing numbers
        return missingNumbers

    # Given an array of n numbers in the range 1 to n (inclusive) sorts the array
    # in linear time. If the array contains duplicates and by extension is missing
    # items from the range, this algorithm places the duplicates in the places that
    # would correspond to the missing numbers.
    def cyclicSort(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == nums[nums[i] - 1]:
                i += 1
                continue
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]

    def FindMissingNumbers(self, nums):
        return self.FindMissingNumbersV2(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1set([i for i in range(len(nums) + 1)]).difference(set(nums))
    nums = [2, 3, 1, 8, 2, 3, 5, 1]
    expectedOutput = [4, 6, 7]
    output = solution.FindMissingNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [2, 4, 1, 2]
    expectedOutput = [3]
    output = solution.FindMissingNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    nums = [2, 3, 2, 1]
    expectedOutput = [4]
    output = solution.FindMissingNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = [1, 2, 1, 4, 5]
    expectedOutput = [3]
    output = solution.FindMissingNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5
    nums = [2, 3, 4, 1]
    expectedOutput = []
    output = solution.FindMissingNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 6
    nums = [3, 3, 3, 3, 3]
    expectedOutput = [1, 2, 4, 5]
    output = solution.FindMissingNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)
    
