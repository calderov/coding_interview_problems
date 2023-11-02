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
    # Solution:
    # 1. For each row in the matrix, save the first number of the row, the row index
    #    and the column index (zero) into a min heap. This min heap should minimize
    #    based on the numbers extracted from the matrix.
    #
    # 2. Set a variable to hold the kth smallest number in the matrix and initialize
    #    it to None. Let's call it 'kthSmallest'.
    #
    # 3. While k > 0:
    #
    #    3.1 Pop the item at the top of the min heap and extract its encoded
    #        number, and its row and column of origin. Save the number in the
    #        kthSmallest variable.
    #
    #    3.2 If the retrieved column is still not the last, push the next the number
    #        at matrix[row][col + 1] into the min heap, as well as its row and column
    #        of origin. In this case, 'row' and 'col + 1'.
    #
    #    3.3 Substrat 1 from k and repeat step 3.
    #
    # 4. Return the 'kthSmallest' variable and finish
    #
    # Solution complexity:
    # Time complexity: O(N^2 log(N)) Note: I'm not sure on this complexity
    # Space complexity: O(N)
    def KthSmallestInSortedMatrix(self, matrix, k):
        # For each row in the matrix, save the first number of the row, the row index
        # and the column index (zero) into a min heap. This min heap should minimize
        # based on the numbers extracted from the matrix.
        minHeap = []
        for row in range(len(matrix)):
            heappush(minHeap, (matrix[row][0], row, 0))

        # Set a variable to hold the kth smallest number in the matrix and initialize
        # it to None. Let's call it 'kthSmallest'
        kthSmallest = None

        # While k > 0
        while k:
            # Pop the item at the top of the min heap and extract its encoded
            # number, and its row and column of origin. Save the number in the
            # kthSmallest variable
            kthSmallest, row, col = heappop(minHeap)

            # If the retrieved column is still not the last,
            # push the next the number at matrix[row][col + 1] into the
            # min heap, as well as its row and colum of origin. In this case,
            # 'row' and 'col + 1'
            if col < len(matrix[row]) + 1:
                heappush(minHeap, (matrix[row][col + 1], row, col + 1))

            # Substrat 1 from k
            k -= 1

        # Return the 'kthSmallest' variable and finish
        return kthSmallest
            

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