# Create an iterator for the inorder traversal of a tree

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.value)
#         inorder(root.right)

class InorderIterator:
    def __init__(self, root):
        self.stack = []
        self.GoLeft(root)

    def GoLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def HasNext(self):
        return bool(self.stack)

    def Next(self):
        if not self.HasNext():
            return None
        
        node = self.stack.pop()
        self.GoLeft(node.right)

        return node.value

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    tree = TreeNode(4)

    tree.left = TreeNode(2)
    tree.right = TreeNode(6)

    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right.left = TreeNode(5)
    tree.right.right = TreeNode(7)

    inorder = InorderIterator(tree)

    print(inorder.Next(), 1)
    print(inorder.Next(), 2)
    print(inorder.Next(), 3)
    print(inorder.Next(), 4)
    print(inorder.Next(), 5)
    print(inorder.Next(), 6)
    print(inorder.Next(), 7)
    print(inorder.Next(), None)