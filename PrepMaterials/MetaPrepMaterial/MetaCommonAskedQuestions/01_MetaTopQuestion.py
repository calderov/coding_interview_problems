# 314. Binary Tree Vertical Order Traversal (Medium)
# Given the root of a binary tree, return the vertical order traversal of its
# nodes' values. (i.e., from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left
# to right.

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def verticalOrder(root):
    if not root:
        return []

    columns = {}
    pending = deque([(0, root)])

    while pending:
        col, node = pending.popleft()

        if col not in columns:
            columns[col] = []

        columns[col].append(node.val)

        if node.left:
            pending.append((col - 1, node.left))
        if node.right:
            pending.append((col + 1, node.right))

    return [columns[i] for i in range(min(columns), max(columns)+1)]

def treeToList(root):
    if not root:
        return []
    
    values = []
    pending = deque([root])

    while pending:
        node = pending.popleft()
        values.append(node.val)

        if node.left:
            pending.append(node.left)
        if node.right:
            pending.append(node.right)

    return values

def listToTree(values, index=0):
    if not values or index < 0 or index >= len(values) or values[index] == None:
        return None

    node = Node(values[index])
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    node.left = listToTree(values, leftIndex)
    node.right = listToTree(values, rightIndex)

    return node

if __name__ == "__main__":
    # Example 1
    tree = listToTree([3,9,20,None,None,15,7])
    expectedOutput = [[9],[3,15],[20],[7]]
    output = verticalOrder(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    tree = listToTree([3,9,8,4,0,1,7])
    expectedOutput = [[4],[9],[3,0,1],[8],[7]]
    output = verticalOrder(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    tree = listToTree([3,9,8,4,0,1,7,None,None,None,2,5])
    expectedOutput = [[4],[9,5],[3,0,1],[8,2],[7]]
    output = verticalOrder(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    