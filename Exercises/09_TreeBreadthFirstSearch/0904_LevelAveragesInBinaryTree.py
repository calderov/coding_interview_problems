# Problem: 
# Given a binary tree, populate an array to represent the averages of all of
# its levels.
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
# Averages: [1, 2.5, 5.5]

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
    #    3.5 Insert the currentLevel into the levels list, and repeat step 3
    #        if there are still items in the pending queue.
    #
    # 4. Now that the levels list contains all of the elements in the tree grouped by level,
    #    compute average value on each level and place it in a new list. Return this list
    #    of average values and finish.
    #       return [sum(i) / len(i) for i in levels]
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def LevelAverages(self, root):
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
                levels.append(currentLevel)

        return [sum(i) / len(i) for i in levels]

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

    expectedOutput = [1.0, 2.5, 5.5]
    output = solution.LevelAverages(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()