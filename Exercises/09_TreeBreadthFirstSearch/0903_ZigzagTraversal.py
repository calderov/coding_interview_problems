# Problem:
# Given a binary tree, populate an array to represent its zigzag level order
# traversal. You should populate the values of all nodes of the first level
# from left to right, then right to left for the next level and keep
# alternating in the same manner for the following levels.
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
# Zigzag order traversal: [[1], [3, 2], [4, 5, 6, 7]]
#

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    # Solution:
    # 1. Initialize a queue of items pending of traversal and an a list of levels
    #    (this will be our result).
    #      pending = []
    #      levels = []
    # 
    # 2. Initialize a variable to keep track if a given level shold be stored from
    #    left to right.
    #      leftToRight = True
    #
    # 2. Push the root into the pending queue.
    #
    # 3. While there are pending items in the queue: 
    #    3.1 Initialize an empty list to hold the items in the current level.
    #          currentLevel = []
    #
    #    3.2 Count the elements in the queue and save the count to a variable
    #          levelSize = len(pending)
    #
    #    3.3 Remove levelSize nodes from the queue and push them into the
    #        list representing the current level. Do this from left to right
    #        if leftToRight is True or from right to left if not.
    #
    #    3.4 For each element in the current level list, insert both of its
    #        children into the pending queue.
    #
    #    3.5 Append the currentLevel at the end of the levels list.
    #
    #    3.6 Negate the current value of leftToRight and repeat step 3 if there
    #        are still items in the pending queue.
    #          leftToRight = not leftToRight
    #
    # 4. Return the levels list and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def ZigzagTraversal(self, root):
        levels = []
        pending = [root]
        
        leftToRight = True
        
        while pending:
            levelSize = len(pending)
            currentLevel = []

            for _ in range(levelSize):
                node = pending.pop(0)

                if node:
                    pending.append(node.left)
                    pending.append(node.right)

                    if leftToRight:
                        currentLevel.append(node.val)
                    else:
                        currentLevel.insert(0, node.val)
            
            if currentLevel:
                levels.append(currentLevel)

            leftToRight = not leftToRight
        
        return levels

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

    expectedOutput = [[1], [3, 2], [4, 5, 6, 7]]
    output = solution.ZigzagTraversal(tree)
    
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    