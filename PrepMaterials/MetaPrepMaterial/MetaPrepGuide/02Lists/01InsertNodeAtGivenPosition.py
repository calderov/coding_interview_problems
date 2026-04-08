# Insert a node at a specific position in a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def toPythonList(head):
    nums = []
    node = head

    while node:
        nums.append(node.val)
        node = node.next
    
    return nums

def toLinkedList(nums):
    head = None
    tail = None

    for val in nums:
        if tail == None:
            head = Node(val)
            tail = head
        else:
            node = Node(val)
            tail.next = node
            tail = node
    
    return head

# Time complexity: O(n)
# Space complexity: O(1)
def insertNodeAtPosition(head, val, position):
    if position == 0:
        newNode = Node(val)
        newNode.next = head
        return newNode

    if not head or position < 0:
        return head

    prevNode = head
    for i in range(1, position):
        if prevNode:
            prevNode = prevNode.next
    
    if prevNode:
        newNode = Node(val)
        newNode.next = prevNode.next
        prevNode.next = newNode

    return head

if __name__=="__main__":
    # Example 1
    inputList = [1,2,3,4,5]
    item = 6
    position = 0
    expected = [6,1,2,3,4,5]
    
    linkedList = toLinkedList(inputList)
    linkedList = insertNodeAtPosition(linkedList, item, position)
    output = toPythonList(linkedList)

    print(expected)
    print(output)
    print(output == expected)
    print()

    # Example 2
    inputList = [1,2,3,4,5]
    item = 6
    position = 2
    expected = [1,2,6,3,4,5]
    
    linkedList = toLinkedList(inputList)
    linkedList = insertNodeAtPosition(linkedList, item, position)
    output = toPythonList(linkedList)

    print(expected)
    print(output)
    print(output == expected)
    print()

    # Example 3
    inputList = [1,2,3,4,5]
    item = 6
    position = 5
    expected = [1,2,3,4,5,6]
    
    linkedList = toLinkedList(inputList)
    linkedList = insertNodeAtPosition(linkedList, item, position)
    output = toPythonList(linkedList)

    print(expected)
    print(output)
    print(output == expected)
    print()