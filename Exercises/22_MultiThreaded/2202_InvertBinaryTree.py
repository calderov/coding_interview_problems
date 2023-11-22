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
    def InvertTreeSingleThread(self, tree):
        if not tree:
            return

        tree.left, tree.right = tree.right, tree.left

        self.InvertTreeSingleThread(tree.left)
        self.InvertTreeSingleThread(tree.right)

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