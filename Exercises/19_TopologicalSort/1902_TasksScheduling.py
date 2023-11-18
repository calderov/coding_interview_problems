# Problem:
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
# prerequisite tasks which need to be completed before it can be scheduled.
# Given the number of tasks and a list of prerequisite pairs, find out if it
# is possible to schedule all the tasks.
# 
# Example:
# 
#   Input: Tasks = 3, Prerequisites = [0, 1], [1, 2]
#   Output: True
#   Explanation: To execute task '1', task '0' needs to finish first.
#                Similarly, task '1' needs to finish before '2' can be
#                scheduled. One possible scheduling of tasks is:
#                [0, 1, 2]

# Solution:
# Topologically sort the tasks, as that will place the first task that needs to be executed at
# the beginning of the list of tasks, followed by its most immediate successor task, and so on.
#
# If the topological sort fails, we can conclude that there is a cycle within the tasks dependencies,
# return False if this is the case. Otherwise, return True
#
# Solution complexity:
# Time complexity: O(V + E)
# Space complexity: O(V + E)
class Solution:
    def ScheduleTasks(self, tasks, prerequisites):
        # Build dependency graph and in-degree tracker
        graph = self.BuildGraph(tasks, prerequisites)
        inDegree = self.BuildInDegreeTracker(graph)

        # Find initial sources
        sources = []
        for v in inDegree:
            if inDegree[v] == 0:
                sources.append(v)

        # Topologically sort the tasks
        sortedTasks = []
        while sources:
            v = sources.pop(0)
            sortedTasks.append(v)

            for u in graph[v]:
                inDegree[u] -= 1
                if inDegree[u] == 0:
                    sources.append(u)
        
        # If there are not as many sorted tasks, as there are tasks, then our
        # topological sort failed, that may be due to a cyclic dependency
        # in the tasks. Return False in this case.
        if len(sortedTasks) != tasks:
            return False
        
        # Otherwise, return True
        return True

    def BuildGraph(self, vertices, edges):
        graph = {i:[] for i in range(vertices)}

        for edge in edges:
            v, u = edge
            graph[v].append(u)

        return graph

    def BuildInDegreeTracker(self, graph):
        inDegree = {i:0 for i in graph}

        for v in graph:
            for u in graph[v]:
                inDegree[u] += 1

        return inDegree

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    tasks = 3
    prerequisites = [0, 1], [1, 2]
    expectedOutput = True
    output = solution.ScheduleTasks(tasks, prerequisites)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    tasks = 3
    prerequisites = [0, 1], [1, 2], [2, 0]
    expectedOutput = False
    output = solution.ScheduleTasks(tasks, prerequisites)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3:
    tasks = 6
    prerequisites = [2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
    expectedOutput = True
    output = solution.ScheduleTasks(tasks, prerequisites)
    print(output, expectedOutput, output == expectedOutput)