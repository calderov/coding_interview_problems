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


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, val):
        node = Node(val)

        if not self.head:
            node.left = node
            node.right = node
            self.head = node
            self.tail = node
            return
        
        node.left = self.tail
        node.right = self.head
        
        self.tail.right = node
        self.head.left = node

        self.tail = node

    def toPythonList(self):
        if not self.head:
            return []
        
        values = [self.head.val]
        node = self.head.right

        while node != self.head:
            values.append(node.val)
            node = node.right

        return values

def treeToDoubleLinkedList(root, doubleLinkedList=None):
    if not doubleLinkedList:
        doubleLinkedList = DoubleLinkedList()
    
    if root:
        treeToDoubleLinkedList(root.left, doubleLinkedList)
        doubleLinkedList.append(root.val)
        treeToDoubleLinkedList(root.right, doubleLinkedList)

    return doubleLinkedList

def pythonListToTree(values, index=0):
    if not values or index < 0 or index >= len(values) or values[index] == None:
        return None
    
    node = Node(values[index])
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2

    node.left = pythonListToTree(values, leftIndex)
    node.right = pythonListToTree(values, rightIndex)

    return node

if __name__ == "__main__":
    # Example 1
    root = pythonListToTree([4,2,5,1,3])
    expectedOutput = [1,2,3,4,5]
    output = treeToDoubleLinkedList(root).toPythonList()
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 2
    root = pythonListToTree([2,1,3])
    expectedOutput = [1,2,3]
    output = treeToDoubleLinkedList(root).toPythonList()
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()