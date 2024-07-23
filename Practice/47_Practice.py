class Solution:
    def findRedundantConnection(self, edges):
        m = len(edges)
        
        parent = [i for i in range(m + 1)]
        rank = [1] * (m + 1)

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

    
if __name__ == "__main__":
    solution = Solution()

    edges=[[1,2],[1,3],[3,4],[2,4]]
    expectedOutput = [2,4]
    output = solution.findRedundantConnection(edges)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)