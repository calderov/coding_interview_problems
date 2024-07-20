class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        graph = {}
        for node in range(numCourses):
            graph[node] = {"predecessors": set(), "successors": set()}

        for node, predecessor in prerequisites:
            graph[node]["predecessors"].add(predecessor)
            graph[predecessor]["successors"].add(node)

        pending = []
        for node in graph:
            if len(graph[node]["predecessors"]) == 0:
                pending.append(node)

        validOrdering = []
        visited = set()
        while pending:
            node = pending.pop()

            areDependenciesMet = True
            for predecessor in graph[node]["predecessors"]:
                if predecessor not in visited:
                    areDependenciesMet = False
                    break

            if not areDependenciesMet:
                continue

            if node in visited:
                return []

            visited.add(node)
            validOrdering.append(node)
            pending = list(filter(lambda x: x != node, pending))

            for successor in graph[node]["successors"]:
                pending.append(successor)

        if len(validOrdering) == len(graph.keys()):
            return validOrdering
        return []



if __name__ == "__main__":
    solution = Solution()

    # Example 1
    numCourses = 3
    prerequisites = [[1, 0]]
    expectedOutput = [2, 0, 1]
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