# 215. Kth Largest Element in an Array (Medium)
# Given an integer array nums and an integer k, return the kth largest
# element in the array.
# 
# Note that it is the kth largest element in the sorted order, not the kth
# distinct element.
# 
# Can you solve it without sorting?
# 
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# 
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

from heapq import *

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def FindKthLargest(self, nums, k):
        if len(nums) < k:
            return None

        maxHeap = [-num for num in nums]
        heapify(maxHeap)

        for _ in range(k - 1):
            heappop(maxHeap)
        
        return -heappop(maxHeap)
        
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3,2,1,5,6,4]
    k = 2
    expectedOutput = 5
    output = solution.FindKthLargest(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expectedOutput = 4
    output = solution.FindKthLargest(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    