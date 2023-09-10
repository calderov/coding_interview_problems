# Find all Duplicate Numbers (easy)
# Problem Statement
# 
# We are given an unsorted array containing n numbers taken from the range 1
# to n. The array has some numbers appearing twice, find all these duplicate
# numbers using constant space.
# 
# Examples:
# 
#   Input: [3, 4, 4, 5, 5]
#   Output: [4, 5]
# 
#   Input: [5, 4, 7, 2, 3, 5, 3]
#   Output: [3, 5]
# 

class Solution:
    # Solution:
    # 1. Sort the nums array using cyclic sort, this will place all the
    # items in their correct place and the duplicates  where the missing
    # numbers from the  range 1 to n should be.
    #
    # 2. Initialize a list of duplicates.
    #      dupes = []
    # 
    # 3. Traverse the nums array and add to the dupes list
    #    all the elements where nums[i] != i + 1
    #
    # 4. Return the dupes list and finish
    #
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def FindAllDuplicates(self, nums):
        self.CyclicSort(nums)

        dupes = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                dupes.append(nums[i])
        
        return dupes

    # Given an array of n numbers in the range 1 to n (inclusive) sorts the array
    # in linear time. If the array contains duplicates and by extension is missing
    # items from the range, this algorithm places the duplicates in the places that
    # would correspond to the missing numbers.
    def CyclicSort(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
                continue
            i += 1

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [3, 4, 4, 5, 5]
    expectedOutput = [5, 4]
    output = solution.FindAllDuplicates(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    nums = [5, 4, 7, 2, 3, 5, 3]
    expectedOutput = [3, 5]
    output = solution.FindAllDuplicates(nums)
    print(output, expectedOutput, output == expectedOutput)

