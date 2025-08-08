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
# Input: tree = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# Example 2:
# Input: tree = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant
# of itself according to the LCA definition.
# 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

# Time complexity: O(log(n))
# Space complexity: O(n)
def LowestCommonAncestorV1(p, q):
    pAncestors = []
    qAncestors = []

    node = p
    while node:
        pAncestors.insert(0, node.val)
        node = node.parent

    node = q
    while node:
        qAncestors.insert(0, node.val)
        node = node.parent

    lowestAncestor = None
    i = 0
    while i < len(pAncestors) and i < len(qAncestors):
        if pAncestors[i] == qAncestors[i]:
            lowestAncestor = pAncestors[i]
            i += 1
        else:
            break
    
    return lowestAncestor

def getDepth(p):
    if p.parent == None:
        return 0
    p = p.parent
    return 1 + getDepth(p)

# Time complexity: O(log n)
# Space complexity: O(1)
def LowestCommonAncestorV2(p, q):
    pDepth = getDepth(p)
    qDepth = getDepth(q)

    pprime = p
    qprime = q

    while pDepth != qDepth:
        if pDepth > qDepth:
            pprime = pprime.parent
            pDepth -= 1

        if pDepth < qDepth:
            qprime = qprime.parent
            qDepth -= 1

    commonDepth = pDepth

    while commonDepth >= 0:
        if pprime == qprime:
            return pprime.val

        pprime = pprime.parent
        qprime = qprime.parent
        commonDepth -= 1

    return None

def LowestCommonAncestor(p, q):
    return LowestCommonAncestorV2(p, q)

def FindNodeInTree(root, val):
    if not root:
        return None

    pending = [root]

    while pending:
        node = pending.pop(0)
        if node.val == val:
            return node
        if node.left:
            pending.append(node.left)
        if node.right:
            pending.append(node.right)

    return None

def ListToTree(values, index=0, parent=None):
    if not values:
        return None
    
    if index < 0 or index >= len(values) or values[index] == None:
        return None
    
    node = Node(values[index])
    
    if parent:
        node.parent = parent
    
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    node.left = ListToTree(values, leftIndex, node)
    node.right = ListToTree(values, rightIndex, node)

    return node
    
if __name__ == "__main__":
    # Example 1
    root = ListToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = FindNodeInTree(root, 5)
    q = FindNodeInTree(root, 1)
    expectedOutput = 3
    output = LowestCommonAncestor(p, q)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    root = ListToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = FindNodeInTree(root, 5)
    q = FindNodeInTree(root, 4)
    expectedOutput = 5
    output = LowestCommonAncestor(p, q)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    root = ListToTree([1, 2])
    p = FindNodeInTree(root, 1)
    q = FindNodeInTree(root, 2)
    expectedOutput = 1
    output = LowestCommonAncestor(p, q)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 4
    root = ListToTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = FindNodeInTree(root, 7)
    q = FindNodeInTree(root, 4)
    expectedOutput = 2
    output = LowestCommonAncestor(p, q)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()