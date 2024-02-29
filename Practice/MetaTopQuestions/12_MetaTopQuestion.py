# 938. Range Sum of BST (Easy)
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range
# [low, high].
# 
# Example 1:
#   Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
#   Output: 32
#   Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
# 
# Example 2:
#   Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
#   Output: 23
#   Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
# 
# Constraints:
# - The number of nodes in the tree is in the range [1, 2 * 104].
# - 1 <= Node.val <= 105
# - 1 <= low <= high <= 105
# - All Node.val are unique.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def RangeSumOfBST(self, root, low, high):
        valuesInRange = []
        pending = [root]
        while pending:
            nodesInLevel = len(pending)
            for _ in range(nodesInLevel):
                node = pending.pop(0)

                if low <= node.val and node.val <= high:
                    valuesInRange.append(node.val)

                if node.left:
                    pending.append(node.left)
                
                if node.right:
                    pending.append(node.right)

        return sum(valuesInRange)

def ListToTree(values, index=0):
    if not values or not values[index]:
        return None
    
    if index >= len(values):
        raise Exception('Index out of range')
    
    root = TreeNode(values[index])
    
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    if leftIndex < len(values):
        root.left = ListToTree(values, leftIndex)
    
    if rightIndex < len(values):
        root.right = ListToTree(values, rightIndex)
    
    return root
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root = ListToTree([10,5,15,3,7,None,18])
    low = 7
    high = 15
    expectedOutput = 32
    output = solution.RangeSumOfBST(root, low, high)
    print(output, expectedOutput, output == expectedOutput)
  
    # Example 2
    root = ListToTree([10,5,15,3,7,13,18,1,None,6])
    low = 6
    high = 10
    expectedOutput = 23
    output = solution.RangeSumOfBST(root, low, high)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    root = ListToTree([10,5,15,3,7,13,18,1,None,6])
    low = 0
    high = 100
    expectedOutput = 78
    output = solution.RangeSumOfBST(root, low, high)
    print(output, expectedOutput, output == expectedOutput)