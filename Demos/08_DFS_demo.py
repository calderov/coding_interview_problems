
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def DFS(head, visited):
    if not head:
        return
    
    # Add node to visited list
    visited.append(head.val)
    
    # Recursively call dfs on neighbor subtrees
    DFS(head.left, visited)
    DFS(head.right, visited)

def DFSIterative(head):
    visited = []
    pending = [head] # Stack

    # While there are nodes in the pending stack
    while pending:
        # Fetch node from pending stack
        node = pending.pop()

        # Add node to visited list
        visited.append(node.val)

        # Add neighbors to pending stack
        if node.right: pending.append(node.right)
        if node.left: pending.append(node.left)

    return visited

if __name__ == "__main__":
    tree = TreeNode(1)

    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = [1, 2, 4, 5, 3, 6, 7]
   
    print("DFS recursive")
    output = []
    DFS(tree, output)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    print("DFS iterative")
    output = DFSIterative(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
