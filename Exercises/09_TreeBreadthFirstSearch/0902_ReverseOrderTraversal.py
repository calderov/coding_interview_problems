# Problem:
# Given a binary tree, populate an array to represent its level-by-level
# traversal in reverse order, i.e., the lowest level comes first. You should
# populate the values of all nodes in each level from left to right in
# separate sub-arrays.
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
# Reverse order traversal:[[4,5,6,7], [2, 3], [1]]
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
    #        list representing the current level.
    #
    #    3.4 For each element in the current level list, insert both of its
    #        children into the pending queue.
    #
    #    3.5 Insert the currentLevel at the beginning of the levels list, 
    #        and repeat step 3 if there are still items in the pending queue.
    #
    # 4. Return the levels list and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def ReverseOrderTraversal(self, root: TreeNode):
        levels = []
        pending = [root]

        while pending:
            levelSize = len(pending)
            currentLevel = []

            for _ in range(levelSize):
                node = pending.pop(0)

                if node:
                    pending.append(node.left)
                    pending.append(node.right)
                    currentLevel.append(node.val)

            if currentLevel:
                levels.insert(0, currentLevel)
            
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

    expectedOutput = [[4,5,6,7], [2, 3], [1]]
    output = solution.ReverseOrderTraversal(tree)
    
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()