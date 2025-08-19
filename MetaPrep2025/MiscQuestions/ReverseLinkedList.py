class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseLinkedList(head):
    if not head:
        return head

    node = head
    prevNode = None
    nextNode = None

    while node:
        nextNode = node.next
        node.next = prevNode
        prevNode = node
        node = nextNode

    return prevNode

def linkedListToPythonList(head):
    values = []

    node = head
    while node:
        values.append(node.val)
        node = node.next

    return values

def pythonListToLinkedList(values):
    head = None
    tail = None

    for val in values:
        node = Node(val)

        if not head:
            head = node
            tail = head
            continue

        tail.next = node
        tail = node
    
    return head

if __name__ == "__main__":
    values   = [1,2,3,4,5,6]
    expected = [6,5,4,3,2,1]
    
    head = pythonListToLinkedList(values)
    output = linkedListToPythonList(reverseLinkedList(head))

    print(values)
    print(expected)
    print(output)
    print(output == expected)