# Problem:
# Given an array of numbers and a number ‘k’, find the median of all the ‘k’
# sized sub-arrays (or windows) of the array.
# 
# Example:
# 
#   Input: nums = [1, 2, -1, 3, 5], k = 2
# 
#   Output: [1.5, 0.5, 1.0, 4.0]
# 
#   Explanation: Let's consider all windows of size ‘2’:
# 
#                [1, 2,  _, _, _] -> median is 1.5
#                [_, 2, -1, _, _] -> median is 0.5
#                [_, _, -1, 3, _] -> median is 1.0
#                [_, _,  _, 3, 5] -> median is 4.0
# 

from heapq import *

# Solution:
# 
# Solution complexity:
# Time complexity: O(k * n)
# Space complexity: O(k * n)
class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def Insert(self, num):
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        self.Rebalance()

    def Remove(self, num):
        if -num in self.maxHeap:
            index = self.maxHeap.index(-num)
            del self.maxHeap[index]
            heapify(self.maxHeap)

        if num in self.minHeap:
            index = self.minHeap.index(num)
            del self.minHeap[index]
            heapify(self.minHeap)

        self.Rebalance()

    def Rebalance(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
    
    def GetMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return float(-self.maxHeap[0])

    def GetKMedians(self, nums, k):
        medians = []

        # Insert k numbers in heaps
        for i in range(k):
            self.Insert(nums[i])

        # Compute the first median
        medians.append(self.GetMedian())

        # Compute subsequent medians
        left = 0
        right = k

        while right < len(nums):
            self.Remove(nums[left])
            self.Insert(nums[right])
            
            medians.append(self.GetMedian())

            left += 1
            right += 1
        
        return medians

if __name__ == "__main__":

    # Example 1
    solution = Solution()
    nums = [1, 2, -1, 3, 5]
    k = 2
    expectedOutput = [1.5, 0.5, 1.0, 4.0]
    output = solution.GetKMedians(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    solution = Solution()
    nums = [1, 2, -1, 3, 5]
    k = 3
    expectedOutput = [1.0, 2.0, 3.0]
    output = solution.GetKMedians(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    solution = Solution()
    nums = [5, 4, 3, 2, 1]
    k = 5
    expectedOutput = [3.0]
    output = solution.GetKMedians(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()