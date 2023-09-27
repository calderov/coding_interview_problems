# Problem: 
# Given a binary tree and a number sequence, find if the sequence is present
# as a root-to-leaf path in the given tree.
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
#   sequence = [1, 9, 9]
#
#   Output: True
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # Solution:
    # Use DFS to traverse the tree, tracking the element of the given sequence
    # that should match with the current node. Returning False as soon as mismatch
    # is found. If the algorithm ends up finding a leaf that matches the last element
    # on the sequence, then the whole sequence is known to be in the tree. Return True
    # in this case.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n log(n))
    def IsSequenceInTree(self, node, sequence, index=0):
        if not node or index >= len(sequence) or sequence[index] != node.val:
            return False
        
        if index == len(sequence) - 1 and not node.left and not node.right and node.val == sequence[index]:
            return True
            
        return self.IsSequenceInTree(node.left, sequence, index + 1) or self.IsSequenceInTree(node.right, sequence, index + 1)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(7)
    tree.right = TreeNode(9)
    tree.right.left = TreeNode(2)
    tree.right.right = TreeNode(9)

    sequence = [1, 9, 9]

    expectedOutput = True
    output = solution.IsSequenceInTree(tree, sequence)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    sequence = [1, 9, 3]

    expectedOutput = False
    output = solution.IsSequenceInTree(tree, sequence)
    print(output, expectedOutput, output == expectedOutput)
