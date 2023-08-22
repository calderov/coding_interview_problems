# Useful code snippets

## Linked lists
### Barebones linked list
```python
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
```

### Find the center of a liked list
```python
def GetListCenter(self, head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### Reverse a linked list
```python
def Reverse(self, head):
    prevNode = None
    while head is not None:
        nextNode = head.next
        head.next = prevNode
        prevNode = head
        head = nextNode
    return prevNode
```