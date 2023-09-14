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

### Python list to linked list
```python
def ToLinkedList(nums):
    head = None
    tail = None

    for i in range(len(nums)):
        node = Node(nums[i])

        if head == None:
            head = node
            tail = head

        else:
            tail.next = node
            tail = node
        
    return head
```

### Linked list to Python list
```python
def ToPythonList(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums
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
def Reverse(head):
    node = head
    prevNode = None
    nextNode = None
    
    while node:
        nextNode = node.next
        node.next = prevNode
        prevNode = node
        node = nextNode
    
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

## Cyclic Sort
### Cyclic sort example
```python
# Given an array of n numbers in the range 1 to n (inclusive) sorts the array
# in linear time. If the array contains duplicates and by extension is missing
# items from the range, this algorithm places the duplicates in the places that
# would correspond to the missing numbers.
#
# Time complexity: O(n)
# Space complexity: O(1)
def CyclicSort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
            continue
        i += 1
```