# Search a 2D Matrix
# MEDIUM
# https://scaleengineer.com/dsa/problems/search-a-2d-matrix

# Description
# You are given an m x n integer matrix matrix with the following two properties:
# - Each row is sorted in non-decreasing order.
# - The first integer of each row is greater than the last integer of the previous row.

# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 100
#     -10**4 <= matrix[i][j], target <= 10**4

def ValueInMatrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])

    # Use binary search to find candidate row
    low = 0
    high = rows - 1
    
    candidateRow = -1

    while low <= high:
        mid = low + (high - low) // 2

        if matrix[mid][0] <= target and target <= matrix[mid][cols - 1]:
            candidateRow = mid
            break

        if target < matrix[mid][0]:
            high = mid - 1
        else:
            low = mid + 1

    # Return early if no candidate row was found
    if candidateRow == -1:
        return False

    # Use binary search again to find target in candidate row
    low = 0
    high = cols - 1

    while low <= high:
        mid = low + (high - low) // 2

        if matrix[candidateRow][mid] == target:
            return True
        
        if target < matrix[candidateRow][mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False

if __name__ == "__main__":
    # Example 1:
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    expected = True
    output = ValueInMatrix(matrix, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    expected = False
    output = ValueInMatrix(matrix, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3: target is first element
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 1
    expected = True
    output = ValueInMatrix(matrix, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: target is last element
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 60
    expected = True
    output = ValueInMatrix(matrix, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: small matrix single row
    matrix = [[1,2,3,4,5]]
    target = 4
    expected = True
    output = ValueInMatrix(matrix, target)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: small matrix single column
    matrix = [[1],[3],[5],[7]]
    target = 5
    expected = True
    output = ValueInMatrix(matrix, target)
    print(expected)
    print(output)
    print(expected == output)
    print()