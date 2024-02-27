# Given a linked list remove all the nodes containing a target value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def PythonListToLinkedList(pythonList):
    head = None
    tail = None

    for item in pythonList:
        node = Node(item)

        if not head:
            head = node
            tail = node
            continue

        tail.next = node
        tail = node

    return head

def LinkedListToPythonList(head):
    pythonList = []
    node = head

    while node:
        pythonList.append(node.value)
        node = node.next

    return pythonList

def RemoveNodesWithValue(head, target):
    # Search target at the head and move the it forward if needed
    while head and head.value == target:
        head = head.next

    # If the head reached the end of the list, return None
    if not head:
        return None
    
    # Traverse the list from the start skipping those nodes that match the intended target (and thus removing them)
    node = head
    while node.next:
        if node.next.value == target:
            node.next = node.next.next
        else:
            node = node.next
    
    # Return the head of the list
    return head

if __name__ == "__main__":
    # Example 1
    nums = [1, 2, 3, 4, 2, 5, 6]
    target = 2
    expectedOutput = [1, 3, 4, 5, 6]
    output = LinkedListToPythonList(RemoveNodesWithValue(PythonListToLinkedList(nums), target))
    print(nums, target)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [1, 1, 1, 2, 3, 4]
    target = 1
    expectedOutput = [2, 3, 4]
    output = LinkedListToPythonList(RemoveNodesWithValue(PythonListToLinkedList(nums), target))
    print(nums, target)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    nums = [1, 2, 3, 4, 4, 4, 4]
    target = 4
    expectedOutput = [1, 2, 3]
    output = LinkedListToPythonList(RemoveNodesWithValue(PythonListToLinkedList(nums), target))
    print(nums, target)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 4
    nums = [1, 1, 1, 1, 1]
    target = 1
    expectedOutput = []
    output = LinkedListToPythonList(RemoveNodesWithValue(PythonListToLinkedList(nums), target))
    print(nums, target)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 5
    nums = [0, 1, 1, 1, 1]
    target = 1
    expectedOutput = [0]
    output = LinkedListToPythonList(RemoveNodesWithValue(PythonListToLinkedList(nums), target))
    print(nums, target)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()