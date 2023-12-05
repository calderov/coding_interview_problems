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
    def IsSubTree(self, treeS, treeT):
        roots = []
        self.FindNodesWithValue(treeS, treeT.val, roots)

        for root in roots:
            if self.IsSubTreeRootedAtRoot(root, treeT):
                return True

        return False

    def IsSubTreeRootedAtRoot(self, tree, subtree):
        if not tree and not subtree:
            return True

        if tree and not subtree:
            return True

        if subtree and not tree:
            return False

        if tree.val != subtree.val:
            return False

        return self.IsSubTreeRootedAtRoot(tree.left, subtree.left) and self.IsSubTreeRootedAtRoot(tree.right, subtree.right)

    def FindNodesWithValue(self, tree, value, roots=[]):
        if not tree:
            return

        if tree.val == value:
            roots.append(tree)

        self.FindNodesWithValue(tree.left, value, roots)
        self.FindNodesWithValue(tree.right, value, roots)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    treeS = TreeNode(3)
    treeS.left = TreeNode(4)
    treeS.right = TreeNode(5)
    treeS.left.left = TreeNode(1)
    treeS.left.right = TreeNode(2)

    treeT = TreeNode(4)
    treeT.left = TreeNode(1)
    treeT.right = TreeNode(2)

    expectedOutput = True
    output = solution.IsSubTree(treeS, treeT)
    print(output, expectedOutput, output == expectedOutput)