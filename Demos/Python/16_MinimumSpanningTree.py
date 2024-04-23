# Given a graph G, compute its minumum spanning tree T

class Graph(object):
    def __init__(self):
        self._neighbors = {}
        self._weights = {}

    def __contains__(self, key):
        return key in self._neighbors

    def GetNodes(self):
        return list(self._neighbors.keys())
    
    def GetEdges(self, includeWeights=False):
        if not includeWeights:
            return list(self._weights.keys())
        
        edges = []
        for key in self._weights:
            u, v = key
            w = self._weights[key]
            edges.append((u, v, w))

        return edges
    
    def AddNode(self, v):
        if v not in self._neighbors:
            self._neighbors[v] = set()

    def AddEdge(self, u, v, weight):
        self.AddNode(u)
        self.AddNode(v)

        self._neighbors[u].add(v)
        self._neighbors[v].add(u)

        self._weights[(min(u, v), max(u, v))] = weight

    def GetNeighbors(self, u):
        if u in self._neighbors:
            return list(self._neighbors[u])
        return []

def CanReach(G: Graph, source, target):
    if source not in G or target not in G:
        return False

    pending = [source]
    visited = set()

    while pending:
        u = pending.pop(0)
        visited.add(u)
        
        if u == target:
            return True

        for v in G.GetNeighbors(u):
            if v not in visited:
                pending.append(v)

    return False

# Kruskal's algorithm
# Time complexity: O(|E| log |V|)
# Space complexity: O(|E| + |V|)
def GetMinimumSpanningTree(G: Graph):
    T = Graph()
    
    candidateEdges = sorted(G.GetEdges(includeWeights=True), key=lambda x: x[2])

    for u, v, w in candidateEdges:
        if CanReach(T, u, v):
            continue

        T.AddEdge(u, v, w)

    return T

if __name__ == "__main__":
    G = Graph()

    G.AddEdge('a', 'b', 2)
    G.AddEdge('a', 'd', 7)
    G.AddEdge('a', 'f', 2)
    G.AddEdge('b', 'c', 1)
    G.AddEdge('b', 'd', 4)
    G.AddEdge('b', 'e', 3)
    G.AddEdge('b', 'f', 5)
    G.AddEdge('c', 'e', 4)
    G.AddEdge('c', 'f', 4)
    G.AddEdge('d', 'e', 1)
    G.AddEdge('d', 'g', 5)
    G.AddEdge('e', 'g', 7)

    output = GetMinimumSpanningTree(G).GetEdges()
    expectedOutput = [('b', 'c'), ('d', 'e'), ('a', 'b'), ('a', 'f'), ('b', 'e'), ('d', 'g')]

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)