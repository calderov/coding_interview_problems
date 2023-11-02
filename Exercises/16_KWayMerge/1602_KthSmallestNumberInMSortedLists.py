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
    # 1. For each of the lists, save the first item or the list, the index of the list,
    #   and the index of the first item of the list (zero) into a min heap. The min heap
    #   should minimize based on the first number on each list.
    #
    # 2. Set a variable to hold the kth smallest variable and initialize it to None.
    #
    # 3. While k > 0
    #
    #    3.1 Pop the item at the top of the min heap and extract the number, list of origin,
    #        and index in that list. Save the number to the variable intended to store the
    #        kth smallest number.
    #
    #    3.2 Take the next number form the origin list, and push it into the min heap with
    #        its corresponding pointer to the origin list and index
    # 
    #    3.3 Substract 1 from k and repeat step 3.
    # 
    # 5. Return the variable holding the kth smallest index and finish
    #
    # Solution complexity:
    # Time complexity: O(m log(k))
    # Space complexity: O(k)
    def KthSmallestNumberInMSortedLists(self, lists, k):
        # For each of the lists, save the first item or the list, the index of the list, 
        # and the index of the first item of the list (zero) into a min heap.
        # The min heap should minimize based on the first number on each list.
        minHeap = []
        for listId in range(len(lists)):
            heappush(minHeap, (lists[listId][0], listId, 0))

        # Set a variable to hold the kth smallest number and initialize it to None
        kthSmallest = None
        
        # While k > 0
        while k:
            # Pop the item at the top of the min heap and extract the number, list of origin, 
            # and index in that list. Save the number to the variable intended to store the
            # kth smallest number
            kthSmallest, listId, index = heappop(minHeap)

            # Take the next number form the origin list, and push it into the min heap 
            # with its corresponding pointer to the origin list and index
            if index + 1 < len(lists[listId]):
                heappush(minHeap, (lists[listId][index + 1], listId, index + 1))

            # Substract 1 from k
            k -= 1

        # Return the variable holding the kth smallest index and finish
        return kthSmallest
            
        

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    lists = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
    k = 5
    expectedOutput = 4
    output = solution.KthSmallestNumberInMSortedLists(lists, k)
    print(output, expectedOutput, output == expectedOutput)
 
    # Example 2:
    lists = [[5, 8, 9], [1, 7]]
    k = 3
    expectedOutput = 7
    output = solution.KthSmallestNumberInMSortedLists(lists, k)
    print(output, expectedOutput, output == expectedOutput)
