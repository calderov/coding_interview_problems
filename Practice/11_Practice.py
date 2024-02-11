# Create an iterator for the preorder traversal of a tree

# def preorder(root):
#      if root:
#         print(root.value)
#         preorder(root.left)
#         preorder(root.right)
        
class PreorderIterator:
    def __init__(self, root):
        self.stack = [root]

    def HasNext(self):
        return bool(self.stack)

    def Next(self):
        if not self.HasNext():
            return None

        node = self.stack.pop()

        if node.right: self.stack.append(node.right)
        if node.left: self.stack.append(node.left)

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

    preorder = PreorderIterator(tree)

    print(preorder.Next(), 1)
    print(preorder.Next(), 2)
    print(preorder.Next(), 4)
    print(preorder.Next(), 5)
    print(preorder.Next(), 3)
    print(preorder.Next(), 6)
    print(preorder.Next(), 7)
    print(preorder.Next(), None)