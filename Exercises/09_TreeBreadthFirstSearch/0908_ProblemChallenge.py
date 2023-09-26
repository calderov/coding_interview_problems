# Problem:
# Given a binary tree, connect each node with its level order successor. The
# last node of each level should point to the first node of the next level.
#
# Example:
#
#              ┌─┬─────────┐
#         ┌────┤1├────┐    │
#         │    └─┘    │    │
#  ┌─────┬┴┐◄────────┬┴┐◄──┘
#  │   ┌─┤2├─┐     ┌─┤3├─┐
#  │   │ └─┘ │     │ └─┘ │
#  │  ┌┴┐   ┌┴┐   ┌┴┐   ┌┴┐    ┌────┐
#  └─►│4├──►│5├──►│6├──►│7├──► │Null│
#     └─┘   └─┘   └─┘   └─┘    └────┘
#

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # Solution:
    # Traverse the tree using BFS remembering the previous node irrespective of
    # the level to connect it with the current node.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def ConnectAllLevelOrderSiblings(self, root):
        pending = [root]
        prevNode = None

        while pending:
            levelSize = len(pending)

            for _ in range(levelSize):
                node = pending.pop(0)

                if node.left: pending.append(node.left)
                if node.right: pending.append(node.right)
                if prevNode: prevNode.next = node
                prevNode = node

        return root

    def print_level_order(self, root):
        result = []
        current = root
        while current:
            result.append(current.val)
            current = current.next
        return result

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

    expectedOutput = [1, 2, 3, 4, 5, 6, 7]
    output = solution.print_level_order(solution.ConnectAllLevelOrderSiblings(tree))
    
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
