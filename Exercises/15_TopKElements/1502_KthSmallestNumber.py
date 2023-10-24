# Problem:
# Given an unsorted array of numbers, find Kth smallest number in it.
# 
# Please note that it is the Kth smallest number in the sorted order, not the
# Kth distinct element.
# 
# Note: For a detailed discussion about different approaches to solve this
# problem, take a look at Kth Smallest Number.
# 
# Examples:
# 
# Input: [1, 5, 12, 2, 11, 5], K = 3
# Output: 5
# Explanation: The 3rd smallest number is '5', as the first two smaller
# numbers are [1, 2].
# 

from heapq import *

class Solution:
    # Solution:
    # 1. Initialize a max heap.
    #    maxHeap = []
    #
    # 2. Push the first k elements in the input array to the max heap.
    #
    # 3. Compare the rest of the elements in the input array with the
    #    top element of the max heap (that with the maximum value). 
    #    If an element is greater than the top of the heap, pop the heap to remove
    #    the top, and push this element.
    #  
    # 4. Return the top of the max heap.
    #
    # Solution complexity:
    # Time complexity: O(n log(k))
    # Space complexity: O(k)
    def KthSmallestNumber(self, nums, k):
        maxHeap = []

        for i in range(k):
            heappush(maxHeap, -nums[i])

        for i in range(k, len(nums)):
            if -nums[i] > maxHeap[0]:
                heappop(maxHeap)
                heappush(maxHeap, -nums[i])

        return -maxHeap[0]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 5, 12, 2, 11, 5]
    k = 3
    expectedOutput = 5
    output = solution.KthSmallestNumber(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 5, 12, 2, 11, 5]
    k = 4
    expectedOutput = 5
    output = solution.KthSmallestNumber(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [5, 12, 11, -1, 12]
    k = 3
    expectedOutput = 11
    output = solution.KthSmallestNumber(nums, k)
    print(output, expectedOutput, output == expectedOutput)

