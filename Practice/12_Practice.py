# Create an iterator for the postorder traversal of a tree

# def postorder(root):
#     if root:
#         postorder(root.left)
#         postorder(root.right)
#         print(root.value)

class PostOrderIterator:
    def __init__(self, root):
        self.stack = []
        self.FillStack(root)

    def FillStack(self, node):
        while node:
            self.stack.append(node)
            if node.left:
                node = node.left
            else:
                node = node.right

    def HasNext(self):
        return bool(self.stack)

    def Next(self):
        if not self.HasNext():
            return None

        node = self.stack.pop()

        if self.stack and node == self.stack[-1].left:
            self.FillStack(self.stack[-1].right)

        return node.value

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    tree = TreeNode(1)

    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    postOrder = PostOrderIterator(tree)

    print(postOrder.Next(), 4)
    print(postOrder.Next(), 5)
    print(postOrder.Next(), 2)
    print(postOrder.Next(), 6)
    print(postOrder.Next(), 7)
    print(postOrder.Next(), 3)
    print(postOrder.Next(), 1)
    print(postOrder.Next(), None)