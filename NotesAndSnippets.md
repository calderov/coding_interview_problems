# Useful code snippets

## Two pointer patterns 
PENDING

## Searches and traversals

### Depth-First Search (iterative)
```python
def dfs(graph, start):
    visited = set()
    pending = [start] # Stack

    while pending:
        node = pending.pop()
        print(node)
        pending += filter(lambda x: x not in visited, reversed([neighbor for neighbor in graph[node]]))
```

### Breadth-First Search (iterative)
```python
def bfs_iterative(graph, start):
    visited = set()
    pending = [start] # Queue

    while pending:
        node = pending.pop(0)
        print(node)
        pending += filter(lambda x: x not in visited, [neighbor for neighbor in graph[node]])
```

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

### Compare linked lists
```python
def AreListsEqual(list1, list2):
    while list1 is not None and list2 is not None:
        if list1.val != list2.val:
            return False
        list1 = list1.next
        list2 = list2.next

    if list1 is not None or list2 is not None:
        return False

    return True
```

## Sliding Window

### Sliding window example
```python
# Given an array of positive numbers and a positive number 'k,' find
# the maximum sum of any contiguous subarray of size 'k'.
def FindMaxSumSubarray(nums, k):
    start = 0
    end = k - 1
    windowSum = 0
    maxWindowSum = 0
    
    while end < len(nums):
        if start == 0:
            windowSum = sum(nums[0 : k])
            maxWindowSum = windowSum
        else:
            windowSum -= nums[start - 1]
            windowSum += nums[end]
        
        if windowSum > maxWindowSum:
            maxWindowSum = windowSum

        start += 1
        end += 1

    return maxWindowSum
```

## Merge intervals

### Check if two intervals overlap
```python
# Use this when you want [1, 2], [2, 3] to be considered disjoint
def IsOverlap(intervalA, intervalB):
    return intervalA.start < intervalB.end and intervalA.end > intervalB.start

# Use this when you want [1, 2], [2, 3] to be considered overlapping
def IsOverlap(self, intervalA, intervalB):
    return not (intervalA.end < intervalB.start or intervalB.end < intervalA.start)
```

