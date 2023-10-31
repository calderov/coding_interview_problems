# Problem:
# You are given a list of tasks that need to be run, in any order, on a
# server. Each task will take one CPU interval to execute but once a task has
# finished, it has a cooling period during which it can’t be run again. If
# the cooling period for all tasks is ‘K’ intervals, find the minimum number
# of CPU intervals that the server needs to finish all tasks.
# 
# If at any time the server can’t execute any task then it must stay idle.
# 
# Examples:
# 
#   Input: [a, a, a, b, c, c], K=2
#   Output: 7
#   Explanation: a -> c -> b -> a -> c -> idle -> a
# 
#   Input: [a, b, a], K=3
#   Output: 5
#   Explanation: a -> b -> idle -> idle -> a
# 

from heapq import *

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def TasksScheduling(self, tasks, k):
        tasksInstances = {}
        for task in tasks:
            tasksInstances[task] = tasksInstances.get(task, 0) + 1
        
        pendingTasks = [] # Max heap
        for task, instances in tasksInstances.items():
            heappush(pendingTasks, (-instances, task))

        executedTasks = []
        idleTasks = [] # Min heap

        t = 0
        while pendingTasks or idleTasks:
            while idleTasks and t - idleTasks[0][0] > k:
                _, nextIdle = heappop(idleTasks)
                heappush(pendingTasks, nextIdle)

            if pendingTasks:
                instances, task = heappop(pendingTasks)
                instances *= -1
                
                executedTasks.append(task)
                instances -= 1

                if instances > 0:
                    heappush(idleTasks, (t, (-instances, task)))
            
            else:
                executedTasks.append(None)

            t += 1
            
        return len(executedTasks)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tasks = ["a", "a", "a", "b", "c", "c"]
    k = 2
    expectedOutput = 7
    output = solution.TasksScheduling(tasks, k)
    print(output, expectedOutput, output == expectedOutput)
     
    # Example 2
    tasks = ["a", "b", "a"]
    k = 3
    expectedOutput = 5
    output = solution.TasksScheduling(tasks, k)
    print(output, expectedOutput, output == expectedOutput)