def MergeIntervals(intervals):
    mergedIntervals = []
    intervals.sort()

    for interval in intervals:
        if not mergedIntervals or not IsOverlap(mergedIntervals[-1], interval):
            mergedIntervals.append(interval)
        else:
            mergedIntervals[-1] = Merge(mergedIntervals[-1], interval)
    
    return mergedIntervals

def Merge(intervalA, intervalB):
    start = min(intervalA[0], intervalB[0])
    end =   max(intervalA[1], intervalB[1])
    return [start, end]

def IsOverlap(intervalA, intervalB):
    return not (intervalA[1] < intervalB[0] or intervalB[1] < intervalA[0])

if __name__ == "__main__":
    intervals = [[1,4], [2,5], [7,9]]
    expectedOutput = [[1,5], [7,9]]
    output = MergeIntervals(intervals)
    print(intervals)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
