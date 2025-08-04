# Binary Search Tree : Insertion
# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem
#
# You are given a pointer to the root of a binary search tree and values to be inserted into the tree.
# Insert the values into their appropriate position in the binary search tree and return the root of
# the updated binary tree. You just have to complete the function.
#
# Sample Input
#         4
#        / \
#       2   7
#      / \
#     1   3
#
# The value to be inserted is 6.
#
# Sample Output
#
#          4
#        /   \
#       2     7
#      / \   /
#     1   3 6

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)

def bfs(root):
    values = []
    pending = [root]

    while pending:
        n = len(pending)
        for _ in range(n):
            node = pending.pop(0)
            if node:            
                values.append(node.val)
                pending.append(node.left)
                pending.append(node.right)
            else:
                values.append(None)

    return values

def insertValue(root, val):
    if not root:
        return Node(val)
    
    if val <= root.val:
        if not root.left:
            root.left = Node(val)
        else:
            insertValue(root.left, val)
    else:
        if not root.right:
            root.right = Node(val)
        else:
            insertValue(root.right, val)

    return root

if __name__ == "__main__":
    tree = Node(4)
    tree.left = Node(2)
    tree.right= Node(7)
    tree.left.left = Node(1)
    tree.left.right= Node(3)

    print("Original:")
    original = bfs(tree)
    expected = [4, 2, 7, 1, 3, 6, None, None, None, None, None, None, None]
    output = bfs(insertValue(tree, 6))
    
    print(original)
    print(expected)
    print(output)
    print(output == expected)


