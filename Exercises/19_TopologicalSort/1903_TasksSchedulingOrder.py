# Problem:
# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some
# prerequisite tasks which need to be completed before it can be scheduled.
# Given the number of tasks and a list of prerequisite pairs, write a method
# to find the ordering of tasks we should pick to finish all tasks.
# 
# Example:
# 
#   Input: Tasks = 3, Prerequisites = [0, 1], [1, 2]
#   Output: [0, 1, 2]
#   Explanation: To execute task '1', task '0' needs to finish first.
#                Similarly, task '1' needs to finish before '2' can be
#                scheduled. A possible scheduling of tasks is: [0, 1, 2] 

class Solution:
    # Solution:
    # Topologically sort the tasks return this order as the proposed schedule. 
    # If there is a cyclic dependency among the tasks, then the topological 
    # order can't be computed, if this is the case, return an empty list.
    #
    # Solution complexity:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def ScheduleTasks(self, tasks, prerequisites):
        graph = self.BuildGraph(tasks, prerequisites)
        inDegree = self.BuildInDegreeTracker(graph)

        sources = []
        for v in inDegree:
            if inDegree[v] == 0:
                sources.append(v)

        sortedTasks = []

        while sources:
            v = sources.pop(0)
            sortedTasks.append(v)

            for u in graph[v]:
                inDegree[u] -= 1
                if inDegree[u] == 0:
                    sources.append(u)
            
        if len(sortedTasks) != tasks:
            return []

        return sortedTasks

    def BuildGraph(self, vertices, edges):
        graph = {i:[] for i in range(vertices)}
        
        for e in edges:
            v, u  = e
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
    prerequisites = [[0, 1], [1, 2]]
    expectedOutput = [0, 1, 2]
    output = solution.ScheduleTasks(tasks, prerequisites)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2:
    tasks = 3
    prerequisites = [[0, 1], [1, 2], [2, 0]]
    expectedOutput = []
    output = solution.ScheduleTasks(tasks, prerequisites)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
 
    # Example 3:
    tasks = 6
    prerequisites = [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
    expectedOutput = [0, 1, 4, 3, 2, 5] 
    output = solution.ScheduleTasks(tasks, prerequisites)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()