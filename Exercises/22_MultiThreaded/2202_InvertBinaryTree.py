# Problem:
# Given the root of a binary tree, invert it.
#
# Example:
#
#  Input:
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
#  Output:
#
#             ┌──┐
#          ┌──┤10├──┐
#          │  └──┘  │
#          │        │
#          │        │
#          ▼        ▼
#         ┌──┐    ┌──┐
#      ┌──┤15│  ┌─┤ 4├──┐
#      │  └──┘  │ └──┘  │
#      │        │       │
#      │        │       │
#      ▼        ▼       ▼
#     ┌──┐     ┌──┐    ┌──┐
#  ┌──┤19│     │14│    │ 1│
#  │  └──┘     └──┘    └──┘
#  │
#  │
#  ▼
# ┌──┐
# │20│
# └──┘
#

import os
import threading

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

class Solution:
    # Single thread solution:
    # Recursively traverse the tree from the root. At each step of recursion
    # check if the root is null, if this is the case, just return. Otherwise,
    # swap the left and right nodes and recursively call this same function
    # on the left and right subtrees.
    # 
    # Solution complexity:
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(h) where h is the height of the tree (due to the recursion stack)
    def InvertTreeSingleThread(self, tree):
        if not tree:
            return

        tree.left, tree.right = tree.right, tree.left

        self.InvertTreeSingleThread(tree.left)
        self.InvertTreeSingleThread(tree.right)

    # Single thread solution:
    # Recursively traverse the tree from the root. At each step of recursion
    # check if the root is null, if this is the case, just return. Otherwise,
    # swap the left and right nodes and recursively call this same function
    # on the left and right subtrees. You can speed up the exploration of subtrees
    # by spawning a new thread for the left subtrees, and using the current node for right
    # subtrees.
    # 
    # Solution complexity:
    # Time complexity: O(n) where n is the number of nodes in the tree
    # Space complexity: O(h) where h is the height of the tree (due to the recursion stack)
    def InvertTreeMultiThread(self, tree, numThreads):
        if not tree:
            return
        
        tree.left, tree.right = tree.right, tree.left
        if numThreads > 0:
            def InvertLeft():
                self.InvertTreeMultiThread(tree.left, 0)
            t1 = threading.Thread(target=InvertLeft)
            t1.start()

            self.InvertTreeMultiThread(tree.right, 0)

            t1.join()
        else:
            self.InvertTreeMultiThread(tree.left, 0)
            self.InvertTreeMultiThread(tree.right, 0)

    def InvertTree(self, tree):
        return self.InvertTreeMultiThread(tree, os.cpu_count())

    def IsSameTree(self, tree1, tree2):
        if not tree1 and not tree2:
            return True
        
        if not tree1 or not tree2:
            return False
        
        if tree1.val != tree2.val:
            return False
        
        return self.IsSameTree(tree1.left, tree2.left) and self.IsSameTree(tree1.right, tree2.right)

if __name__ == "__main__":
    solution = Solution()

    tree = TreeNode(10)
    tree.left = TreeNode(4)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(1)
    tree.right.left = TreeNode(14)
    tree.right.right = TreeNode(19)
    tree.right.right.right = TreeNode(20)

    invertedTree = TreeNode(10)
    invertedTree.right = TreeNode(4)
    invertedTree.left = TreeNode(15)
    invertedTree.right.right = TreeNode(1)
    invertedTree.left.right = TreeNode(14)
    invertedTree.left.left = TreeNode(19)
    invertedTree.left.left.left = TreeNode(20)

    solution.InvertTree(tree)

    print(solution.IsSameTree(tree, invertedTree))