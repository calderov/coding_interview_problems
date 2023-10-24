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
    # Time complexity: 
    # Space complexity: 
    def foo(self, nums, k):
        maxHeap = []

        for num in nums:
            heappush(maxHeap, -num)

        topK = [-heappop(maxHeap) for i in range(k)]
        
        topK.sort()
        
        return topK

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3, 1, 5, 12, 2, 11]
    k = 3
    expectedOutput = [5, 11, 12]
    output = solution.foo(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [5, 12, 11, -1, 12]
    k = 3
    expectedOutput = [11, 12, 12]
    output = solution.foo(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()