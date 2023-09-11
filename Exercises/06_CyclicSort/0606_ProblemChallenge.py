# Problem: 
# We are given an unsorted array containing n numbers taken from the range
# 1 to n. The array originally contained all the numbers from 1 to n, but
# due to a data error, one of the numbers got duplicated which also resulted
# in one number going missing. Find both these numbers.
# 
# Examples:
# 
#   Input: [3, 1, 2, 5, 2]
#   Output: [2, 4]
#   Explanation: '2' is duplicated and '4' is missing.
# 
#   Input: [3, 1, 2, 3, 6, 4]
#   Output: [3, 5]
#   Explanation: '3' is duplicated and '5' is missing.
# 

class Solution:
    # Solution:
    # 1. Sort the nums array using cyclic sort, this will place all the
    # items in their correct place and the duplicates  where the missing
    # numbers from the  range 1 to n should be.
    # 
    # 2. Initialize a list of duplicates or missing numbers.
    #      dupeOrMissing = []
    # 
    # 3. Traverse the nums array, if at any index i, nums[i] != i + 1
    #    add nums[i] and 1 + 1 into the duplicates or missing numbers
    #    list.
    #
    # 4. Return the dupelicates or missing numbers list and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindTheCorruptPair(self, nums):
        self.CyclicSort(nums)
        
        dupeOrMissing = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                dupeOrMissing.append(nums[i])
                dupeOrMissing.append(i + 1)

        return dupeOrMissing

    # Given an array of n numbers in the range 1 to n (inclusive) sorts the array
    # in linear time. If the array contains duplicates and by extension is missing
    # items from the range, this algorithm places the duplicates in the places that
    # would correspond to the missing numbers.
    #
    # Time complexity: O(n)
    # Space complexity: O(1)
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

    # Example 1
    nums = [3, 1, 2, 5, 2]
    expectedOutput = [2, 4]
    output = solution.FindTheCorruptPair(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [3, 1, 2, 3, 6, 4]
    expectedOutput = [3, 5]
    output = solution.FindTheCorruptPair(nums)
    print(output, expectedOutput, output == expectedOutput)