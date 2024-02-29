# 426. Convert Binary Search Tree to Sorted Doubly Linked List (Medium)
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in
# place.
# 
# You can think of the left and right pointers as synonymous to the
# predecessor and successor pointers in a doubly-linked list. For a circular
# doubly linked list, the predecessor of the first element is the last
# element, and the successor of the last element is the first element.
# 
# We want to do the transformation in place. After the transformation, the
# left pointer of the tree node should point to its predecessor, and the
# right pointer should point to its successor. You should return the pointer
# to the smallest element of the linked list.
# 
# Example 1:
#   Input: root = [4,2,5,1,3]
#   Output: [1,2,3,4,5]
#   Explanation: The figure below shows the transformed BST. The solid line
#                indicates the successor relationship, while the dashed line means the
#                predecessor relationship.
# 
# Example 2:
#   Input: root = [2,1,3]
#   Output: [1,2,3]
# 
# Constraints:
# - The number of nodes in the tree is in the range [0, 2000].
# - 1000 <= Node.val <= 1000
# - All the values of the tree are unique.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(h)
    def TreeToLinearDoublyLinkedList(self, root, first=None, last=None):
        if not root:
            return first, last
        
        # Process left subtree
        first, last = self.TreeToLinearDoublyLinkedList(root.left, first, last)

        # Process current node
        if last:
            last.right = root
            root.left = last
        else:
            first = root

        last = root

        # Process right subtree
        first, last = self.TreeToLinearDoublyLinkedList(root.right, first, last)

        return first, last

    # Time complexity: O(n)
    # Space complexity: O(h)
    def TreeToCircularDoublyLinkedList(self, root):
        if not root:
            return None
        
        # Transform the tree into a linear doubly-linked list and connect its head to its tail
        first, last = self.TreeToLinearDoublyLinkedList(root)
        first.left = last
        last.right = first

        # Return the head of the circular DLL
        return first

    def PythonListToTree(self, values, index=0):
        if not values:
            return None

        if index >= len(values):
            raise Exception('Index out of range')
        
        root = Node(values[index])

        leftIndex = 2 * index + 1
        rightIndex = 2 * index + 2

        if leftIndex < len(values):
            root.left = self.PythonListToTree(values, leftIndex)

        if rightIndex < len(values):
            root.right = self.PythonListToTree(values, rightIndex)

        return root

    def DoublyLinkedListToPythonList(self, root):
        if not root:
            return []

        pythonList = [root.val]
        node = root.right
        while node != root:
            pythonList.append(node.val)
            node = node.right
        
        return pythonList
    
    def treeToDoublyList(self, root):
        return self.TreeToCircularDoublyLinkedList(root)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root = solution.PythonListToTree([4,2,5,1,3])
    expectedOutput = [1,2,3,4,5]
    output = solution.DoublyLinkedListToPythonList(solution.TreeToCircularDoublyLinkedList(root))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 2
    root = solution.PythonListToTree([2,1,3])
    expectedOutput = [1,2,3]
    output = solution.DoublyLinkedListToPythonList(solution.TreeToCircularDoublyLinkedList(root))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()