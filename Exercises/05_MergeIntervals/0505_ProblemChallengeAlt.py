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

from heapq import *

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end

    @staticmethod
    def ListOfMeetings(listOfPairs):
        return [Meeting(i[0], i[1]) for i in listOfPairs]

class Solution:
    # Solution:
    # 1. Sort meetings by start time.
    #
    # 2. Initialize a min heap to keep track of the meetings that are
    #    concurrent to a given meeting, and a variable to count the max
    #    number of concurrent meetings ever found, this value will be
    #    our minimum number of rooms required to host all meetings.
    #      minRooms = 0
    #      minHeap = []
    #
    # 3. For each meeting in the meetings list, remove previous meetings
    #    from the heap (those which finished before the current meeting
    #    started).
    #
    # 4. Push the meeting to the heap and update the minimum number of
    #    rooms required to host the meetings.
    #      minRooms = max(minRooms, len(minHeap))
    #
    # 5. Return the minimum number of rooms required to host the meetings.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def FindMinimumMeetingRooms(self, meetings):
        # Sort meetings by start time
        meetings.sort(key=lambda x: x.start)
        
        # Initialize a min heap to keep track of the meetings that are
        # concurrent to a given meeting, and a variable to count the max
        # number of concurrent meetings ever found, this value will be
        # our minimum number of rooms required to host all meetings.
        minRooms = 0
        minHeap = []
        
        # For each meeting in the meetings list
        for meeting in meetings:
            # Remove previous meetings from the heap (those which finished
            # before the current meeting started) 
            while minHeap and meeting.start >= minHeap[0].end:
                heappop(minHeap)
            
            # Push the meeting to the heap
            heappush(minHeap, meeting)
            
            # Update minimum number of rooms required to host the meetings
            minRooms = max(minRooms, len(minHeap))

        # Return the minimum number of rooms required to host the meetings
        return minRooms 

if __name__ == "__main__":
    solution = Solution()
    ListOfIntervals = Meeting.ListOfMeetings

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

