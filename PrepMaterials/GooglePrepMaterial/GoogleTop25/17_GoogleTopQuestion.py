# Rotate Image
# MEDIUM
# https://scaleengineer.com/dsa/problems/rotate-image

# Description
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Input: matrix = [[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]
#
# Output:         [[7,4,1],
#                  [8,5,2],
#                  [9,6,3]]

# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Constraints:
#     n == matrix.length == matrix[i].length
#     1 <= n <= 20
#     -1000 <= matrix[i][j] <= 1000

def RotateMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix)

    # Transpose matrix in-place
    for row in range(rows):
        for col in range(row + 1, cols):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    # Reverse matrix in-place
    left = 0
    right = cols - 1

    while left < right:
        for row in range(rows):
            matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
        left += 1
        right -= 1

    return matrix

if __name__ == "__main__":
    # Example 1:
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [[7,4,1],[8,5,2],[9,6,3]]
    print(expected)
    output = RotateMatrix(matrix)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    print(expected)
    output = RotateMatrix(matrix)
    print(output)
    print(expected == output)
    print()