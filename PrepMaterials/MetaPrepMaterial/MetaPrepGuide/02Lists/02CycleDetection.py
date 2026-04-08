# Cycle Detection
# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def isCycle(head):
    if not head:
        return False

    slow = head
    fast = head.next

    while fast.next and fast.next.next:
        if slow == fast:
            return True
        
        slow = slow.next
        fast = fast.next.next

    return False

if __name__ == "__main__":
    # Base case
    linkedList = Node(1)
    linkedList.next = Node(2)
    linkedList.next.next = Node(3)
    linkedList.next.next.next = Node(4)

    # Example 1 (No cycle)
    expected = False
    output = isCycle(linkedList)
    print(output == expected)

    print()

    # Example 2 (Cycle)
    linkedList.next.next.next.next = linkedList
    expected = True
    output = isCycle(linkedList)
    print(output == expected)



