
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def BFS(head, visited, pending=[]):
    if not head:
        return
    
    # Add node to visited list
    visited.append(head.val)

    # Add neighbor nodes to pending queue
    pending.append(head.left)
    pending.append(head.right)
    
    # Recursively call bfs if there are pending nodes
    if pending:
        BFS(pending.pop(0), visited, pending)

def BFSIterative(head):
    visited = []
    pending = [head] # Queue

    # While there are nodes in the pending queue
    while pending:
        # Fetch node from pending queue
        node = pending.pop(0)

        # Add node to visited list
        visited.append(node.val)

        # Add neighbors to pending queue
        if node.left: pending.append(node.left)
        if node.right: pending.append(node.right)

    return visited

if __name__ == "__main__":
    tree = TreeNode(1)

    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = [1, 2, 3, 4, 5, 6, 7]
   
    print("BFS recursive")
    output = []
    BFS(tree, output)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    print("BFS iterative")
    output = BFSIterative(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()