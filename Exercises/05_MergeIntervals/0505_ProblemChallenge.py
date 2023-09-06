# Problem: 
# Given a list of intervals representing the start and end time of ‘N’
# meetings, find the minimum number of rooms required to hold all the
# meetings.
# 
# Example 1:
# 
# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these
# two meetings. [7,9] can occur in any of the two rooms later.
# 
# Example 2:
# 
# Meetings: [[6,7], [2,4], [8,12]]
# Output: 1
# Explanation: None of the meetings overlap, therefore we only need one room
# to hold all meetings.
# 
# Example 3:
# 
# Meetings: [[1,4], [2,3], [3,6]]
# Output:2
# Explanation: Since [1,4] overlaps with the other two meetings [2,3] and
# [3,6], we need two rooms to hold all the meetings.
# 
# Example 4:
# 
# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room
# for [2,4] and [4,5].

import heapq

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def ListOfIntervals(listOfPairs):
        return [Interval(i[0], i[1]) for i in listOfPairs]

class Solution:
    # Solution:
    # 1. Sort meetings by start time.
    #
    # 2. Initialize an empty list of meeting rooms.
    #
    # 3. For each meeting find an existing room which last meeting doesn't
    #    overlap the current meeting.
    #
    # 4. If no existing room can host the meeting without overlapping, 
    #    allocate a new room for the meeting and add it to the meeting rooms
    #    list.
    #
    # 5. Return the total number of meeting rooms once all the meetings
    #    have been scheduled.
    #
    # Solution complexity:
    # Time complexity: O(n * n)
    # Space complexity: O(n)
    def FindMinimumMeetingRooms(self, meetings):
        # Sort meetings by start time
        meetings.sort(key=lambda x: x.start)
        
        # Initialize empty list of meeting rooms
        meetingRooms = []
        
        # For each meeting
        for meeting in meetings:
            scheduled = False
            
            # Find an existing room with no overlapping meetings and
            # append the meeting to it
            for room in meetingRooms:
                if not self.IsOverlap(meeting, room[-1]):
                    room.append(meeting)
                    scheduled = True
                    break
        
            # If no existing room can host the meeting without overlapping, 
            # allocate a new room for the meeting
            if not scheduled:
                meetingRooms.append([meeting])

        # Return the total number of meeting rooms
        return len(meetingRooms)

    def IsOverlap(self, intervalA, intervalB):
        return intervalA.start < intervalB.end and intervalA.end > intervalB.start  

if __name__ == "__main__":
    solution = Solution()
    ListOfIntervals = Interval.ListOfIntervals

    # Example 1
    meetings = [[1,4], [2,5], [7,9]]
    expectedOutput = 2
    output = solution.FindMinimumMeetingRooms(ListOfIntervals(meetings))
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    meetings = [[6,7], [2,4], [8,12]]
    expectedOutput = 1
    output = solution.FindMinimumMeetingRooms(ListOfIntervals(meetings))
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    meetings = [[1,4], [2,3], [3,6]]
    expectedOutput = 2
    output = solution.FindMinimumMeetingRooms(ListOfIntervals(meetings))
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    meetings = [[4,5], [2,3], [2,4], [3,5]]
    expectedOutput = 2
    output = solution.FindMinimumMeetingRooms(ListOfIntervals(meetings))
    print(output, expectedOutput, output == expectedOutput)

