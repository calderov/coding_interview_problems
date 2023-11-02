# Problem:
# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
# 
# Example 1:
# 
# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
# Output: 4
# Explanation: The 5th smallest number among all the arrays is 4, this can be
# verified from 
# the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
# 
# Example 2:
# 
# Input: L1=[5, 8, 9], L2=[1, 7], K=3
# Output: 7
# Explanation: The 3rd smallest number among all the arrays is 7.
# 

from heapq import *

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n log(k))
    # Space complexity: O(k)
    def foo(self, lists, k):
        minHeap = []
        for listId in range(len(lists)):
            heappush(minHeap, (lists[listId][0], listId, 0))

        kthSmallest = None
        while k:
            kthSmallest, listId, index = heappop(minHeap)

            if index + 1 < len(lists[listId]):
                heappush(minHeap, (lists[listId][index + 1], listId, index + 1))

            k -= 1

        return kthSmallest
            
        

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    lists = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
    k = 5
    expectedOutput = 4
    output = solution.foo(lists, k)
    print(output, expectedOutput, output == expectedOutput)
 
    # Example 2:
    lists = [[5, 8, 9], [1, 7]]
    k = 3
    expectedOutput = 7
    output = solution.foo(lists, k)
    print(output, expectedOutput, output == expectedOutput)
