# Problem:
# For K employees, we are given a list of intervals representing each
# employee’s working hours. Our goal is to determine if there is a free
# interval which is common to all employees. You can assume that each list of
# employee working hours is sorted on the start time.
# 
# Example 1:
# 
# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
# Output: [3,5]
# Explanation: All the employees are free between [3,5].
# 
# Example 2:
# 
# Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
# Output: [4,6], [8,9]
# Explanation: All employees are free between [4,6] and [8,9].
# 
# Example 3:
# 
# Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
# Output: [5,7]
# Explanation: All employees are free between [5,7].
# 

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def ListOfListOfPairsToSchedule(employees):
        schedule = []
        for employee in employees:
            shifts = []
            for interval in employee:
                shifts.append(Interval(interval[0], interval[1]))
            schedule.append(shifts)
        return schedule

    @staticmethod
    def ListOfPairs(intervals):
        return [[i.start, i.end] for i in intervals]

class Solution:
    # Solution:
    # 
    # 1. Extract the working hours intervals from the employee schedule,
    #    and store them into a list named intervals.
    #
    # 2. Sort the intervals list.
    #
    # 3. Find the min start time and max end time from the intervals list.
    # 
    # 4. Initialize the employee free time list by having an interval from
    #    min start to max end in it.
    #      employeeFreeTime = [Interval(minStart, maxEnd)]
    #
    # 5. For each interval in the intervals list, check if the if overlaps
    #    with the last interval of employeeFreeTime. If so, substract the
    #    current interval from it.
    #
    # 6. After all the intervals have been substracted from the employeeFreeTime
    #    The remainder should be the time intervals that is free for all the 
    #    employees. Return employeeFreeTime and finish.
    #    
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def FindEmployeeFreeTime(self, schedule):
        # Extract the working hours intervals from the employee schedule
        intervals = self.ScheduleToIntervalsList(schedule)
        
        # Sort the intervals
        intervals.sort(key=lambda x: x.start)
        
        # Find the min start time and max end time from the intervals list.
        minStart = min([i.start for i in intervals])
        maxEnd = max([i.end for i in intervals])

        # Initialize the employee free time list by assuming that the employees
        # are free from minStart to maxEnd
        employeeFreeTime = [Interval(minStart, maxEnd)]
        

        # For each interval
        for interval in intervals:
            # If the interval overlaps with the last interval of employee free time
            # substract the current interval from it.
            if self.IsOverlap(interval, employeeFreeTime[-1]):
                substractionResult = self.Substract(employeeFreeTime[-1], interval)
                employeeFreeTime.pop()
                employeeFreeTime += substractionResult

        # The remainder should be the time that is free for all the employees
        return employeeFreeTime

    def IsOverlap(self, intervalA, intervalB):
        return intervalA.start < intervalB.end and intervalA.end > intervalB.start
    
    def Substract(self, a, b):
        # Case 1: No overlap (left)
        if b.end <= a.start:
            return [a]
        
        # Case 2: Left overlap
        if b.start <= a.start and b.end < a.end:
            return [Interval(b.end, a.end)]
        
        # Case 3: Inner overlap A in B
        if b.start < a.start and b.end > a.end:
            return [Interval(b.start, a.start), Interval(a.end, b.end)]
        
        # Case 4: Inner overlap B in A
        if a.start < b.start and a.end > b.end:
            return [Interval(a.start, b.start), Interval(b.end, a.end)]

        # Case 5: Right overlap
        if a.start < b.start and a.end >= b.end:
            return [Interval(a.start, b.start)]
        
        # Case 6: No overlap (right)
        if a.end <= b.start:
            return [a]
        
        return []

    def ScheduleToIntervalsList(self, schedule):
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)
        return intervals


if __name__ == "__main__":
    solution = Solution()
    ListOfPairs = Interval.ListOfPairs
    ListOfListOfPairsToSchedule = Interval.ListOfListOfPairsToSchedule

    # Example 1
    schedule = [[[1,3], [5,6]], [[2,3], [6,8]]]
    expectedOutput = [[3,5]]
    output = ListOfPairs(solution.FindEmployeeFreeTime(ListOfListOfPairsToSchedule(schedule)))
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    schedule = [[[1,3], [9,12]], [[2,4]], [[6,8]]]
    expectedOutput = [[4,6], [8,9]]
    output = ListOfPairs(solution.FindEmployeeFreeTime(ListOfListOfPairsToSchedule(schedule)))
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    schedule = [[[1,3]], [[2,4]], [[3,5], [7,9]]]
    expectedOutput = [[5,7]]
    output = ListOfPairs(solution.FindEmployeeFreeTime(ListOfListOfPairsToSchedule(schedule)))
    print(output, expectedOutput, output == expectedOutput)

