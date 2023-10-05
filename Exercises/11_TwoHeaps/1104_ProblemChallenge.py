# Problem: 
# Given an array of intervals, find the next interval of each interval. In a
# list of intervals, for an interval 'i' its next interval 'j' will have the
# smallest 'start' greater than or equal to the 'end' of 'i'.
# 
# Write a function to return an array containing indices of the next interval
# of each input interval. If there is no next interval of a given interval,
# return -1. It is given that none of the intervals have the same start
# point.
# 
# Example:
# 
#   Input: Intervals [[2,3], [3,4], [5,6]]  
# 
#   Output: [1, 2, -1]  
# 
#   Explanation: The next interval of [2,3] is [3,4] having index '1'.
#                Similarly, the next interval of [3,4] is [5,6] having index '2'.
#                There is no next interval for [5,6] hence we have '-1'.
# 

from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def NextIntervals(self, intervals: list[Interval]):
        n = len(intervals)
        
        nextIntervals = [-1] * n
        maxStart = []
        maxEnd = []

        for i in range(n):
            heappush(maxStart, (-intervals[i].start, i))
            heappush(maxEnd, (-intervals[i].end, i))

        for _ in range(n):
            i_end, i = heappop(maxEnd)

            if -i_end <= -maxStart[0][0]:
                j_start, j = heappop(maxStart)

                while maxStart and -i_end <= -maxStart[0][0]:
                   j_start, j = heappop(maxStart)

                nextIntervals[i] = j

                heappush(maxStart, (j_start, j))

        return nextIntervals

def ListOfListsToIntervalsList(listOfLists):
    return [Interval(i[0], i[1]) for i in listOfLists]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    intervals = [[2,3], [3,4], [5,6]]  
    expectedOutput = [1, 2, -1]
    output = solution.NextIntervals(ListOfListsToIntervalsList(intervals))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    intervals = [[3,4], [1,5], [4,6]]  
    expectedOutput = [2, -1, -1]
    output = solution.NextIntervals(ListOfListsToIntervalsList(intervals))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

