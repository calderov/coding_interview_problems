# 236. Lowest Common Ancestor of a Binary Tree (Medium)
# Given a binary tree, find the lowest common ancestor (LCA) of two given
# nodes in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common
# ancestor is defined between two nodes p and q as the lowest node in T that
# has both p and q as descendants (where we allow a node to be a descendant
# of itself).”
# 
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a
# descendant of itself according to the LCA definition.
# 
# Example 3:
# Input: root = [1,2], p = 1, q = 2
# Output: 1
#  
# 
# Constraints:
# - The number of nodes in the tree is in the range [2, 105].
# - -109 <= Node.val <= 109
# - All Node.val are unique.
# - p != q
# - p and q will exist in the tree.

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def LowestCommonAncestor(self, root, p, q):
        nodeQ = None
        nodeP = None
        depthP = 0
        depthQ = 0
        parents = {}
        
        # Use BFS to find the nodes p and q, compute their respective depths, and  populate a dictionary of parents
        level = 0
        pending = [root]
        while pending:
            nodesInLevel = len(pending)
            for _ in range(nodesInLevel):
                node = pending.pop(0)

                if node.val == p:
                    nodeP = node
                    depthP = level

                if node.val == q:
                    nodeQ = node
                    depthQ = level
                
                if node.left:
                    parents[node.left] = node
                    pending.append(node.left)

                if node.right:
                    parents[node.right] = node
                    pending.append(node.right)
            
            level += 1

        # If p is deeper than q, traverse its parents until we reach the level of q
        while depthP > depthQ:
            nodeP = parents[nodeP]
            depthP -= 1

        # Analogously, if q is deeper than p, traverse its parents until we reach the level of p
        while depthQ > depthP:
            nodeQ = parents[nodeQ]
            depthQ -= 1

        # Now traverse the parents of both p and q until the first common ancestor is found (this is our lower common ancestor)
        while nodeP != nodeQ:
            nodeP = parents[nodeP]
            nodeQ = parents[nodeQ]

        # Return the value of the lower common ancestor
        return nodeP.val
               



    def PythonListToTree(self, values, index=0):
        if not values:
            return None

        root = Node(values[index])

        leftIndex = 2 * index + 1
        rightIndex = 2 * index + 2

        if leftIndex < len(values):
            root.left = self.PythonListToTree(values, leftIndex)

        if rightIndex < len(values):
            root.right = self.PythonListToTree(values, rightIndex)

        return root

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root = solution.PythonListToTree([3,5,1,6,2,0,8,None,None,7,4])
    p = 5
    q = 1
    expectedOutput = 3
    output = solution.LowestCommonAncestor(root, p, q)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    root = solution.PythonListToTree([3,5,1,6,2,0,8,None,None,7,4])
    p = 5
    q = 4
    expectedOutput = 5
    output = solution.LowestCommonAncestor(root, p, q)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    root = solution.PythonListToTree([1,2])
    p = 1
    q = 2
    expectedOutput = 1
    output = solution.LowestCommonAncestor(root, p, q)
    print(output, expectedOutput, output == expectedOutput)