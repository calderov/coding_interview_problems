# Top 'K' Numbers (easy)
# Problem Statement
# 
# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
# 
# Note: For a detailed discussion about different approaches to solve this
# problem, take a look at Kth Smallest Number.
# 
# Example 1:
# 
# Input: [3, 1, 5, 12, 2, 11], K = 3
# Output: [5, 12, 11]
# 
# Example 2:
# 
# Input: [5, 12, 11, -1, 12], K = 3
# Output: [12, 11, 12]
# 

from heapq import *

class Solution:
    # Solution:
    # 1. Initialize a max heap.
    #  
    # 2. Populate the max heap with the values from the input.
    #  
    # 3. Extract k elements from the max heap and save them to a list (topK).
    #  
    # 4. Sort the topK list (optional).
    #  
    # 5. Return the list with the top k elements.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def GetTopKV1(self, nums, k):
        maxHeap = []

        for num in nums:
            heappush(maxHeap, -num)

        topK = [-heappop(maxHeap) for i in range(k)]
        
        topK.sort()
        
        return topK

    # Solution:
    # 1. Initialize a min heap.
    #    minHeap = []
    #
    # 2. Push the first k elements in the input array to the min heap.
    #
    # 3. Compare the rest of the elements in the input array with the
    #    top element of the heap (that with the minimum value). 
    #    If an element is greater than the top of the heap, pop the heap to remove
    #    the top, and push this element.
    #  
    # 4. Return the inner list of the heap.
    #
    # Solution complexity:
    # Time complexity: O(n log(k))
    # Space complexity: O(k)
    def GetTopKV2(self, nums, k):
        minHeap = []

        for i in range(k):
            heappush(minHeap, nums[i])

        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, nums[i])

        minHeap.sort() # Optional
        return minHeap

    def GetTopK(self, nums, k):
        return self.GetTopKV2(nums, k)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3, 1, 5, 12, 2, 11]
    k = 3
    expectedOutput = [5, 11, 12]
    output = solution.GetTopK(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [5, 12, 11, -1, 12]
    k = 3
    expectedOutput = [11, 12, 12]
    output = solution.GetTopK(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()