# Problem:
# Given an array, find the sum of all numbers between the K1’th and K2’th
# smallest elements of that array.
#
# Example:
#
#   Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
#   Output: 23
#   Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The
#   sum of numbers coming between 5 and 15 is 23 (11+12).
#

from heapq import *

class Solution:
    # Solution:
    #
    # Solution complexity:
    # Time complexity:
    # Space complexity:
    def SumOfElements(self, nums, k1, k2):
        minHeap = []

        for num in nums:
            heappush(minHeap, num)

        numbersInRange = []

        for i in range(len(nums)):
            if i > k1 - 1 and i < k2 - 1:
                numbersInRange.append(heappop(minHeap))
                continue

            heappop(minHeap)

        return sum(numbersInRange)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 3, 12, 5, 15, 11]
    k1 = 3
    k2 = 6
    expectedOutput = 23
    output = solution.SumOfElements(nums, k1, k2)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [3, 5, 8, 7]
    k1 = 1
    k2 = 4
    expectedOutput = 12
    output = solution.SumOfElements(nums, k1, k2)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 1, 1, 1, 1]
    k1 = 1
    k2 = 5
    expectedOutput = 3
    output = solution.SumOfElements(nums, k1, k2)
    print(output, expectedOutput, output == expectedOutput)

