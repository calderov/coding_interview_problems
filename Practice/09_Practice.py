# Given a binary tree, a target node in the binary tree, and an integer value
# k, print all the nodes that are at distance k from the given target node.
# No parent pointers are available

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Time complexity: O(n)
# Space complexity: O(n)
def GetNodesAtKFromTarget(root, target, k):
    if not root:
        return []
    
    # BFS traversal to find the target node and populate the parents map
    parents = {root: None}
    pending = [root]
    targetFound = False

    while pending:
        nodesInLevel = len(pending)
        for _ in range(nodesInLevel):
            node = pending.pop(0)

            if node == target:
                targetFound = True

            if node.left:
                pending.append(node.left)
                parents[node.left] = node

            if node.right:
                pending.append(node.right)
                parents[node.right] = node

    # Return early if the target was not found in the tree
    if not targetFound:
        return []
    
    # BFS traversal to find nodes at distance k from the target
    visited = set()
    pending = [target]
    nodesAtDistanceK = []
    distanceFromTarget = 0

    while pending:
        nodesInLevel = len(pending)
        for _ in range(nodesInLevel):
            node = pending.pop(0)
            parent = parents[node]

            visited.add(node)

            if distanceFromTarget == k:
                nodesAtDistanceK.append(node.value)

            if node.left and node.left not in visited:
                pending.append(node.left)

            if node.right and node.right not in visited:
                pending.append(node.right)

            if parent and parent not in visited:
                pending.append(parent)
        
        distanceFromTarget += 1

        if distanceFromTarget > k:
            break

    return nodesAtDistanceK

def ExampleTree():
    tree = TreeNode(1)
    
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    tree.left.left.left = TreeNode(8)
    tree.left.left.right = TreeNode(9)
    tree.left.right.left = TreeNode(10)
    tree.left.right.right = TreeNode(11)
    tree.right.left.left = TreeNode(12)
    tree.right.left.right = TreeNode(13)
    tree.right.right.left = TreeNode(14)
    tree.right.right.right = TreeNode(15)

    return tree

if __name__ == "__main__":
    tree = ExampleTree()
    target = tree.right # 3
    k = 2
    print(GetNodesAtKFromTarget(tree, target, k))

