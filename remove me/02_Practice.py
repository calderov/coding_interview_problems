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
from sys import maxsize as INFINITE
from heapq import *

class Solution:
    def KthSmallestInSortedMatrix(self, matrix, k):
        n = len(matrix)

        # Initialize min heap with the values and positions
        # of the elementsat the start of each row
        minHeap = [(matrix[i][0], i, 0) for i in range(n)]
        heapify(minHeap)

        # Loop k - 1 times extracting the smallest element on the heap (the one at the top)
        # and replacing it by the element that follows it on the same row of the matrix
        for i in range(k - 1):
            val, row, col = heappop(minHeap)

            if col < n - 1:
                heappush(minHeap, (matrix[row][col + 1], row, col + 1))

        # In the end, the element at the top of the matrix should be the kth largest element
        return minHeap[0][0]

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