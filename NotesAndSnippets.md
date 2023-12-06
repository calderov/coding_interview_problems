# Useful code snippets

# Searches and Traversals
Searching for values is a common operation on graphs, trees and matrices. There are well known algorithms to traverse these data structures which can be easily modified to accomplish search. 

## Breadth First Search (BFS) and Depth First Search (DFS)
BFS and DFS are two traversal algorithms. For a given graph, matrix or tree, BFS will explore the data structure level by level, starting with the closest neighbors from a starting point. DFS on the other hand will try to explore neighbors in a given direction until it can not go further.

The implementations of both algorithms are quite simmilar, their main difference is their underliying data structure. DFS uses a stack to keep track of pending states and BFS uses a queue.
Lets study how DFS and BFS traverse a binary tree implemented as follows:  

### Depth-First Search
```python
def dfs(head, visited):
    if not head:
        return
    
    # Add node to visited list
    visited.append(head.val)
    
    # Recursively call dfs on neighbor subtrees
    dfs(head.left, visited)
    dfs(head.right, visited)

def dfs_iterative(head):
    visited = []
    pending = [head] # Stack

    # While there are nodes in the pending stack
    while pending:
        # Fetch node from pending stack
        node = pending.pop()

        # Add node to visited list
        visited.append(node.val)

        # Add neighbors to pending stack
        if node.right: pending.append(node.right)
        if node.left: pending.append(node.left)

    return visited
```

### Breadth-First Search
```python

def bfs(head, visited, pending=[]):
    if not head:
        return
    
    # Add node to visited list
    visited.append(head.val)

    # Add neighbor nodes to pending queue
    pending.append(head.left)
    pending.append(head.right)
    
    # Recursively call bfs if there are pending nodes
    if pending:
        bfs(pending.pop(0), visited, pending)

def bfs_iterative(head):
    visited = []
    pending = [head] # Queue

    # While there are nodes in the pending queue
    while pending:
        # Fetch node from pending queue
        node = pending.pop(0)

        # Add node to visited list
        visited.append(node.val)

        # Add neighbors to pending queue
        if node.left: pending.append(node.left)
        if node.right: pending.append(node.right)

    return visited
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

    for num in nums:
        node = Node(num)

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

## Binary search
### Binary search example (assuming input array is sorted in ascending order)
```python
def BinarySearch(nums, key):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == key:
            return mid
        
        if nums[mid] < key:
            left = mid + 1

        else: # nums[mid] > key
            right = mid - 1
    
    return -1
```

## Bitwise XOR
## XOR truth table
| A | B | A xor B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

## Dynamic programming
Dynamic Programming (DP) is defined as a technique that solves some particular type of problems in Polynomial Time. Dynamic Programming solutions are faster than the exponential brute method and can be easily proved their correctness.

There are two approaches to formulate a dynamic programming solution:

1. Top-Down Approach:  This approach follows the memoization technique. It consists of recursion and caching. In computation, recursion represents the process of calling functions repeatedly, whereas cache refers to the process of storing intermediate results.

2. Bottom-Up Approach: This approach uses the tabulation technique to implement the dynamic programming solution. It addresses the same problems as before, but without recursion. In this approach, iteration replaces recursion. Hence, there is no stack overflow error or overhead of recursive procedures.

```python
# Example of Dynamic Programming with tabulation to compute factorials
class Factorial:
    def __init__(self):
        self.cache = [1, 1]
    
    def get(self, n):
        if n < len(self.cache):
            return self.cache[n]
        
        i = len(self.cache)
        while i < n + 1:
            self.cache.append(i * self.cache[i - 1])
            i += 1

        return self.cache[n]
```

Here es a complete example of a 0/1 knapsack problem, solved with dynamic programming

```python
# Problem:
# Given a set of positive numbers, find the total number of subsets whose sum
# is equal to a given number ‘S’.

# Solution:
# Use dynamic programming to set a table dp, where dp[i][j] keeps the number of
# subsets of the first i elements of the input, that add up to the value j which
# ranges from 0 to S. Build this table iteratively based on whether an element is
# included in a subset or not.
#
# Once the table is populated, return the value stored in the last cell of the
# table, as it contains how many subsets add to S.
#
# Solution complexity:
# Time complexity: O(n * s)
# Space complexity: O(n * s)
def TotalNumberOfSubsetsWithSumS(self, nums, s):
    rows = len(nums)
    cols = s + 1

    # Initialize the dynamic programming table (dp)
    dp = [[0 for col in range(cols)] for row in range(rows)]

    # Base case: Mark the fist colum as the every set has an empty set 
    #            that adds up to zero.
    for row in range(rows):
        dp[row][0] = 1

    # Base case: A set containing only the first element from nums
    #            can add up to the value of the first element of nums,
    #            mark its corresponding colum.
    if nums[0] < cols:
        dp[0][nums[0]] = 1

    # For each cell on the dynamic programming table
    for row in range(1, rows):
        for col in range(1, cols):
            element = nums[row]

            # Case 1: Exclude the current element
            dp[row][col] += dp[row - 1][col]
            
            # Case 2: Include the current element
            if col >= element:
                dp[row][col] += dp[row - 1][col - element]
    
    # The amount of subsets that add up to S is located
    # in the last cell of the dynamic programming table
    return dp[-1][-1]
```