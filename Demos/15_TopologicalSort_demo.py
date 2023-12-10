# The Topological Sort of a directed graph (a graph with unidirectional edges) is
# a linear ordering of its vertices such that for every directed edge (U, V) from
# vertex U to vertex V, U comes before V in the ordering.
#
# Given the vertices and edges of a directed graph, find the topological ordering of
# the vertices.
def TopologicalSort(vertices, edges):
    graph = BuildGraph(vertices, edges)
    inDegree = BuildInDegreeTracker(graph)

    # Find initial sources (nodes with no incoming edges)
    sources = []
    for v in inDegree:
        if inDegree[v] == 0:
            sources.append(v)

    sortedVertices = []
    while sources:
        v = sources.pop(0)
        sortedVertices.append(v)

        # For each vertex u, children of v, decrease the inDegree value of u by one.
        # If the inDegree value of u has reached zero, add u to the sources list
        for u in graph[v]:
            inDegree[u] -= 1
            if inDegree[u] == 0:
                sources.append(u)

    # Return an empty list if the graph is not acyclical
    if len(sortedVertices) != vertices:
        return []

    # Otherwise, return sorted vertices
    return sortedVertices


def BuildGraph(vertices, edges):
    graph = {i: [] for i in range(vertices)}
    for e in edges:
        v, u = e
        graph[v].append(u)
    return graph

def BuildInDegreeTracker(graph):
    inDegree = {i: 0 for i in graph}
    for v in graph:
        for u in graph[v]:
            inDegree[u] += 1
    return inDegree

if __name__ == "__main__":
    # Example 1
    vertices = 4
    edges = [[3, 2], [3, 0], [2, 0], [2, 1]]
    expectedOutput = [3, 2, 0, 1]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 2
    vertices = 3
    edges = [[1, 0], [2, 1]]
    expectedOutput = [2, 1, 0]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 3
    vertices = 4
    edges = [[0, 1], [1, 2], [2, 3]]
    expectedOutput = [0, 1, 2, 3]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 4
    vertices = 3
    edges = [[0, 2], [1, 2], [1, 0]]
    expectedOutput = [1, 0, 2]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 5
    vertices = 1
    edges = []
    expectedOutput = [0]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 6
    vertices = 2
    edges = [[0, 1]]
    expectedOutput = [0, 1]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 7
    vertices = 2
    edges = [[1, 0]]
    expectedOutput = [1, 0]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 8
    vertices = 3
    edges = [[0, 1], [0, 2], [1, 2]]
    expectedOutput = [0, 1, 2]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()