# Remove Duplicates from Sorted List II
# MEDIUM
# https://scaleengineer.com/dsa/problems/remove-duplicates-from-sorted-list-ii

# Description
# Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# Return the linked list sorted as well.

# Example 1:
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Example 2:
# Input: head = [1,1,1,2,3]
# Output: [2,3]

# Constraints:
#     The number of nodes in the list is in the range [0, 300].
#     -100 <= Node.val <= 100
#     The list is guaranteed to be sorted in ascending order.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def ToPythonList(head):
    pythonList = []
    node = head

    while node:
        pythonList.append(node.val)
        node = node.next

    return pythonList

def ToLinkedList(pythonList):
    head = None
    tail = None

    for val in pythonList:
        node = Node(val)

        if not head:
            head = node
            tail = node
            continue

        tail.next = node
        tail = node

    return head

# Time: O(n)
# Space: O(1)
def RemoveDuplicatesV1(head):
    # Mark duplicate nodes
    mark = float("inf")
    dupe = None
    
    node = head
    while node:
        if node.next and node.val == node.next.val:
            dupe = node.val
        
        if node.val == dupe:
            node.val = mark

        node = node.next

    # Move head to first non marked node
    node = head
    head = None

    while node:
        if node.val != mark:
            head = node
            break
        node = node.next

    # Remove remaining marked nodes
    node = head
    prevNode = None

    while node:
        while node.val == mark:
            prevNode.next = node.next
            node = node.next
        
        prevNode = node
        node = node.next

    return head

# Time: O(n)
# Space: O(1)
def RemoveDuplicatesV2(head):
    sentinel = Node(0)
    sentinel.next = head

    node = head
    prevNode = sentinel

    while node:
        if node.next and node.val == node.next.val:
            while node.next and node.val == node.next.val:
                node = node.next
            prevNode.next = node.next
            node = node.next
            continue

        prevNode = prevNode.next
        node = node.next
    
    return sentinel.next

def RemoveDuplicates(head):
    return RemoveDuplicatesV2(head)

if __name__ == "__main__":
    # Example 1:
    head = [1,2,3,3,4,4,5]
    expected = [1,2,5]
    output = ToPythonList(RemoveDuplicates(ToLinkedList(head)))
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    head = [1,1,1,2,3]
    expected = [2,3]
    output = ToPythonList(RemoveDuplicates(ToLinkedList(head)))
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    head = [1,1,1,2,3,3,3,4]
    expected = [2,4]
    output = ToPythonList(RemoveDuplicates(ToLinkedList(head)))
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4:
    head = [1,1,1,1]
    expected = []
    output = ToPythonList(RemoveDuplicates(ToLinkedList(head)))
    print(expected)
    print(output)
    print(expected == output)
    print()