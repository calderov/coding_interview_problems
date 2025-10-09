# 797. All Paths From Source to Target (Medium)
#
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
# find all possible paths from node 0 to node n - 1 and return them in any
# order.

from collections import deque

def findAllPathsBFS(g, source, target):
    queue = deque([(source, [])])
    result = []

    while queue:
        node, path = queue.popleft()

        if node == target:
            result.append(path + [node])

        for nextNode in g[node]:
            if nextNode not in path:
                queue.append((nextNode, path + [node]))
        
    return result

def findAllPathsDFS(g, source, target):
    stack = [(source, [])]
    result = []

    while stack:
        node, path = stack.pop()

        if node == target:
            result.append(path + [node])

        for nextNode in g[node]:
            if nextNode not in path:
                stack.append((nextNode, path + [node]))

    return result

def findAllPaths(g):
    return findAllPathsBFS(g, 0, len(g) - 1)

def createGraph(neighborsList):
    return {i:neighborsList[i] for i in range(len(neighborsList))}

if __name__=="__main__":
    # Example 1
    g = [[1, 2],[3],[3],[]]
    expected = [[0, 1, 3], [0, 2, 3]]
    output = findAllPaths(createGraph(g))
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2
    g = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    expected = [[0, 4], [0, 3, 4], [0, 1, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]
    output = findAllPaths(createGraph(g))
    print(expected)
    print(output)
    print(expected == output)
    print()
