# Course Schedule II 
# https://leetcode.com/problems/course-schedule-ii/description/
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        return list(reversed(self.topologicalSort(numCourses, prerequisites)))
    
    def topologicalSort(self, vertices, edges):
        graph = {v:[] for v in range(vertices)}
        for u, v in edges:
            graph[u].append(v)

        inDegree = {v:0 for v in range(vertices)}
        for u, v in edges:
            inDegree[v] += 1
        
        sources = []
        for v in inDegree:
            if inDegree[v] == 0:
                sources.append(v)
        
        validOrdering = []
        while sources:
            u = sources.pop()

            validOrdering.append(u)

            for v in graph[u]:
                inDegree[v] -= 1
                if inDegree[v] == 0:
                    sources.append(v)

        if len(validOrdering) != len(graph):
            return []

        return validOrdering
            
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    numCourses = 3
    prerequisites = [[1, 0]]
    expectedOutput = [0, 1, 2]
    output = solution.findOrder(numCourses, prerequisites)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    
    print()

    # Example 2
    numCourses = 3
    prerequisites = [[0,1], [0,2], [1,2]]
    expectedOutput = [2, 1, 0]
    output = solution.findOrder(numCourses, prerequisites)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)