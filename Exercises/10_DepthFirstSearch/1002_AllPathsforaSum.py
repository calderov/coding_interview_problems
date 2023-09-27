# Problem:
# Given a binary tree and a number S, find all paths from root-to-leaf such
# that the sum of all the node values of each path equals S.
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
#    │4│   │5│   │2│   │7│
#    └─┘   └─┘   └─┘   └─┘
#
#   S = 12
#
# Output: [[1, 7, 4], [1, 9, 2]]
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Solution:
    # Use a DFS approach to traverse the tree. Checking for each node,
    # if the node is a leaf and if the sum of the previous nodes in
    # the path, plus the node's value is equal to the desired sum.
    # If this is the case, append the visited nodes plus the current node
    # to a list of all paths that serves as the result. Return the result
    # list and finish.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n log(n))
    def AllPathsForASum(self, node, targetSum):
        allPaths = []
        self.AllPathsForASumDFS(node, targetSum, [], allPaths)
        return allPaths

    def AllPathsForASumDFS(self, node, targetSum, visited, allPaths):
        if not node:
            return

        if not node.left and not node.right and sum(visited) + node.val == targetSum:
            allPaths.append(visited + [node.val])

        self.AllPathsForASumDFS(node.left, targetSum, visited + [node.val], allPaths)
        self.AllPathsForASumDFS(node.right, targetSum, visited  + [node.val], allPaths)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(7)
    tree.right = TreeNode(9)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(2)
    tree.right.right = TreeNode(7)

    s = 12

    expectedOutput = [[1, 7, 4], [1, 9, 2]]
    output = solution.AllPathsForASum(tree, s)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()