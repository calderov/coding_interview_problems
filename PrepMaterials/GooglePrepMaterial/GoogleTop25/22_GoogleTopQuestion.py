# Insert Interval
# MEDIUM
# https://scaleengineer.com/dsa/problems/insert-interval

# Description
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end
# of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end]
# that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have
# any overlapping intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# Constraints:
#  0 <= intervals.length <= 10**4
#  intervals[i].length == 2
#  0 <= starti <= endi <= 10**5
#  intervals is sorted by starti in ascending order.
#  newInterval.length == 2
#  0 <= start <= end <= 10**5

def InsertInterval(intervals, newInterval):
    if not intervals:
        return [[newInterval]]

    if newInterval[1] < intervals[0][0]:
        return [[newInterval]] + intervals

    if newInterval[0] > intervals[-1][1]:
        return intervals + [[newInterval]]

    result = []
    for interval in intervals:
        if IsOverlap(newInterval, interval):
            if result and result[-1] == newInterval:
                result.pop()
            newInterval = Merge(newInterval, interval)
            result.append(newInterval)
        else:
            result.append(interval)

    return result

def IsOverlap(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    return not (end1 < start2 or end2 < start1)

def Merge(interval1, interval2):
    start1, end1 = interval1
    start2, end2 = interval2
    newStart = min(start1, start2)
    newEnd = max(end1, end2)
    return [newStart, newEnd]

if __name__ == "__main__":
    # Example 1:
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    expected = [[1,5],[6,9]]
    output = InsertInterval(intervals, newInterval)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    expected = [[1,2],[3,10],[12,16]]
    output = InsertInterval(intervals, newInterval)
    print(expected)
    print(output)
    print(expected == output)
    print()

     # Example 3
    intervals = [[1,3], [5,7], [8,12]]
    newInterval = [4,6]
    expected = [[1,3], [4,7], [8,12]]
    output = InsertInterval(intervals, newInterval)
    print(expected)
    print(output)
    print(expected == output)
    print()
    
    # Example 4
    intervals = [[1,3], [5,7], [8,12]]
    newInterval = [4,10]
    expected = [[1,3], [4,12]]
    output = InsertInterval(intervals, newInterval)
    print(expected)
    print(output)
    print(expected == output)
    print()
    
    # Example 5
    intervals = [[2,3],[5,7]]
    newInterval = [1,4]
    expected = [[1,4], [5,7]]
    output = InsertInterval(intervals, newInterval)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3
    intervals = [[1,2], [3,4], [5,6]]
    newInterval = [2,5]
    expected = [[1,6]]
    output = InsertInterval(intervals, newInterval)
    print(expected)
    print(output)
    print(expected == output)
    print()