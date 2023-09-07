# Problem:
# We are given a list of Jobs. Each job has a Start time, an End time, and a
# CPU load when it is running. Our goal is to find the maximum CPU load at
# any time if all the jobs are running on the same machine.
# 
# Example 1:
# 
# Jobs: [[1,4,3], [2,5,4], [7,9,6]]
# Output: 7
# Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load
# (3+4=7) will be when both the jobs are running at the same time i.e.,
# during the time interval (2,4).
# 
# Example 2:
# 
# Jobs: [[6,7,10], [2,4,11], [8,12,15]]
# Output: 15
# Explanation: None of the jobs overlap, therefore we will take the maximum
# load of any job which is 15.
# 
# Example 3:
# 
# Jobs: [[1,4,2], [2,4,1], [3,6,5]]
# Output: 8
# Explanation: Maximum CPU load will be 8 as all jobs overlap during the time
# interval [3,4].
# 

from heapq import *

class Job:
    def __init__(self, start, end, cpuload):
        self.start = start
        self.end = end
        self.cpuload = cpuload

    @staticmethod
    def ListOfJobs(listOfTriplets):
        return [Job(i[0], i[1], i[2]) for i in listOfTriplets]

class Solution:
    # Solution:
    # 1. Sort the list of jobs by start time.
    # 2. Initialize an empty min heap to overlapping jobs.
    #      minHeap = []
    #
    # 3. Initialize a variable to keep track of the maximum CPU load found so far.
    #      maxCPULoad = 0
    #
    # 4. For each job in the job list, remove those jobs from the min heap that
    #    finished before the start of the current job.
    # 
    #    Then, add the current job to the minHeap and update the max CPU load by
    #    comparing its stored value with the sum of cpu load values from the jobs
    #    in the min heap.
    #
    #    Repeat this step for all the jobs in the input list.
    #
    # 6. Return the max cpu load.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def GetMaxCPULoad(self, jobs):
        # Sort the list of jobs by start time
        jobs.sort(key=lambda x: x.start)
        
        # Initialize a min heap to track clusters of overlapping jobs
        minHeap = []

        # Initialize a variable to keep track of the maximum CPU load found so far
        maxCPULoad = 0

        # For each job in the job list
        for job in jobs:
            # Remove those jobs that finished before the start of  the current job
            # from the min heap
            while minHeap and minHeap[0].end <= job.start:
                heappop(minHeap)

            # Add the current job to the minHeap
            minHeap.append(job)

            # Update the max CPU load by comparing its stored value with the
            # sum of cpu load values of those jobs present in the min heap
            maxCPULoad = max(maxCPULoad, sum([i.cpuload for i in minHeap]))
        
        # Return the max cpu load
        return maxCPULoad

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    jobs = [[1,4,3], [2,5,4], [7,9,6]]
    expectedOutput = 7
    output = solution.GetMaxCPULoad(Job.ListOfJobs(jobs))
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    jobs = [[6,7,10], [2,4,11], [8,12,15]]
    expectedOutput = 15
    output = solution.GetMaxCPULoad(Job.ListOfJobs(jobs))
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    jobs = [[1,4,2], [2,4,1], [3,6,5]]
    expectedOutput = 8
    output = solution.GetMaxCPULoad(Job.ListOfJobs(jobs))
    print(output, expectedOutput, output == expectedOutput)
