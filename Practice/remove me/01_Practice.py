# Minimum Depth of a Binary Tree (easy)
# Problem Statement
# 
# Find the minimum depth of a binary tree. The minimum depth is the number of
# nodes along the shortest path from the root node to the nearest leaf node.
# 
# Example:
# 
#           ┌─┐
#      ┌────┤1├────┐
#      │    └─┘    │
#     ┌┴┐         ┌┴┐
#   ┌─┤2├─┐       │3│
#   │ └─┘ │       └─┘
#  ┌┴┐   ┌┴┐
#  │4│   │5│
#  └─┘   └─┘
#
# Minumum depth: 2
#

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    def MinimumDepth(self, root):
        if not root:
            return 0
        
        pending = [root]
        minDepth = 0

        while pending:
            minDepth += 1
            nodesInLevel = len(pending)

            for _ in range(nodesInLevel):
                node = pending.pop(0)

                if not node.left and not node.right:
                    return minDepth

                if node.left:
                    pending.append(node.left)

                if node.right:
                    pending.append(node.right)
                

        return minDepth
            
        

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    
    expectedOutput = 2
    output = solution.MinimumDepth(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = 3
    output = solution.MinimumDepth(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    # [1, 2, 3, 4, null, 6, 7]
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = 3
    output = solution.MinimumDepth(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()