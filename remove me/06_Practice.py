# Problem:
# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.
# 
# Examples:
# 
#   Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
#   Output: [2, 3], [5, 6], [7, 7]
#   Explanation: The output list contains the common intervals between the two
#   lists.
#  
#   Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
#   Output: [5, 7], [9, 10]
#   Explanation: The output list contains the common intervals between the two
#   lists.
# 

class Solution:
    def IntervalsIntersection(self, intervals1, intervals2):
        intersections = []

        i = 0
        j = 0

        while i < len(intervals1) and j < len(intervals2):
            intervalA = intervals1[i]
            intervalB = intervals2[j]

            intersection = self.GetIntersection(intervalA, intervalB)

            if intersection:
                intersections.append(intersection)

            if intervalA[1] < intervalB[1]:
                i += 1
            else:
                j += 1

        return intersections
    
    def IsOverlap(self, intervalA, intervalB):
        return intervalA[0] < intervalB[1] and intervalA[1] > intervalB[0]
        
    def GetIntersection(self, intervalA, intervalB):
        if not self.IsOverlap(intervalA, intervalB):
            return None

        intersectionStart = max(intervalA[0], intervalB[0])
        intersectionEnd = min(intervalA[1], intervalB[1])

        return [intersectionStart, intersectionEnd]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    intervals1 = [[1, 3], [5, 6], [7, 9]]
    intervals2 = [[2, 3], [5, 7]]
    expectedOutput = [[2, 3], [5, 6]]
    output = solution.IntervalsIntersection(intervals1, intervals2)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 2
    intervals1 = [[1, 3], [5, 7], [9, 12]]
    intervals2 = [[5, 10]]
    expectedOutput = [[5, 7], [9, 10]]
    output = solution.IntervalsIntersection(intervals1, intervals2)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
