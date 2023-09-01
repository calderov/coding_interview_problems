# Problem: 
# Given a list of intervals, merge all the overlapping intervals to produce a
# list that has only mutually exclusive intervals.
# 
# Examples:
# 
#   Intervals: [[1,4], [2,5], [7,9]]
#   Output: [[1,5], [7,9]]
#   Explanation: Since the first two intervals [1,4] and [2,5] overlap, we
#   merged them into one [1,5].
# 
#   Intervals: [[6,7], [2,4], [5,9]]
#   Output: [[2,4], [5,9]]
#   Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them
#   into one [5,9].
# 
#   Intervals: [[1,4], [2,6], [3,5]]
#   Output: [[1,6]]
#   Explanation: Since all the given intervals overlap, we merged them into one.
  # 

class Solution:
    # Solution:
    # 1. Initialize a list to store the merged intervals.
    #      mergedIntervals = []
    # 
    # 2. Sort the intervals list by starting point. This will put intervals which
    #    are likely to be overlapping close to one another.
    #
    # 3. For each interval in the intervals list:
    #    3. 1 Check if the mergedIntervals list is empty, if it is add the interval to it.
    #         and go back to step 3.
    #
    #    3.2 Check if the interval overlaps with the last element of the mergedIntervals list.
    #        If so, replace the last item of the mergedIntervals list with the merge of
    #        it and the current interval:
    #           mergedIntervals[-1] = merge(mergedIntervals[-1], interval)
    
    #        Otherwise, append the interval to the mergedIntervals list and go back to step 3.
    #
    # 3. Return mergedIntervals.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def MergeIntervalsList(self, intervals):
        mergedIntervals = []
        intervals.sort()

        for interval in intervals:
            if not mergedIntervals or not self.IsOverlap(mergedIntervals[-1], interval):
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1] = self.Merge(mergedIntervals[-1], interval)
        
        return mergedIntervals

    def Merge(self, intervalA, intervalB):
        start = min(intervalA[0], intervalB[0])
        end = max(intervalA[1], intervalB[1])
        return [start, end]

    def IsOverlap(self, intervalA, intervalB):
        return intervalA[1] > intervalB[0] and intervalB[1] > intervalA[0]

if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    intervals = [[1,4], [2,5], [7,9]]
    expectedOutput = [[1,5], [7,9]]
    output = solution.MergeIntervalsList(intervals)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    intervals = [[6,7], [2,4], [5,9]]
    expectedOutput = [[2,4], [5,9]]
    output = solution.MergeIntervalsList(intervals)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    intervals = [[1,4], [2,6], [3,5]]
    expectedOutput = [[1,6]]
    output = solution.MergeIntervalsList(intervals)
    print(output, expectedOutput, output == expectedOutput)