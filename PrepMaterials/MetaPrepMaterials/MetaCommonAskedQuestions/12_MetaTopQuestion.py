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

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def rangeSumOfBST(root, low, high):
    if not root:
        return 0
    
    if root.val < low:
        return rangeSumOfBST(root.right, low, high)

    if root.val > high:
        return rangeSumOfBST(root.left, low, high)

    return root.val + rangeSumOfBST(root.left, low, high) + rangeSumOfBST(root.right, low, high)

def listToTree(values, index=0):
    if not values or index < 0 or index >= len(values) or values[index] == None:
        return None
    
    node = Node(values[index])
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    node.left = listToTree(values, leftIndex)
    node.right = listToTree(values, rightIndex)

    return node
    
if __name__ == "__main__":
    # Example 1
    root = listToTree([10,5,15,3,7,None,18])
    low = 7
    high = 15
    expectedOutput = 32
    output = rangeSumOfBST(root, low, high)
    print(output, expectedOutput, output == expectedOutput)
  
    # Example 2
    root = listToTree([10,5,15,3,7,13,18,1,None,6])
    low = 6
    high = 10
    expectedOutput = 23
    output = rangeSumOfBST(root, low, high)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    root = listToTree([10,5,15,3,7,13,18,1,None,6])
    low = 0
    high = 100
    expectedOutput = 78
    output = rangeSumOfBST(root, low, high)
    print(output, expectedOutput, output == expectedOutput)