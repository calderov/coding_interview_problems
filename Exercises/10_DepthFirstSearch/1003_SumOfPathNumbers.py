# Problem:
# Given a binary tree where each node can only have a digit (0-9) value, each
# root-to-leaf path will represent a number. Find the total sum of all the
# numbers represented by all paths.
# 
# Example:
# 
#   Input:
#             ┌─┐
#        ┌────┤1├────┐
#        │    └─┘    │
#       ┌┴┐         ┌┴┐
#       │7│       ┌─┤9├─┐
#       └─┘       │ └─┘ │
#                ┌┴┐   ┌┴┐
#                │2│   │9│
#                └─┘   └─┘ 
# 
#   Output: 408
#   Explanation: 17 + 192 + 199
# 

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Solution:
    # 1. Use DFS to compute a list with all the paths in the tree.
    #
    # 2. Sum all the numbers encoded in the paths.
    #
    # 3. Return the total sum and finish.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n log(n))
    def SumOfAllPaths(self, root):
        # Compute all paths
        allPaths = []
        self.AllPathsDFS(root, [], allPaths)

        # Add the numbers encoded in the paths
        totalSum = 0
        for path in allPaths:
            totalSum += self.PathToNumber(path)
        
        # Return total sum
        return totalSum
    
    def AllPathsDFS(self, node, visited, allPaths):
        if not node:
            return
        
        if not node.left and not node.right:
            allPaths.append(visited + [node.val])
        
        self.AllPathsDFS(node.left, visited + [node.val], allPaths)
        self.AllPathsDFS(node.right, visited + [node.val], allPaths)

    def PathToNumber(self, path):
        num = 0
        power = len(path) - 1

        for digit in path:
            num += digit * 10 ** power
            power -= 1
        
        return num

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(7)
    tree.right = TreeNode(9)
    tree.right.left = TreeNode(2)
    tree.right.right = TreeNode(9)

    expectedOutput = 408
    output = solution.SumOfAllPaths(tree)
    print(output, expectedOutput, output == expectedOutput)
