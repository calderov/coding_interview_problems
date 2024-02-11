# Given a Binary Tree and an input array. The task is to create an Iterator
# that utilizes next() and hasNext() functions to perform Inorder traversal
# on the binary tree.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class InorderIterator:
    def __init__(self, root):
        self.stack = []
        self.findLeftMost(root)

    def findLeftMost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def has_next(self):
        return bool(self.stack)
    
    def next(self):
        if not self.stack:
            return None
     
        nextNode = self.stack.pop()

        if nextNode.right:
            self.findLeftMost(nextNode.right)

        return nextNode

if __name__ == "__main__":
    root = TreeNode(8)
    root.right = TreeNode(9)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.right.right = TreeNode(5)

    iterator = InorderIterator(root)

    print(iterator.has_next(), iterator.next().val)
    print(iterator.has_next(), iterator.next().val)
    print(iterator.has_next(), iterator.next().val)
    print(iterator.has_next(), iterator.next().val)
    print(iterator.has_next(), iterator.next().val)
    print(iterator.has_next(), iterator.next().val)
    print(iterator.has_next(), iterator.next())