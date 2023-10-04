# Problem:
# Find the path with the maximum sum in a given binary tree. Write a function
# that returns the maximum sum.
# 
# A path can be defined as a sequence of nodes between any two nodes and
# doesn’t necessarily pass through the root. The path must contain at least
# one node.
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
#   Output: 52
#   Explanation: 10 + 8 + 5 + 3 + 6 + 9 + 11 = 52
#

import math

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Solution:
    # This problem follows the Binary Tree Path Sum pattern and shares the
    # algorithmic logic with Tree Diameter. We can follow the same DFS approach.
    # The only difference will be to ignore the paths with negative sums. Since
    # we need to find the overall maximum sum, we should ignore any path which
    # has an overall negative sum.
    #
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def MaximumPathSum(self, root):
        self.maxSumResult = -math.inf
        self.ComputeMaximumPathSum(root)
        return self.maxSumResult

    def ComputeMaximumPathSum(self, node):
        if not node:
            return 0

        leftSum = self.ComputeMaximumPathSum(node.left)
        rightSum = self.ComputeMaximumPathSum(node.right)

        # Ignore paths with negative sums
        leftSum = max(leftSum, 0)
        rightSum = max(rightSum, 0)

        self.maxSumResult = max(self.maxSumResult, leftSum + rightSum + node.val)

        return max(leftSum, rightSum) + node.val

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

    expectedOutput = 52
    output = solution.MaximumPathSum(tree)
    
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    tree = TreeNode(-1)
    tree.left = TreeNode(-3)

    expectedOutput = -1
    output = solution.MaximumPathSum(tree)
    
    print(output, expectedOutput, output == expectedOutput)