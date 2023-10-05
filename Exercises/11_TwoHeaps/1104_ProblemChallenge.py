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
    # 1. Initialize results array.
    #    nextIntervals = [-1] * n
    #
    # 2. Initialize max heaps to track start times, end times and their corresponding indexes.
    #    maxStart = []
    #    maxEnd = []
    #
    # 3. Populate maxStart and maxEnd heaps.
    #
    # 4. Go through all the intervals to find each interval's next interval.
    #
    #    4.1 Let i be the index of the interval with the latest end time in the maxEnd heap.
    #
    #    4.2 If interval[i] ends before than, or at the same time as the interval with the latest
    #        start date in maxStart (lets call it interval[j]), then interval[j] is a candidate
    #        to be the next interval after interval[i].
    #
    #       4.2.1 Loop through the elements in maxStart to see if there is a better candidate.
    #
    #       4.2.2 Register the best j as the next interval.
    #
    #       4.2.3 Put the interval[j] back in the maxStart heap as it could be the next interval of
    #             another interval.
    #
    #       4.2.4 Return the list of next intervals and finish.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def NextIntervals(self, intervals: list[Interval]):
        n = len(intervals)
        
        # Initialize results array
        nextIntervals = [-1] * n

        # Initialize max heaps to track start times, end times
        # and their corresponding indexes
        maxStart = []
        maxEnd = []

        # Populate maxStart and maxEnd heaps
        for i in range(n):
            heappush(maxStart, (-intervals[i].start, i))
            heappush(maxEnd, (-intervals[i].end, i))

        # Go through all the intervals to find each interval's next interval
        for _ in range(n):
            # Let i be the index of the interval with the latest end time in the maxEnd heap
            i_end, i = heappop(maxEnd)

            # If interval[i] ends before than, or at the same time as the interval with the latest
            # start date in maxStart (lets call it interval[j]), then interval[j] is a candidate
            # to be the next interval after interval[i]
            if -i_end <= -maxStart[0][0]:
                # Loop through the elements in maxStart to see if there is a better candidate
                j_start, j = heappop(maxStart)
                while maxStart and -i_end <= -maxStart[0][0]:
                   j_start, j = heappop(maxStart)
                # Register the best j as the next interval
                nextIntervals[i] = j

                # Put the interval[j] back in the maxStart heap as it could be the next interval of
                # another interval
                heappush(maxStart, (j_start, j))

        # Return the list of next intervals and finish
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

