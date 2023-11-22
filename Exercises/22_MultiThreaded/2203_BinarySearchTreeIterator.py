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

import multiprocessing

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

# Solution:
# Traverse the tree on demand using a stack to store the in order traversal of the tree.
# 
# Solution complexity:
# Time complexity: The hasNext function has a constant time complexity O(1), 
#                  the next function has a time complexity of O(n) where n
#                  is the number of nodes in the tree.
#
# Space complexity: The has next function has a constant time complexity O(1),
#                   the next function has a time complexity of O(h) where h
#                   is the height of the tree.
class Solution:
    def __init__(self, root):
        self.inOrderStack = []
        self.lock = multiprocessing.Lock()
        self.traverseLeft(root)

    def hasNext(self):
        return len(self.inOrderStack) > 0

    def next(self):
        self.lock.acquire()
        nextNode = self.inOrderStack.pop()
        self.traverseLeft(nextNode.right)
        self.lock.release()
        return nextNode.val

    def traverseLeft(self, node):
        while node:
            self.inOrderStack.append(node)
            node = node.left

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