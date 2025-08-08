# 314. Binary Tree Vertical Order Traversal (Medium)
# Given the root of a binary tree, return the vertical order traversal of its
# nodes' values. (i.e., from top to bottom, column by column).
# 
# If two nodes are in the same row and column, the order should be from left
# to right.

# from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def verticalOrder(root):
    columns = {}
    pending = [(root, 0)]

    while pending:
        node, col = pending.pop(0)

        if col not in columns:
            columns[col] = []

        columns[col].append(node.val)
        
        if node.left:
            pending.append((node.left, col - 1))
        if node.right:
            pending.append((node.right, col + 1))

    return [columns[col] for col in sorted(columns)]

def treeToList(root):
    values = []

    pending = [root]
    while pending:
        node = pending.pop(0)

        if node == None:
            values.append(None)
            continue

        values.append(node.val)
        pending.append(node.left)
        pending.append(node.right)

    while values and values[-1] == None:
        values.pop()

    return values

def listToTree(values, index=0):
    if not values:
        return None
    
    if index < 0 or index >= len(values):
        return None
    
    if values[index] == None:
        return None
    
    node = Node(values[index])
    indexLeft = 2 * index + 1
    indexRight = 2 * index + 2

    node.left = listToTree(values, indexLeft)
    node.right = listToTree(values, indexRight)

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