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
    # 1. Insert numbers into a min heap.
    #
    # 2. Initialize a list of numbers in range (those between the k1th and k2nd smallest numbers).
    #
    # 3. Traverse the numbers of the input list.
    #
    #    3.1 If the index of the current number is greater than k1 - 1 and less than k2 - 1,
    #        pop the top of the heap and append it to the list of numbers in range.
    #
    #    3.2 Otherwise, just pop the top of the list and discard that number.
    #
    # 4. Return the sum of the numbers in range and finish.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(k2 - k1)
    def SumOfElements(self, nums, k1, k2):
        # Insert numbers into a min heap
        minHeap = []
        for num in nums:
            heappush(minHeap, num)

        # Initialize a list of numbers in range (those between the k1th and k2nd smallest numbers)
        numbersInRange = []

        # Traverse the numbers of the input list
        for i in range(len(nums)):
            # If the index of the current number is greater than k1 - 1 and less than k2 - 1,
            # pop the top of the heap and append it to the list of numbers in range
            if i > k1 - 1 and i < k2 - 1:
                numbersInRange.append(heappop(minHeap))
                continue
            # Otherwise, just pop the top of the list and discard that number
            heappop(minHeap)

        # Return the sum of the numbers in range
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

