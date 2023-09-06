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

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    @staticmethod
    def ListOfIntervals(listOfPairs):
        intervals = []
        for pair in listOfPairs:
            intervals.append(Interval(pair[0], pair[1]))
        return intervals
    
    @staticmethod
    def ListOfPairs(intervals):
        listOfPairs = []
        for interval in intervals:
            listOfPairs.append([interval.start, interval.end])
        return listOfPairs

class Solution:
    # Solution:
    # Brute force, compare all intervals in the first and second list and
    # create a third list with the intersections.
    # 
    # Solution complexity:
    # Time complexity: O(n * m)
    # Space complexity: O(n)
    def IntervalsIntersectionsV1(self, intervals1, intervals2):
        intersectionList = []

        for i in range(len(intervals1)):
            for j in range(len(intervals2)):
                intersection = self.Intersection(intervals1[i], intervals2[j])
                if intersection:
                    intersectionList.append(intersection)
        
        return intersectionList
    
    # Solution:
    # Iterate through both lists together to see if any two intervals overlap. 
    # If so intervals overlap, insert the overlapped part into a result list 
    # and move on to the next interval which is finishing early.
    # 
    # Solution complexity:
    # Time complexity: O(n + m)
    # Space complexity: O(n)
    def IntervalsIntersectionsV2(self, intervals1, intervals2):
        intersectionList = []

        i = 0
        j = 0
        while i < len(intervals1) and j < len(intervals2):
            if self.IsOverlap(intervals1[i], intervals2[j]):
                intersectionList.append(self.Intersection(intervals1[i], intervals2[j]))
            
            if intervals1[i].end < intervals2[j].end:
                i += 1
            else:
                j += 1
                
        return intersectionList
    
    def IntervalsIntersections(self, intervals1, intervals2):
        return self.IntervalsIntersectionsV2(intervals1, intervals2)
    
    def Intersection(self, intervalA, intervalB):
        if self.IsOverlap(intervalA, intervalB):
            start = max(intervalA.start, intervalB.start)
            end = min(intervalA.end, intervalB.end)
            return Interval(start, end)
        return None

    def IsOverlap(self, intervalA, intervalB):
        return not (intervalA.end < intervalB.start or intervalB.end < intervalA.start)

if __name__ == "__main__":
    solution = Solution()
    ListOfIntervals = Interval.ListOfIntervals
    ListOfPairs = Interval.ListOfPairs

    # Example 1:
    intervals1 = [[1, 3], [5, 6], [7, 9]]
    intervals2 = [[2, 3], [5, 7]]
    expectedOutput = [[2, 3], [5, 6], [7, 7]]
    output = ListOfPairs(solution.IntervalsIntersections(ListOfIntervals(intervals1), ListOfIntervals(intervals2)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 2:
    intervals1 = [[1, 3], [5, 7], [9, 12]]
    intervals2 = [[5, 10]]
    expectedOutput = [[5, 7], [9, 10]]
    output = ListOfPairs(solution.IntervalsIntersections(ListOfIntervals(intervals1), ListOfIntervals(intervals2)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()