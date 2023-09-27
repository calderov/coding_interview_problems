# Problem:
# Given a binary tree and a number S, find all paths in the tree such that
# the sum of all the node values of each path equals S. Please note that
# the paths can start or end at any node but all paths must follow direction
# from parent to child (top to bottom).
#
# Example:
#
#   Input:
#             ┌─┐
#        ┌────┤1├────┐
#        │    └─┘    │
#       ┌┴┐         ┌┴┐
#     ┌─┤7├─┐     ┌─┤9├─┐
#     │ └─┘ │     │ └─┘ │
#    ┌┴┐   ┌┴┐   ┌┴┐   ┌┴┐
#    │6│   │5│   │2│   │3│
#    └─┘   └─┘   └─┘   └─┘
#
#   S = 12
#
# Output: 3
# Explication: There are three paths with sum 12: [7 5], [1 9 2], [9 3]
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # Solution:
    # Use DFS to recursively traverse the node. On each node, keep track of the count
    # of paths with subsequences that add up to the target sum up to this node.
    # 
    # Increase this count by one if the addition of the current node to the path, produces
    # a subsequence that adds up to the target sum.
    #
    # Recursively increase this count once again by the respective path counts on the left and right
    # nodes.
    #
    # Remove the current node from the path before returning the path count upwards, to avoid
    # messing up with backtracking.
    #
    # Solution complexity:
    # Time complexity: O(n ^ 2) due to the constant compution of the sum of
    #                  visited nodes for each new node in the branch
    # Space complexity: O(n) due to the recursion stack
    def CountPathsForSumDFS(self, node, targetSum, currentPath=[]):
        if not node:
            return 0
        
        currentPath.append(node.val)
        n = len(currentPath)
        pathCount = 0
        pathSum = 0

        for i in range(n):
            pathSum += currentPath[n - 1 - i]
            if pathSum == targetSum:
                pathCount += 1
                break

        pathCount += self.CountPathsForSumDFS(node.left, targetSum, currentPath)
        pathCount += self.CountPathsForSumDFS(node.right, targetSum, currentPath)

        del currentPath[-1]

        return pathCount

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(7)
    tree.right = TreeNode(9)
    tree.left.left = TreeNode(6)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(2)
    tree.right.right = TreeNode(3)

    s = 12

    expectedOutput = 3
    output = solution.CountPathsForSumDFS(tree, s)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    tree = TreeNode(1)
    tree.left = TreeNode(0)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(1)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(5)
    
    s = 2

    expectedOutput = 2
    output = solution.CountPathsForSumDFS(tree, s)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    tree = TreeNode(4)
    
    tree.left = TreeNode(4)
    tree.right = TreeNode(4)
    
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(4)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(4)
    
    tree.left.left.left = TreeNode(4)
    tree.left.left.right = TreeNode(4)
    tree.left.right.left = TreeNode(4)
    tree.left.right.right = TreeNode(4)

    s = 8

    expectedOutput = 10
    output = solution.CountPathsForSumDFS(tree, s)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()