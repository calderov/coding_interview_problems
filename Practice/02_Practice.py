# Problem Statement
# Given an N * N matrix where each row and column is sorted in ascending
# order, find the Kth smallest element in the matrix.
#
# Example:
#
#   Input: Matrix=[[2, 6, 8],
#                  [3, 7, 10],
#                  [5, 8, 11]]
#   K = 5
#   Output: 7
#   Explanation: The 5th smallest number in the matrix is 7.
#

from heapq import *

class Solution:
    def KthSmallestInSortedMatrix(self, matrix, k):
        minHeap = []
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                heappush(minHeap, matrix[row][col])

        for i in range(k - 1):
            heappop(minHeap)
        
        return heappop(minHeap)

if __name__ == "__main__":
    solution = Solution()

    #Example 1:
    matrix = [[2, 6, 8],
              [3, 7, 10],
              [5, 8, 11]]
    k = 5
    expectedOutput = 7
    output = solution.KthSmallestInSortedMatrix(matrix, k)
    print(output, expectedOutput, output == expectedOutput)