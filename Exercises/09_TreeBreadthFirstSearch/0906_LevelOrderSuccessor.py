# Problem:
# Given a binary tree and a node, find the level order successor of the given
# node in the tree. The level order successor is the node that appears right
# after the given node in the level order traversal.
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
# Given node: 3
# Level order successor: 4
#

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    # Solution:
    # Initialize a flag variable isValueFound to False. Then, use BFS to traverse 
    # the tree level by level. 
    # 
    # For each node in the traversal:
    #  - Check if the flag variable isValueFound is True and return the current node if that's the case. 
    #  - Otherwise, check if the node node matches the given value k. If so, set isValueFound to True. 
    #    This will return the next node in traversal in the next interation.
    #
    # If all the nodes were traversed and the none of them matched with the given value k, return None.
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def LevelOrderSuccessor(self, root, k):
        pending = [root]
        isValueFound = False
        
        while pending:
            node = pending.pop(0)
            
            if node:
                if isValueFound:
                    return node.val
                
                pending.append(node.left)
                pending.append(node.right)

                if node.val == k:
                    isValueFound = True
        
        return None


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    k = 3
    expectedOutput = 4
    output = solution.LevelOrderSuccessor(tree, k)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()