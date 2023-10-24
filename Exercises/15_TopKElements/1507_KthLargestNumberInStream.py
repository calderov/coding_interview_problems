# Problem Statement
# 
# Design a class to efficiently find the Kth largest element in a stream of
# numbers.
# 
# The class should have the following two things:
# 
#     The constructor of the class should accept an integer array containing
# initial numbers from the stream and an integer ‘K’.
#     The class should expose a function add(int num) which will store the
# given number and return the Kth largest number.
# 
# Example:
# 
#   Input: [3, 1, 5, 12, 2, 11], K = 4
#   1. Calling add(6) should return '5'.
#   2. Calling add(13) should return '6'.
#   2. Calling add(4) should still return '6'.
# 

from heapq import *

class Solution:
    # Solution:
    # Use a min heap to store the stream of numbers.
    # 
    # Each time a new number is added, push the number into the min heap.
    # If the length min heap is greater than k, pop the top of the min heap and discard it.
    # This will force the min heap to store at most k numbers. Return the top of the min heap (the kth
    # largest item).
    #
    # Solution complexity:
    # Time complexity: O(log(k))
    # Space complexity: O(k)
    def __init__(self, nums, k):
        self.minHeap = []
        self.k = k
        
        for num in nums:
            self.add(num)

    def add(self, num):
        heappush(self.minHeap, num)

        if len(self.minHeap) > k:
            heappop(self.minHeap)

        return self.minHeap[0]

if __name__ == "__main__":
    # Example 1
    nums = [3, 1, 5, 12, 2, 11]
    k = 4

    solution = Solution(nums, k)

    # 1. Calling add(6) should return '5'.
    expectedOutput = 5
    output = solution.add(6)
    print(output, expectedOutput, output == expectedOutput)

    # 2. Calling add(13) should return '6'.
    expectedOutput = 6
    output = solution.add(13)
    print(output, expectedOutput, output == expectedOutput)

    # 3. Calling add(4) should still return '6'.
    expectedOutput = 6
    output = solution.add(4)
    print(output, expectedOutput, output == expectedOutput)

