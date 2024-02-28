# 1650. Lowest Common Ancestor of a Binary Tree III (Medium)
# Given two nodes of a binary tree p and q, return their lowest common
# ancestor (LCA).
# 
# Each node will have a reference to its parent node. The definition for Node
# is below:
# 
# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }
#
# According to the definition of LCA on Wikipedia: "The lowest common
# ancestor of two nodes p and q in a tree T is the lowest node that has both
# p and q as descendants (where we allow a node to be a descendant of
# itself)."
# 
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant
# of itself according to the LCA definition.
# 
# Example 3:
# Input: root = [1,2]
# Output: 1

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def GetDepth(self, sourceNode):
        node = sourceNode
        depth = 0

        while node:
            node = node.parent
            depth += 1
        
        return depth

    # Time complexity: O(n)
    # Space complexity: O(1)
    def LowestCommonAncestor(self, nodeA, nodeB):
        # Get depths of nodes A and B
        depthA = self.GetDepth(nodeA)
        depthB = self.GetDepth(nodeB)

        # Move pointers A and B to the same level
        while depthA != depthB:
            if depthA < depthB:
                nodeB = nodeB.parent
                depthB -= 1

            if depthB < depthA:
                nodeA = nodeA.parent
                depthA -= 1

        # Now that the pointers are at the same level
        # traverse their parents until the first common
        # ancestor is found
        while nodeA != nodeB:
            nodeA = nodeA.parent
            nodeB = nodeB.parent

        # Node A should be sitting at the lowest common ancestor
        if nodeA:
            return nodeA.val
    
        # If nodes A and B are part of diferent trees, they have no common ancestor
        return None

def ListToTree(values, index=0, parent=None):
    if not values:
        return None
    
    if index > len(values):
        raise Exception('Index out of range')
    
    root = Node(values[index])
    root.parent = parent
    
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    if leftIndex < len(values):
        root.left = ListToTree(values, leftIndex, parent=root)
    
    if rightIndex < len(values):
        root.right = ListToTree(values, rightIndex, parent=root)
    
    return root

def FindValueInTree(root, value):
    pending = [root]
    while pending:
        node = pending.pop()
        
        if node.val == value:
            return node
        
        if node.left:
            pending.append(node.left)
        
        if node.right:
            pending.append(node.right)

    return None

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root = ListToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = FindValueInTree(root, 5)
    q = FindValueInTree(root, 1)
    expectedOutput = 3
    output = solution.LowestCommonAncestor(p, q)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)

    # Example 2
    root = ListToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = FindValueInTree(root, 5)
    q = FindValueInTree(root, 4)
    expectedOutput = 5
    output = solution.LowestCommonAncestor(p, q)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)

    # Example 3
    root = ListToTree([1, 2])
    p = FindValueInTree(root, 1)
    q = FindValueInTree(root, 2)
    expectedOutput = 1
    output = solution.LowestCommonAncestor(p, q)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)