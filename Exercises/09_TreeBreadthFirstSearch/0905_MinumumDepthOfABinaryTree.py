# Minimum Depth of a Binary Tree (easy)
# Problem Statement
# 
# Find the minimum depth of a binary tree. The minimum depth is the number of
# nodes along the shortest path from the root node to the nearest leaf node.
# 
# Example 1:
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
# Minumum depth: 2
#

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

class Solution:
    # Solution:
    # 1. Initialize a queue of items pending of traversal, a list of levels, and a
    #    variable to track if a leaf node has been found.
    #    (this will be our result).
    #      pending = []
    #      levels = []
    #      isLeaf = False
    # 
    # 2. Push the root into the pending queue.
    #
    # 3. While there are pending items in the queue and no leaf has been found: 
    #    3.1 Initialize an empty list to hold the items in the current level.
    #          currentLevel = []
    #
    #    3.2 Count the elements in the queue and save the count to a variable
    #          levelSize = len(pending)
    #
    #    3.3 Remove levelSize nodes from the queue and push them into the
    #        list representing the current level. Also, check if any of them
    #        is a leaf node, if so, set isLeaf to True.
    #
    #    3.4 For each element in the current level list, insert both of its
    #        children into the pending queue.
    #
    #    3.5 Insert the currentLevel into the levels list, and repeat step 3
    #        if there are still items in the pending queue and if isLeaf is
    #        equal to False.
    #
    # 4. Return the length of the levels list.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def MinimumDepth(self, root):
        levels = []
        pending = [root]

        isLeaf = False

        while pending and not isLeaf:
            currentLevel = []
            levelSize = len(pending)

            for _ in range(levelSize):
                node = pending.pop(0)
        
                if node:
                    pending.append(node.left)
                    pending.append(node.right)
                    currentLevel.append(node.val)
                    if node.left == None and node.right == None:
                        isLeaf = True

            if currentLevel:
                levels.append(currentLevel)

        return len(levels)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    
    expectedOutput = 2
    output = solution.MinimumDepth(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = 3
    output = solution.MinimumDepth(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    # [1, 2, 3, 4, null, 6, 7]
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = 3
    output = solution.MinimumDepth(tree)

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()