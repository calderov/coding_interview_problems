# Given a graph G, compute its minumum spanning tree T

def MinimumSpanningTree(G):
    if not G:
        return {}
    
    

if __name__ == "__main__":
    nodes = list('abcdefg')
    edges = [
        # u, v, weight
        ('a', 'b', 2),
        ('a', 'd', 7),
        ('a', 'f', 2),
        ('b', 'c', 1),
        ('b', 'd', 4),
        ('b', 'e', 3),
        ('b', 'f', 5),
        ('c', 'e', 4),
        ('c', 'f', 4),
        ('d', 'e', 1),
        ('d', 'g', 5),
        ('e', 'g', 7),
    ]

    G = {node:set() for node in nodes}

    for edge in edges:
        u, v, w = edge
        G[u].add((v, w))
        G[v].add((u, w))

    T = MinimumSpanningTree(G)
    print(T)