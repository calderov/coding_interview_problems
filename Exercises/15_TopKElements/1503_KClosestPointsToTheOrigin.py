# Problem:
# Given an array of points in a 2D2D plane, find ‘K’ closest points to the
# origin.
# 
# Example:
# 
#   Input: points = [[1,2],[1,3]], K = 1
#   Output: [[1,2]]
#   Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
#   The Euclidean distance between (1, 3) and the origin is sqrt(10).
#   Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
#

from heapq import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()
    
    def distance_from_origin(self):
        return (self.x * self.x) + (self.y * self.y)

class Solution:
    # Solution:
    # 1. Initialize a max heap.
    #
    # 2. Insert the first k elements of the input array into the max heap.
    #
    # 3. Compare each of the remaining elements in the input with the top of the heap
    #    if the distance between a given element and the origin is less than the distance
    #    of the top of the heap to the origin, pop the top of the heap, and insert the
    #    given element into the heap. This will keep the heap populated with the k closest
    #    points during the traversal of the input array.
    # 
    # 4. Return the elements in the max heap.
    #
    # Solution complexity:
    # Time complexity: O(n log(k))
    # Space complexity: O(k) 
    def GetKClosestPoints(self, points, k):
        closestPoints = []

        for i in range(k):
            heappush(closestPoints, (-points[i].distance_from_origin(), points[i]))

        for i in range(k, len(points)):
            distance = points[i].distance_from_origin()
            if distance < -closestPoints[0][0]:
                heappop(closestPoints)
                heappush(closestPoints, (-distance, points[i]))
        
        return [i[1] for i in closestPoints]

def ToPoints(listOfLists):
    return [Point(i[0], i[1]) for i in listOfLists]

def ToLists(listOfPoints):
    return [[p.x, p.y] for p in listOfPoints]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    points = [[1,2],[1,3]]
    k = 1
    expectedOutput = [[1,2]]
    output = ToLists(solution.GetKClosestPoints(ToPoints(points), k))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    points = [[1, 3], [3, 4], [2, -1]]
    k = 2
    expectedOutput = [[1, 3], [2, -1]]
    output = ToLists(solution.GetKClosestPoints(ToPoints(points), k))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
