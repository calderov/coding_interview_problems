# K Closest Points to Origin (Medium)
# You are given an 2-D array points where points[i] = [xi, yi] represents the
# coordinates of a point on an X-Y axis plane. You are also given an integer
# k.
# 
# Return the k closest points to the origin (0, 0).
# 
# The distance between two points is defined as the Euclidean distance
# (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
# 
# You may return the answer in any order.
# 
# Example 1:
#   Input: points = [[0,2],[2,2]], k = 1
#   Output: [[0,2]]
# 
# Example 2:
#   Input: points = [[0,2],[2,0],[2,2]], k = 2
#   Output: [[0,2],[2,0]]

from heapq import *

class Solution:
    def kClosest(self, points, k: int):
        closestPoints = [] # Max Heap

        for point in points:
            x, y = point
            d = x**2 + y**2

            heappush(closestPoints, (-d, point))

            if len(closestPoints) > k:
                heappop(closestPoints)

        return [point for d, point in closestPoints]
        

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    points = [[0,2],[2,2]]
    k = 1
    expectedOutput = [[0,2]]
    output = solution.kClosest(points, k)
    print(output)
    print(expectedOutput)
    print()
    
    # Example 2:
    points = [[0,2],[2,0],[2,2]]
    k = 2
    expectedOutput = [[0,2],[2,0]]
    output = solution.kClosest(points, k)
    print(output)
    print(expectedOutput)
    print()