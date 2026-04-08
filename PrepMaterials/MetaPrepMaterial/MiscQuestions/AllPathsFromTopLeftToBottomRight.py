# All Paths From Source to Target in matrix
#
# Given an NxN matrix find all possible paths from cell (0, 0)
# to cell (n - 1, n - 1) if only right and down movements are
# allowed.
#
# Example:
# N = 3
# output = ['DDRR', 'DRDR', 'DRRD', 'RDDR', 'RDRD', 'RRDD']

from collections import deque

def allPathsBFS(N):
    source = (0,0)
    goal = (N - 1, N - 1)

    #                 cell,   directions
    pending = deque([(source, [])])
    result = []

    while pending:
        cell, directions = pending.popleft()

        if cell == goal:
            result.append("".join(directions))

        x, y = cell

        # can it go down?
        if x < N:
            pending.append(((x + 1, y), directions + ["D"]))
        
        # can it go right?
        if y < N:
            pending.append(((x, y + 1), directions + ["R"]))

    return result

def allPathsDFS(N):
    source = (0,0)
    goal = (N - 1, N - 1)

    #           cell,   directions
    pending = [(source, [])]
    result = []

    while pending:
        cell, directions = pending.pop()

        if cell == goal:
            result.append("".join(directions))

        x, y = cell

        # can it go right?
        if x < N:
            pending.append(((x + 1, y), directions + ["R"]))
        
        # can it go down?
        if y < N:
            pending.append(((x, y + 1), directions + ["D"]))

    return result

def allPaths(N):
    return allPathsDFS(N)

if __name__=="__main__":
    N = 3
    expected = ['DDRR', 'DRDR', 'DRRD', 'RDDR', 'RDRD', 'RRDD']
    output = allPaths(N)
    print(expected)
    print(output)
    print(expected == output)
