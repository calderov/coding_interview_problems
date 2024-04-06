# 74. Search a 2D Matrix (Medium)
# You are given an m x n integer matrix matrix with the following two
# properties:
# 
# 1. Each row is sorted in non-decreasing order.
# 
# 2. The first integer of each row is greater than the last integer of the
#    previous row.
# 
# Given an integer target, return true if target is in matrix or false
# otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.
# 
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


class Solution:
    def searchVector(self, vector, target):
        low = 0
        high = len(vector) - 1

        while low <= high:
            mid = (low + high) // 2

            if vector[mid] == target:
                return mid

            if vector[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return -1

    # Time complexity: 
    # Space complexity: 
    def searchMatrix(self, matrix, target):
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2

            first, last = matrix[mid][0], matrix[mid][-1]
            if first <= target and target <= last:
                return self.searchVector(matrix[mid], target) != -1

            if target < first:
                high = mid - 1

            else: # target > last
                low = mid + 1

        return False
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    expectedOutput = True
    output = solution.searchMatrix(matrix, target)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    expectedOutput = False
    output = solution.searchMatrix(matrix, target)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    matrix = [[1]]
    target = 1
    expectedOutput = True
    output = solution.searchMatrix(matrix, target)
    print(output, expectedOutput, output == expectedOutput)