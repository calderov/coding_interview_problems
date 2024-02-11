# Problem:
# Given an array of intervals representing N appointments, find out if a
# person can attend all the appointments.
#
# Examples:
#
#   Appointments: [[1,4], [2,5], [7,9]]
#   Output: False
#   Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of
#   these appointments.

class Solution:
    def CanAttendAllAppointments(self, appointments):
        appointments.sort()

        for i in range(len(appointments) - 1):
            if self.IsOverlap(appointments[i], appointments[i + 1]):
                return False
        
        return True

    def IsOverlap(self, intervalA, intervalB):
        intervalAStart, intervalAEnd = intervalA
        intervalBStart, intervalBEnd = intervalB
        return intervalAStart < intervalBEnd and intervalAEnd > intervalBStart

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    appointments = [[1,4], [2,5], [7,9]]
    expectedOutput = False
    output = solution.CanAttendAllAppointments(appointments)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    appointments = [[6,7], [2,4], [8,12]]
    expectedOutput = True
    output = solution.CanAttendAllAppointments(appointments)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    appointments = [[4,5], [2,3], [3,6]]
    expectedOutput = False
    output = solution.CanAttendAllAppointments(appointments)
    print(output, expectedOutput, output == expectedOutput)
