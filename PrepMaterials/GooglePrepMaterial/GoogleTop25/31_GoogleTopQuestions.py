# Maximal Rectangle
# HARD
# https://scaleengineer.com/dsa/problems/maximal-rectangle

# Description
# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example 1:
# Input: matrix = [["1","0","1","0","0"],
#                  ["1","0","1","1","1"],
#                  ["1","1","1","1","1"],
#                  ["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.

# Example 2:
# Input: matrix = [["0"]]
# Output: 0

# Example 3:
# Input: matrix = [["1"]]
# Output: 1

# Constraints:
#     rows == matrix.length
#     cols == matrix[i].length
#     1 <= row, cols <= 200
#     matrix[i][j] is '0' or '1'.

# Time: O(n ** 2)
# Space: O(1)
def MaximalRectangleAreaInHistogramV1(histogram):
    maxArea = 0
    n = len(histogram)

    for i in range(n):
        area = histogram[i]

        j = i - 1
        while j >= 0 and histogram[j] >= histogram[i]:
            area += histogram[i]
            j -= 1

        j = i + 1
        while j < n and histogram[j] >= histogram[i]:
            area += histogram[i]
            j += 1

        maxArea = max(maxArea, area)

    return maxArea

# Time: O(n)
# Space: O(n)
def MaximalRectangleAreaInHistogramV2(heights):
    stack = []
    maxArea = 0
    
    n = len(heights)

    for i in range(n + 1):
        h = 0 if i == n else heights[i]
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        stack.append(i)

    return maxArea


def MaximalRectangleAreaInMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    maxHistogram = [[0] * cols for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            if row == 0:
                maxHistogram[row][col] = int(matrix[row][col])
                continue

            if matrix[row][col]:
                maxHistogram[row][col] = int(matrix[row][col]) + maxHistogram[row - 1][col]

    maxAreaInHistogram = -1
    for row in maxHistogram:
        maxAreaInHistogram = max(maxAreaInHistogram, MaximalRectangleAreaInHistogramV2(row))

    return maxAreaInHistogram

if __name__ == "__main__":
    # Example 1:
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    expected = 6
    output = MaximalRectangleAreaInMatrix(matrix)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    matrix = [["0"]]
    expected = 0
    output = MaximalRectangleAreaInMatrix(matrix)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    matrix = [["1"]]
    expected = 1
    output = MaximalRectangleAreaInMatrix(matrix)
    print(expected)
    print(output)
    print(expected == output)
    print()