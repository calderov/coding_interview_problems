# Problem:
# Given two sorted arrays in descending order, find ‘K’ pairs with the
# largest sum where each pair consists of numbers from both the arrays.
# 
# Example 1:
# 
# Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
# Output: [9, 3], [9, 6], [8, 6] 
# Explanation: These 3 pairs have the largest sum. No other pair has a sum
# larger than any of these.
# 
# Example 2:
# 
# Input: L1=[5, 2, 1], L2=[2, -1], K=3
# Output: [5, 2], [5, -1], [2, 2]
# 

from heapq import *

class Solution:
    # Solution:
    # 1. Let nums1 and nums2 be two sorted arrays.
    #
    # 2. Produce all the pairs (N_i, M_j) where i and j range from 0 to k, and store the 
    #    sum of each pair N_i + M_j into a min heap, as well as the values for N_i and M_j.
    #
    # 3. Extract k pairs from the min heap (N_i, M_j) and save them into a list.
    #
    # 4. Return the list with the k pairs, as these are the k pairs with the largest sums.
    #
    # Solution complexity:
    # Time complexity: O(k ^ 2 * log(k))
    # Space complexity: O(k)
    def KPairsWithLargestSums(self, N, M, k):
        minHeap = []

        for i in N[:k]:
            for j in M[:k]:
                heappush(minHeap, (-(i + j), i, j))

        kPairs = []
        while k:
            _, i, j = heappop(minHeap)
            kPairs.append([i, j])
            k -= 1

        return kPairs

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    l1 = [9, 8, 2]
    l2 = [6, 3, 1]
    k = 3
    expectedOutput = [[9, 6], [8, 6], [9, 3]]
    output = solution.KPairsWithLargestSums(l1, l2, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    l1 = [5, 2, 1]
    l2 = [2, -1]
    k = 3
    expectedOutput = [[5, 2], [2, 2], [5, -1]]
    output = solution.KPairsWithLargestSums(l1, l2, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()