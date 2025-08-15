# 129. Sum Root to Leaf Numbers (Medium)
# You are given the root of a binary tree containing digits from 0 to 9 only.
#
# Each root-to-leaf path in the tree represents a number.
#
# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated
# so that the answer will fit in a 32-bit integer.
#
# A leaf node is a node with no children.
#
# Example 1:
#   Input: root = [1,2,3]
#   Output: 25
#   Explanation:
#     The root-to-leaf path 1->2 represents the number 12.
#     The root-to-leaf path 1->3 represents the number 13.
#     Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#   Input: root = [4,9,0,5,1]
#   Output: 1026
#   Explanation:
#     The root-to-leaf path 4->9->5 represents the number 495.
#     The root-to-leaf path 4->9->1 represents the number 491.
#     The root-to-leaf path 4->0 represents the number 40.
#     Therefore, sum = 495 + 491 + 40 = 1026.
#
# Constraints:
# - The number of nodes in the tree is in the range [1, 1000].
# - 0 <= Node.val <= 9
# - The depth of the tree will not exceed 10.

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def SumNumbers(self, root):
        if not root:
            return 0

        pending = [(root, 0)]
        totalSum = 0

        while pending:
            node, currentSum = pending.pop()

            currentSum = 10 * currentSum + node.val

            if not node.left and not node.right:
                totalSum += currentSum
                continue

            if node.left:
                pending.append((node.left, currentSum))

            if node.right:
                pending.append((node.right, currentSum))

        return totalSum

    def PythonListToTree(self, values, index=0):
        if not values:
            None

        if index > len(values):
            raise Exception('Index out of range')

        root = TreeNode(values[index])

        leftIndex = 2 * index + 1
        rightIndex = 2 * index + 2

        if leftIndex < len(values):
            root.left = self.PythonListToTree(values, leftIndex)

        if rightIndex< len(values):
            root.right = self.PythonListToTree(values, rightIndex)

        return root

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    root = [1,2,3]
    expectedOutput = 25
    output = solution.SumNumbers(solution.PythonListToTree(root))
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    root = [4,9,0,5,1]
    expectedOutput = 1026
    output = solution.SumNumbers(solution.PythonListToTree(root))
    print(output, expectedOutput, output == expectedOutput)