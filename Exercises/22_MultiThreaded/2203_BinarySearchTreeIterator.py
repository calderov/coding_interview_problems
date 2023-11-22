# Problem Statement
# Implement an iterator for the in-order traversal of a binary search tree
# (BST). That is, given a BST, we need to implement two functions:
# 
# bool hasNext(): Returns true if at least one element is left in the
# in-order traversal of the BST. int next(): Return the next element in the
# in-order traversal of the BST.
#
# Example:
#             ┌──┐
#          ┌──┤10├──┐
#          │  └──┘  │
#          │        │
#          │        │
#          ▼        ▼
#         ┌──┐    ┌──┐
#      ┌──┤ 4│  ┌─┤15├──┐
#      │  └──┘  │ └──┘  │
#      │        │       │
#      │        │       │
#      ▼        ▼       ▼
#     ┌──┐     ┌──┐    ┌──┐
#     │ 1│     │14│    │19├──┐
#     └──┘     └──┘    └──┘  │
#                            │
#                            │
#                            ▼
#                           ┌──┐
#                           │20│
#                           └──┘
#
# In order traversal: [1, 4, 10, 14, 15, 19, 20]
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self, tree):
        self.inOrderList = []
        self.nextPointer = 0
        self.inOrderTraversal(tree, self.inOrderList)

    def hasNext(self):
        return self.nextPointer < len(self.inOrderList)

    def next(self):
        result = None
        if self.hasNext():
            result = self.inOrderList[self.nextPointer]
            self.nextPointer += 1
        return result

    def inOrderTraversal(self, tree, inOrderList):
        if tree.left:
            self.inOrderTraversal(tree.left, inOrderList)

        inOrderList.append(tree.val)

        if tree.right:
            self.inOrderTraversal(tree.right, inOrderList)

if __name__ == "__main__":
    # Example 1
    tree = TreeNode(10)
    tree.left = TreeNode(4)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(1)
    tree.right.left = TreeNode(14)
    tree.right.right = TreeNode(19)
    tree.right.right.right = TreeNode(20)

    inOrderIterator = Solution(tree)
    
    print("%s\t%s" %(inOrderIterator.hasNext(), True))
    print("%s\t%s" %(inOrderIterator.next(), 1))
    print("%s\t%s" %(inOrderIterator.next(), 4))
    print("%s\t%s" %(inOrderIterator.hasNext(), True))
    print("%s\t%s" %(inOrderIterator.next(), 10))
    print("%s\t%s" %(inOrderIterator.next(), 14))
    print("%s\t%s" %(inOrderIterator.next(), 15))
    print("%s\t%s" %(inOrderIterator.next(), 19))
    print("%s\t%s" %(inOrderIterator.next(), 20))
    print("%s\t%s" %(inOrderIterator.hasNext(), False))