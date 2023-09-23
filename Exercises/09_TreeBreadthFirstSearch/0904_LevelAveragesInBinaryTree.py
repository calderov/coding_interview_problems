# Problem: 
# Given a binary tree, populate an array to represent the averages of all of
# its levels.
# 
# Example:
# 
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
# Averages: [1, 2.5, 5.5]

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def LevelAverages(self, root):
        levels = []
        pending = [root]

        while pending:
            levelSize = len(pending)
            currentLevel = []
            for _ in range(levelSize):
                node = pending.pop(0)

                if node:
                    pending.append(node.left)
                    pending.append(node.right)
                    currentLevel.append(node.val)

            if currentLevel:
                levels.append(currentLevel)

        return [sum(i) / len(i) for i in levels]

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

    expectedOutput = [1.0, 2.5, 5.5]
    output = solution.LevelAverages(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()