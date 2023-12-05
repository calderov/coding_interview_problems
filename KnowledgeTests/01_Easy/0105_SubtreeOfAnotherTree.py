# Problem:
# Given two binary trees s and t, determine if tree t is a subtree of tree s.
# A tree t is considered a subtree of s if there exists a node in s such that
# the subtree of that node is identical to t. Both trees are considered
# identical if their structure and nodes are the same.
#
# Example
#
#  Tree s:
#             ┌─┐
#        ┌────┤3├────┐
#        │    └─┘    │
#       ┌┴┐         ┌┴┐
#     ┌─┤4├─┐       │5│
#     │ └─┘ │       └─┘
#    ┌┴┐   ┌┴┐
#    │1│   │2│
#    └─┘   └─┘
#
#  Tree t:
#             ┌─┐
#        ┌────┤4├────┐
#        │    └─┘    │
#       ┌┴┐         ┌┴┐
#       │1│         │2│
#       └─┘         └─┘
#
#  Is t a subtree of s: True
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Time complexity:
    # Space complexity:
    def IsSubTree(self, tree, subtree):
        if not tree:
            return False

        return self.IsSubTreeRootedAtRoot(tree, subtree) or self.IsSubTree(tree.left, subtree) or self.IsSubTree(tree.right, subtree)

    def IsSubTreeRootedAtRoot(self, tree, subtree):
        if not tree and not subtree:
            return True

        if not tree or not subtree:
            return False

        if tree.val != subtree.val:
            return False

        return self.IsSubTreeRootedAtRoot(tree.left, subtree.left) and self.IsSubTreeRootedAtRoot(tree.right, subtree.right)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(3)
    tree.left = TreeNode(4)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(2)

    subtree = TreeNode(4)
    subtree.left = TreeNode(1)
    subtree.right = TreeNode(2)

    expectedOutput = True
    output = solution.IsSubTree(tree, subtree)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2 (based on Example 1)
    tree.left.right.left = TreeNode(0)

    expectedOutput = False
    output = solution.IsSubTree(tree, subtree)
    print(output, expectedOutput, output == expectedOutput)