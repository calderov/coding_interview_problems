# Problem:
# Given a binary tree, return an array containing nodes in its right view.
# The right view of a binary tree is the set of nodes visible when the tree
# is seen from the right side.
#
# Example:
#           ┌─┐
#      ┌────┤1├────┐
#      │    └─┘    │
#     ┌┴┐         ┌┴┐
#   ┌─┤2├─┐     ┌─┤3├─┐
#   │ └─┘ │     │ └─┘ │
#  ┌┴┐   ┌┴┐   ┌┴┐   ┌┴┐
#  │4│   │5│   │6│   │7│
#  └─┘   └─┘   └─┘   └─┘
#
# Right view: [1, 3, 7]
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def RightView(self, root):
        pending = [root]
        result = []
        
        while pending:
            levelSize = len(pending)

            for i in range(levelSize):
                node = pending.pop(0)

                if node.left: pending.append(node.left)
                if node.right: pending.append(node.right)

                if i == levelSize - 1: result.append(node.val)
        
        return result

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

    expectedOutput = [1, 3, 7]
    output = solution.RightView(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    tree = TreeNode(12)
    tree.left = TreeNode(7)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(9)
    tree.left.left.left = TreeNode(3)
    tree.right.left = TreeNode(10)
    tree.right.right = TreeNode(5)

    expectedOutput = [12, 1, 5, 3]
    output = solution.RightView(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()