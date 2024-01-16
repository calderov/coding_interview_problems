# Problem:
# Given an unsorted array containing numbers and a number k, find the first
# k missing positive numbers in the array.
#
# Examples:
#
#   Input: [3, -1, 4, 5, 5], k=3
#   Output: [1, 2, 6]
#   Explanation: The smallest missing positive numbers are 1, 2 and 6.
#
#   Input: [2, 3, 4], k=3
#   Output: [1, 5, 6]
#   Explanation: The smallest missing positive numbers are 1, 5 and 6.
#
#   Input: [-2, -3, 4], k=2
#   Output: [1, 2]
#   Explanation: The smallest missing positive numbers are 1 and 2.

class Solution:
    def FindKMissingNumbers(self, nums, k):
        if k < 1:
            return []

        self.CyclicSort(nums)        
        
        missingNumbers = []
        misplaced = set()

        i = 0
        while len(missingNumbers) < k:
            if i < len(nums):
                if nums[i] != i + 1:
                    missingNumbers.append(i + 1)
                    misplaced.add(nums[i])
            else:
                if i + 1 not in misplaced:
                    missingNumbers.append(i + 1)

            i += 1

        return missingNumbers
        
    def CyclicSort(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] > 0 and \
               nums[i] <= len(nums) and \
               nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
                continue
            i += 1

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3, -1, 4, 5, 5]
    k = 3
    expectedOutput = [1, 2, 6]
    output = solution.FindKMissingNumbers(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [2, 3, 4]
    k = 3
    expectedOutput = [1, 5, 6]
    output = solution.FindKMissingNumbers(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [-2, -3, 4]
    k = 2
    expectedOutput = [1, 2]
    output = solution.FindKMissingNumbers(nums, k)
    print(output, expectedOutput, output == expectedOutput)
