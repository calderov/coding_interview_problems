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

# Time complexity: O(n log(n))
# Space complexity: O(n)
def findKthLargestV1(nums, k):
    if not nums or k < 1 or k > len(nums):
        return None
    
    maxHeap = [-n for n in nums]
    heapify(maxHeap)

    result = None
    for i in range(k):
        result = -heappop(maxHeap)

    return result

# Time complexity: O(n log(k))
# Space complexity: O(k)
def findKthLargestV2(nums, k):
    if not nums or k < 1 or k > len(nums):
        return None
    
    minHeap = []
    for num in nums:
        if len(minHeap) < k:
            heappush(minHeap, num)
        else:
            heappush(minHeap, num)
            heappop(minHeap)

    return minHeap[0]

def findKthLargest(nums, k):
    return findKthLargestV2(nums, k)
        
if __name__ == "__main__":
    # Example 1
    nums = [3,2,1,5,6,4]
    k = 2
    expectedOutput = 5
    output = findKthLargest(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    expectedOutput = 4
    output = findKthLargest(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    