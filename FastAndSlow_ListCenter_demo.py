class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

# Given the head of a LinkedList, returns the node at the middle of the list
def GetListCenter(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    # Insert elements
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    expectedOutput = 4
    output = GetListCenter(head).val

    print(output, expectedOutput, output == expectedOutput)
