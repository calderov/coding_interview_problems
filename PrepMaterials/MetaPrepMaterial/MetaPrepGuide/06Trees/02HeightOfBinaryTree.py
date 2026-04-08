# Tree: Height of a Binary Tree
# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
#
# The height of a binary tree is the number of edges between the tree's root and its furthest leaf.
# For example, the following binary tree is of height 2:
#
#         4
#        / \
#       2   7
#      / \
#     1   3
#
#

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getHeight(root):
    h = -1
    pending = [root]
    
    while pending:
        m = len(pending)
        for _ in range(m):
            node = pending.pop(0)
            if node.left:
                pending.append(node.left)
            if node.right:
                pending.append(node.right)
        h += 1
    
    return h

if __name__ == "__main__":
    tree = Node(4)
    tree.left = Node(2)
    tree.right= Node(7)
    tree.left.left = Node(1)
    tree.left.right= Node(3)

    expected = 2
    output = getHeight(tree)
    print(expected)
    print(output)
    print(output == expected)
        