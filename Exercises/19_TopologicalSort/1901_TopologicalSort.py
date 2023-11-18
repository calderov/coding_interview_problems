# Problem:
# The Topological Sort of a directed graph (a graph with unidirectional edges) is
# a linear ordering of its vertices such that for every directed edge (U, V) from
# vertex U to vertex V, U comes before V in the ordering.
# 
# Given a directed graph, find the topological ordering of its vertices.
# 
# Example:
# 
#   Input: Vertices = 4, Edges = [3, 2], [3, 0], [2, 0], [2, 1]
#   Output: Following are the two valid topological sorts for the given graph:
#     1) 3, 2, 0, 1
#     2) 3, 2, 1, 0

class Solution:
    # Solution:
    #
    # Solution complexity:
    # Time complexity: O(V + E)
    # Space complexity: O(V + E)
    def TopologicalSort(self, vertices, edges):
        # Build graph and in-degree tracker
        graph = self.BuildGraph(vertices, edges)
        inDegree = self.BuildInDegreeTracker(graph)
        
        # Find initial sources (nodes with no incoming edges)
        sources = []
        for v in inDegree:
            if inDegree[v] == 0:
                sources.append(v)

        # Initialize sorted vertices list (this will hold our result)
        sortedVertices = []

        # While there are sources in the sources list
        while sources:
            # Pop the first element v of the sources list and push it to the sorted vertices list
            v = sources.pop(0)
            sortedVertices.append(v)
            
            # For each vertex u, children of v, decrease the inDegree value of u by one.
            # If the inDegree value of u has reached zero, add u to the sources list
            for u in graph[v]:
                inDegree[u] -= 1
                if inDegree[u] == 0:
                    sources.append(u)

        # Return an empty list if there is a missmatch between the amount of sorted
        # vertices, and the total amount of vertices in the graph, as this suggests
        # that the graph is not acyclical        
        if len(sortedVertices) != vertices:
            return []

        # Return sorted vertices
        return sortedVertices
        

    def BuildGraph(self, vertices, edges):
        # Initialize graph
        graph = {i: [] for i in range(vertices)}

        # Insert edges
        for e in edges:
            v, u = e
            graph[v].append(u)

        return graph
    
    def BuildInDegreeTracker(self, graph):
        # Initialize in-degree tracker
        inDegree = {i: 0 for i in graph}

        # For each v
        for v in graph:
            # Add 1 to each children of v
            for u in graph[v]:
                inDegree[u] += 1

        return inDegree


def main():
    solution = Solution()

    # Example 1:
    vertices = 4 
    edges = [[3, 2], [3, 0], [2, 0], [2, 1]] 
    expectedOutput = [3, 2, 0, 1] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

    vertices = 3 
    edges = [[1, 0], [2, 1]] 
    expectedOutput = [2, 1, 0] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

    vertices = 4 
    edges = [[0, 1], [1, 2], [2, 3]] 
    expectedOutput = [0, 1, 2, 3] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

    vertices = 3 
    edges = [[0, 2], [1, 2], [1, 0]] 
    expectedOutput = [1, 0, 2] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

    vertices = 1 
    edges = [] 
    expectedOutput = [0] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

    vertices = 2 
    edges = [[0, 1]] 
    expectedOutput = [0, 1] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

    vertices = 2 
    edges = [[1, 0]] 
    expectedOutput = [1, 0] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

    vertices = 3 
    edges = [[0, 1], [0, 2], [1, 2]] 
    expectedOutput = [0, 1, 2] 
    output = solution.TopologicalSort(vertices, edges)
    # print(output)
    # print(output == expectedOutput)
    # print()

import timeit
if __name__ == "__main__":
    executionTime = timeit.timeit(main)
    print(executionTime)