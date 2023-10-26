# Problem:
# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers
# from the array such that we are left with maximum distinct numbers.
#
# Example:
#
#   Input: [7, 3, 5, 8, 5, 3, 3], and K=2
#   Output: 3
#
#   Explanation: We can remove two occurrences of 3 to be left with 3 distinct
#   numbers [7, 3, 8], we have to skip 5 because it is not distinct and occurred twice.
#   Another solution could be to remove one instance of '5' and '3' each to be
#   left with three distinct numbers [7, 5, 8], in this case, we have to skip 3
#   because it occurred twice.
#

from heapq import *

class Solution:
    # Solution:
    #
    # Solution complexity:
    # Time complexity:
    # Space complexity:
    def MaxDistinctElements(self, nums:list[int], k:int):
        # Find the frequencies of all the numbers
        frequencies = {}
        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1

        # Push all the numbers and their frequencies into a min heap (the min heap
        # should minimize on the frequency of the numbers).
        minHeap = []
        for num, freq in frequencies.items():
            heappush(minHeap, (freq, num))

        # Extract distinct items from the min heap in a greedy fashion
        # until the heap is empty or k reaches zero.
        distinct = []
        while minHeap and k:
            freq, num = heappop(minHeap)

            # If the frequency of the number is 1, then it is distinct by definition.
            # Add it to the 'distinct' list and loop back.
            if freq == 1:
                distinct.append(num)
                continue

            
            # If the frequency of the number is less or equal than k. Add the number
            # to the 'distinct' list and substract frequency - 1 from k and loop back.
            # This is akin to removing all the duplicates of a number from the original list.
            if freq <= k:
                distinct.append(num)
                k -= freq - 1
                continue

            # If the frequency is greater than k, check if the difference between the frequency
            # and k is equal to 1. If so, add the number to the 'distinct' list. In any case,
            # make k equal to zero.
            if freq > k:
                if freq - k == 1:
                    distinct.append(num)
                k = 0

        # If we have not removed k elements yet, remove those in excess from the distinct items list
        while k > 0 and distinct:
            distinct.pop()
            k -= 1

        return len(distinct)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [7, 3, 5, 8, 5, 3, 3]
    k = 2
    expectedOutput = 3
    output = solution.MaxDistinctElements(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    print()

    # Example 2
    nums = [3, 5, 12, 11, 12]
    k = 3
    expectedOutput = 2
    output = solution.MaxDistinctElements(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    print()

    # Example 3
    nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
    k = 2
    expectedOutput = 3
    output = solution.MaxDistinctElements(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    print()

    # Example 4
    nums = [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
    k = 3
    expectedOutput = 4
    output = solution.MaxDistinctElements(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    print()