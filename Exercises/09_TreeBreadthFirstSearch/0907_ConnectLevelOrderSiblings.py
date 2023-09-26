# Problem:
# Given a binary tree, connect each node with its level order successor. The
# last node of each level should point to a null node.
#
# Example:
#
#            ┌─┬──────────────┐
#       ┌────┤1├────┐         ▼
#       │    └─┘    │       ┌────┐
#      ┌┴┬────────►┌┴┬─────►│Null│
#    ┌─┤2├─┐     ┌─┤3├─┐    └────┘
#    │ └─┘ │     │ └─┘ │      ▲
#   ┌┴┐   ┌┴┐   ┌┴┐   ┌┴┐     │
#   │4├──►│5├──►│6├──►│7├─────┘
#   └─┘   └─┘   └─┘   └─┘
#
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # Solution:
    # Traverse the tree using BFS. On each level, remember the previous node to
    # connect it with the current node.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def ConnectLevelOrderSiblings(self, root: TreeNode):
        if not root:
            return

        pending = [root]

        while pending:
            prevNode = None
            levelSize = len(pending)

            for _ in range(levelSize):
                node = pending.pop(0)

                if prevNode:
                    prevNode.next = node

                prevNode = node

                if node.left: pending.append(node.left)
                if node.right: pending.append(node.right)

        return root

    # This code was given as part of the problem (it is pretty bad IMO)
    def print_level_order(self, root):
        result = []
        nextLevelRoot = root
        while nextLevelRoot:
            innerResult = []
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                innerResult.append(current.val)
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            result.append(innerResult)
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

    expectedOutput = [[1], [2, 3], [4, 5, 6, 7]]
    output = solution.print_level_order(solution.ConnectLevelOrderSiblingsV2(tree))

    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
