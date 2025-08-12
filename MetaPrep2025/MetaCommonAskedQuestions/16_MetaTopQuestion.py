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

from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Time complexity: O(n)
# Space complexity: O(n)
def lowestCommonAncestor(root, p, q):
    if not root:
        return None
    
    # Find node parents and levels using BFS
    parents = {}
    pending = deque([(root, None, 1)])

    while pending:
        node, parent, level = pending.popleft()

        parents[node.val] = (node, parent, level)
        
        if node.left:
            pending.append((node.left, node, level + 1))

        if node.right:
            pending.append((node.right, node, level + 1))
    
    if p not in parents or q not in parents:
        return None
    
    # Find lowest common ancestor
    pNode, pParent, pLevel = parents[p]
    qNode, qParent, qLevel = parents[q]

    while pLevel != qLevel:
        if pLevel > qLevel:
            pNode, pParent, pLevel = parents[pParent.val]
            continue

        if qLevel > pLevel:
            qNode, qParent, qLevel = parents[qParent.val]
            continue
    
    while pNode and qNode:
        if pNode == qNode:
            return pNode.val
        pNode, pParent, _ = parents[pParent.val]
        qNode, qParent, _ = parents[qParent.val]

    return None

def lowestCommonAncestorAlt(root, p, q):
    if not root:
        return None
    
    # Find node parents and levels using BFS
    pNode = None
    qNode = None
    pLevel = 0
    qLevel = 0

    parents = {}
    pending = deque([(root, None, 1)])

    while pending:
        node, parent, level = pending.popleft()

        parents[node] = parent
        
        if node.val == p:
            pNode = node
            pLevel = level

        if node.val == q:
            qNode = node
            qLevel = level

        if pNode and qNode:
            break

        if node.left:
            pending.append((node.left, node, level + 1))
        
        if node.right:
            pending.append((node.right, node, level + 1))

    if not pNode or not qNode:
        return None
    
    while pLevel != qLevel:
        if pLevel > qLevel:
            pNode = parents[pNode]
            pLevel -= 1
        
        if qLevel > pLevel:
            qNode = parents[qNode]
            qLevel -= 1

    while pNode and qNode:
        if pNode == qNode:
            return pNode.val
        
        pNode = parents[pNode]
        qNode = parents[qNode]
    
    return None

def listToTree(values, index=0):
    if not values or index < 0 or index >= len(values) or values[index] == None:
        return None
    
    node = Node(values[index])
    leftIndex = 2 * index + 1
    rightIndex = 2* index + 2

    node.left = listToTree(values, leftIndex)
    node.right = listToTree(values, rightIndex)

    return node

if __name__ == "__main__":
    # Example 1
    root = listToTree([3,5,1,6,2,0,8,None,None,7,4])
    p = 5
    q = 1
    expectedOutput = 3
    output = lowestCommonAncestor(root, p, q)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    root = listToTree([3,5,1,6,2,0,8,None,None,7,4])
    p = 5
    q = 4
    expectedOutput = 5
    output = lowestCommonAncestor(root, p, q)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    root = listToTree([1,2])
    p = 1
    q = 2
    expectedOutput = 1
    output = lowestCommonAncestor(root, p, q)
    print(output, expectedOutput, output == expectedOutput)