# Problem:
# Given a binary tree and a number S, find if the tree has a path from
# root-to-leaf such that the sum of all the node values of that path equals
# S.
#
# Example:
#
#   Input:
#             ┌─┐
#        ┌────┤1├────┐
#        │    └─┘    │
#       ┌┴┐         ┌┴┐
#     ┌─┤2├─┐     ┌─┤3├─┐
#     │ └─┘ │     │ └─┘ │
#    ┌┴┐   ┌┴┐   ┌┴┐   ┌┴┐
#    │4│   │5│   │6│   │7│
#    └─┘   └─┘   └─┘   └─┘
#
#   S = 10
#
# Output: True
# Explication: 1 + 3 + 6 = 10
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Solution:
    # Use a DFS approach and check if a given node is a leaf and if its value is equal to
    # a given target. If that's the case, return True. Otherwise, recursively call this method
    # again, passing the left and right neighbors of the node as input and the value of the
    # current node substracted from the target value, as the new target value.
    #
    # Solution complexity:
    # Time complexity: O(n) as each element is explored only once
    # Space complexity: O(n)
    def FindSumDFS(self, root, targetSum):
        if not root:
            return False

        if root.val == targetSum and not root.left and not root.right:
            return True

        return self.FindSumDFS(root.left, targetSum - root.val) or self.FindSumDFS(root.right, targetSum - root.val)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    s = 10

    expectedOutput = True
    output = solution.FindSumDFS(tree, s)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
