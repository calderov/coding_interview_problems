# Meeting Schedule II
# https://neetcode.io/problems/meeting-schedule-ii

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def isOverlap(self, intervalA, intervalB):
        return not (intervalA.start > intervalB.end or intervalA.end <= intervalB.start)

    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        meetingRooms = []

        intervals.sort(reverse=True, key=lambda interval: interval.start)

        while intervals:
            interval = intervals.pop()

            inserted = False
            i = 0
            while i < len(meetingRooms):
                if not self.isOverlap(meetingRooms[i][-1], interval):
                    meetingRooms[i].append(interval)
                    inserted = True
                    break
                i += 1

            if not inserted:
                meetingRooms.append([interval])

        return len(meetingRooms) 

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    intervals = [Interval(start, end) for start, end in [(0,40), (5,10), (15,20)]]
    expectedOutput = 2
    output = solution.minMeetingRooms(intervals)

    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    intervals = [Interval(start, end) for start, end in [(0,30),(5,25),(10,20),(15,18),(18,22),(23,30),(30,40),(35,45),(40,50),(45,55),(50,60),(55,65),(60,70),(65,75),(70,80),(75,85),(80,90),(85,95),(90,100)]]
    expectedOutput = 4
    output = solution.minMeetingRooms(intervals)

    print(output, expectedOutput, output == expectedOutput)