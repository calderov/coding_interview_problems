# Problem:
# Given a list of non-overlapping intervals sorted by their start time,
# insert a given interval at the correct position and merge all necessary
# intervals to produce a list that has only mutually exclusive intervals.
# 
# Examples:
# 
#   Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
#   Output: [[1,3], [4,7], [8,12]]
#   Explanation: After insertion, since [4,6] overlaps with [5,7], we merged
#   them into one [4,7].
#   
#   Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
#   Output: [[1,3], [4,12]]
#   Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we
#   merged them into [4,12].
#   
#   Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
#   Output: [[1,4], [5,7]]
#   Explanation: After insertion, since [1,4] overlaps with [2,3], we merged
#   them into one [1,4].

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def toPair(self):
        return [self.start, self.end]

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
    
    @staticmethod
    def ToInterval(pair):
        return Interval(pair[0], pair[1])

class Solution:
    # Solution:
    # 1. Insert the new interval into the intervals list just after the last interval that starts before it.
    #
    # 2. Initialize a list to store the merged intervals.
    #      mergedIntervals = []
    #
    # 3. For each interval in the intervals list:
    #    3. 1 Check if the mergedIntervals list is empty, if it is add the interval to it.
    #         and go back to step 3.
    #
    #    3.2 Check if the interval overlaps with the last element of the mergedIntervals list.
    #        If so, replace the last item of the mergedIntervals list with the merge of
    #        it and the current interval:
    #           mergedIntervals[-1] = merge(mergedIntervals[-1], interval)
    #
    #        Otherwise, append the interval to the mergedIntervals list and go back to step 3.
    #
    # 4. Return mergedIntervals.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def InsertInterval(self, intervals, newInterval):
        for i in range(len(intervals)):
            if newInterval.start < intervals[i].start:
                intervals.insert(i, newInterval)
                break

        if newInterval not in intervals:
            intervals.append(newInterval)

        mergedIntervals = []

        for interval in intervals:
            if not mergedIntervals:
                mergedIntervals.append(interval)
                continue

            if self.IsOverlap(interval, mergedIntervals[-1]):
                mergedIntervals[-1] = self.Merge(interval, mergedIntervals[-1])
            else:
                mergedIntervals.append(interval)

        return mergedIntervals

    def IsOverlap(self, intervalA, intervalB):
        return intervalA.start < intervalB.end and intervalA.end > intervalB.start

    def Merge(self, intervalA, intervalB):
        start = min(intervalA.start, intervalB.start)
        end = max(intervalA.end, intervalB.end)
        return Interval(start, end)

if __name__ == "__main__":
    solution = Solution()
    ListOfPairs = Interval.ListOfPairs
    ListOfIntervals = Interval.ListOfIntervals
    ToInterval = Interval.ToInterval

    # Example 1
    intervals = [[1,3], [5,7], [8,12]]
    newInterval = [4,6]
    expectedOutput = [[1,3], [4,7], [8,12]]
    output = ListOfPairs(solution.InsertInterval(ListOfIntervals(intervals), ToInterval(newInterval)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 2
    intervals = [[1,3], [5,7], [8,12]]
    newInterval = [4,10]
    expectedOutput = [[1,3], [4,12]]
    output = ListOfPairs(solution.InsertInterval(ListOfIntervals(intervals), ToInterval(newInterval)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 3
    intervals = [[2,3],[5,7]]
    newInterval = [1,4]
    expectedOutput = [[1,4], [5,7]]
    output = ListOfPairs(solution.InsertInterval(ListOfIntervals(intervals), ToInterval(newInterval)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()