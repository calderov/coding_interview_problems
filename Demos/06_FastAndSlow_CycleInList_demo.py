class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

# Given the head of a LinkedList, returns True if ithas a cycle and False if not.
def HasCycle(head):
    fast = head
    slow = head

    while True:
        if fast == None or fast.next == None or fast.next.next == None:
            return False

        fast = fast.next.next
        slow = slow.next

        if fast.val == slow.val:
            return True

if __name__ == "__main__":
    # Insert elements
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Insert loop
    head.next.next.next.next.next.next = head.next.next # Point tail to the 3rd node
    
    expectedOutput = True
    output = HasCycle(head)

    print(output, expectedOutput, output == expectedOutput)

