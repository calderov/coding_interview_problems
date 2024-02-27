# Given a linked list and target value, remove all instances of such value from the linked list

class Node:
    def __init__(self, value):
        self.val = value
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

def LinkedListToPythonList(node):
    node = node
    pythonList = []

    while node:
        pythonList.append(node.val)
        node = node.next

    return pythonList

# Time complexity: O(n)
# Space complexity: O(1)
def RemoveValueFromLinkedList(head, value):
    node = head
    prevNode = None

    while node:
        if node.val == value:
            if node == head:
                head = head.next
                node = head
                prevNode = None
                continue

            if node.next:
                prevNode.next = node.next
                node = node.next.next
            else:
                prevNode.next = node.next
                break


        prevNode = node
        node = node.next

    return head


if __name__ == "__main__":
    # Example 1
    value = 2
    inputList = [1, 2, 3, 4, 2, 5, 6, 7]
    expectedOutput = [1, 3, 4, 5, 6, 7]
    output = LinkedListToPythonList(RemoveValueFromLinkedList(PythonListToLinkedList(inputList), value))
    print(inputList, value)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    value = 1
    inputList = [1, 1, 2, 3, 4]
    expectedOutput = [2, 3, 4]
    output = LinkedListToPythonList(RemoveValueFromLinkedList(PythonListToLinkedList(inputList), value))
    print(inputList, value)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    value = 3
    inputList = [0, 1, 2, 3]
    expectedOutput = [0, 1, 2]
    output = LinkedListToPythonList(RemoveValueFromLinkedList(PythonListToLinkedList(inputList), value))
    print(inputList, value)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 4
    value = 1
    inputList = [1, 1, 1, 1]
    expectedOutput = []
    output = LinkedListToPythonList(RemoveValueFromLinkedList(PythonListToLinkedList(inputList), value))
    print(inputList, value)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()