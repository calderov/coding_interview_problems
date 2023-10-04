# Problem:
# Given a binary tree, find the length of its diameter. The diameter of a
# tree is the number of nodes on the longest path between any two leaf nodes.
# The diameter of a tree may or may not pass through the root.
# 
# Note: You can always assume that there are at least two leaf nodes in the
# given tree.
#
# Example:
#
#   Input:
#             ┌─┐
#        ┌────┤1├─────┐
#        │    └─┘     │
#       ┌┴┐          ┌┴┐
#       │2│       ┌──┤3├──┐
#       └─┘       │  └─┘  │
#                ┌┴┐     ┌┴┐
#              ┌─┤5├─┐   │6├─┐
#              │ └─┘ │   └─┘ │
#             ┌┴┐   ┌┴┐     ┌┴┐
#             │7│   │8├─┐   │9├─┐ 
#             └─┘   └─┘ │   └─┘ │
#                      ┌┴─┐    ┌┴─┐
#                      │10│    │11│
#                      └──┘    └──┘
#
#   Output: 7, as the longest path is [10, 8, 5, 3, 6, 9, 11]
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Solution:
    # This problem follows the Binary Tree Path Sum pattern. We can follow the
    # same DFS approach. There will be a few differences:
    # 
    # At every step, we need to find the height of both children of the
    # current node. For this, we will make two recursive calls similar to DFS.
    # 
    # The height of the current node will be equal to the maximum of the
    # heights of its left or right children, plus ‘1’ for the current node.
    #
    # The tree diameter at the current node will be equal to the height of
    # the left child plus the height of the right child plus ‘1’ for the current
    # node: diameter = leftTreeHeight + rightTreeHeight + 1. To find the overall
    # tree diameter, we will use a class level variable. This variable will store
    # the maximum diameter of all the nodes visited so far, hence, eventually, it
    # will have the final tree diameter.
    # 
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def TreeDiameter(self, root):
        diameter = [0]
        self.ComputeTreeDiameter(root, diameter)
        return diameter[0]

    def ComputeTreeDiameter(self, currentNode, diameterResult):
        if currentNode is None:
            return 0

        leftHeight = self.ComputeTreeDiameter(currentNode.left, diameterResult)
        rightHeight = self.ComputeTreeDiameter(currentNode.right, diameterResult)

        if leftHeight and rightHeight:
            diameterResult[0] = max(diameterResult[0], leftHeight + rightHeight + 1)

        return max(leftHeight, rightHeight) + 1

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(5)
    tree.right.left.left = TreeNode(7)
    tree.right.left.right = TreeNode(8)
    tree.right.left.right.right = TreeNode(10)
    tree.right.right = TreeNode(6)
    tree.right.right.right = TreeNode(9)
    tree.right.right.right.right = TreeNode(11)

    expectedOutput = 7
    output = solution.TreeDiameter(tree)
    
    print(output, expectedOutput, output == expectedOutput)
