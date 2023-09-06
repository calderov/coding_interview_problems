# Problem:
# Given an array of intervals representing N appointments, find out if a
# person can attend all the appointments.
# 
# Examples:
# 
#   Appointments: [[1,4], [2,5], [7,9]]
#   Output: false
#   Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of
#   these appointments.
# 
#   Appointments: [[6,7], [2,4], [8,12]]
#   Output: true
#   Explanation: None of the appointments overlap, therefore a person can
#   attend all of them.
# 
#   Appointments: [[4,5], [2,3], [3,6]]
#   Output: false
#   Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of
#   these appointments.

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    @staticmethod
    def ListOfIntervals(listOfPairs):
        return [Interval(i[0], i[1]) for i in listOfPairs]

class Solution:
    # Solution:
    # 1. Sort the appointments list.
    # 2. Use a for loop to traverse the appointments list,
    #    checking at every iteration if the current appointment
    #    overlaps with the next one. If so, return False and finish.
    #
    # 3. Return True if for loop finished normally.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(1)
    def CanAttendAllAppointments(self, appointments):
        appointments.sort(key=lambda x: x.start)

        for i in range(len(appointments) - 1):
            if self.IsOverlap(appointments[i], appointments[i + 1]):
                return False

        return True

    def IsOverlap(self, intervalA, intervalB):
        return intervalA.start < intervalB.end and intervalA.end > intervalB.start

if __name__ == "__main__":
    solution = Solution()
    ListOfIntervals = Interval.ListOfIntervals

    # Example 1
    appointments = [[1,4], [2,5], [7,9]]
    expectedOutput = False
    output = solution.CanAttendAllAppointments(ListOfIntervals(appointments))
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    appointments = [[6,7], [2,4], [8,12]]
    expectedOutput = True
    output = solution.CanAttendAllAppointments(ListOfIntervals(appointments))
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    appointments = [[4,5], [2,3], [3,6]]
    expectedOutput = False
    output = solution.CanAttendAllAppointments(ListOfIntervals(appointments))
    print(output, expectedOutput, output == expectedOutput)