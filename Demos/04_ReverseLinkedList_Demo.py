class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

def ReverseLinkedList(head):
    node = head
    prevNode = None
    nextNode = None

    while node:
        nextNode = node.next
        node.next = prevNode
        prevNode = node
        node = nextNode

    return prevNode

def PythonListToLinkedList(pythonList):
    head = None
    tail = None

    for value in pythonList:
        node = Node(value)

        if head == None:
            head = node
            tail = head
            continue

        tail.next = node
        tail = node

    return head

def LinkedListToPythonList(head):
    pythonList = []
    while head:
        pythonList.append(head.val)
        head = head.next
    return pythonList

if __name__ == "__main__":
    nums = [i for i in range(10)]

    linkedList = PythonListToLinkedList(nums)
    print(LinkedListToPythonList(linkedList))

    linkedList = ReverseLinkedList(linkedList)
    print(LinkedListToPythonList(linkedList))
