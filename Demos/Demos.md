# Chapter 01: Quicksort
```python
def Partition(nums, low, high):
    pivot = nums[high]
    index = low - 1

    for i in range(low, high):
        if nums[i] <= pivot:
            index += 1
            nums[index], nums[i] = nums[i], nums[index]

    index += 1
    nums[index], nums[high] = nums[high], nums[index]

    return index

def Quicksort(nums, low=None, high=None):
    if low == None and high == None:
        low = 0
        high = len(nums) - 1

    if low < high:
        index = Partition(nums, low, high)
        Quicksort(nums, low, index - 1)
        Quicksort(nums, index + 1, high)

if __name__ == "__main__":
    nums = [1, 5, 4, 2, 7, 3, 10, 8, 9, 6]
    Quicksort(nums)
    print(nums)
```
# Chapter 02: Cyclic sort
```python
def CyclicSort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
            continue
        i += 1

if __name__ == "__main__":
    nums = [2, 1, 4, 5, 3]
    print(nums)

    CyclicSort(nums)
    print(nums)
```
# Chapter 03: Binary search
```python
def BinarySearch(nums, value):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == value:
            return mid
        
        if nums[mid] < value:
            left = mid + 1

        else: # nums[mid] > value
            right = mid - 1
    
    return -1

if __name__ == "__main__":
    nums = [1, 3, 5, 9, 11, 24, 36]
    target = 11
    expectedOutput = 4
    output = BinarySearch(nums, target)
    print(output, expectedOutput, output == expectedOutput)
```
# Chapter 04: Reverse list
```python
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
    head = prevNode
    return head

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
```
# Chapter 05: Top K emelents
```python
from heapq import *

def TopKElements(nums, k):
    if k > len(nums):
        return None

    maxHeap = [-num for num in nums]
    heapify(maxHeap)

    return [-heappop(maxHeap) for i in range(k)]

if __name__ == "__main__":
    nums = [1, 5, 4, 2, 7, 3, 10, 8, 9, 6]
    k = 4
    expectedOutput = [10, 9, 8, 7]
    output = TopKElements(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
```
# Chapter 06: Fast and slow (cycle in linked list)
```python
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

```
# Chapter 07: Fast and slow (middle of linked list)
```python
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
```
# Chapter 08: DFS
```python
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def DFS(head, visited):
    if not head:
        return
    
    # Add node to visited list
    visited.append(head.val)
    
    # Recursively call dfs on neighbor subtrees
    DFS(head.left, visited)
    DFS(head.right, visited)

def DFSIterative(head):
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

if __name__ == "__main__":
    tree = TreeNode(1)

    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = [1, 2, 4, 5, 3, 6, 7]
   
    print("DFS recursive")
    output = []
    DFS(tree, output)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    print("DFS iterative")
    output = DFSIterative(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
```
# Chapter 09: BFS
```python
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def BFS(head, visited, pending=[]):
    if not head:
        return
    
    # Add node to visited list
    visited.append(head.val)

    # Add neighbor nodes to pending queue
    pending.append(head.left)
    pending.append(head.right)
    
    # Recursively call bfs if there are pending nodes
    if pending:
        BFS(pending.pop(0), visited, pending)

def BFSIterative(head):
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

if __name__ == "__main__":
    tree = TreeNode(1)

    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    expectedOutput = [1, 2, 3, 4, 5, 6, 7]
   
    print("BFS recursive")
    output = []
    BFS(tree, output)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    print("BFS iterative")
    output = BFSIterative(tree)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
```
# Chapter 10: All subsets
```python
def AllSubsets(nums):
    subsets = [[]]
    
    for num in nums:
        n = len(subsets)

        for i in range(n):
            subset = subsets[i] + [num]
            subsets.append(subset)
    
    subsets.sort(key=lambda x: len(x)) # Optional
    
    return subsets


if __name__ == "__main__":
    nums = [1, 2, 3]
    expectedOutput = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    output = AllSubsets(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
```
# Chapter 11: All permutations
```python
def AllPermutations(nums):
    prevPermutations = [[]]
    allPermutations = []

    for num in nums:
        allPermutations = []
        for permutation in prevPermutations:
            for i in range(len(permutation) + 1):
                newPerm = permutation.copy()
                newPerm.insert(i, num)
                allPermutations.append(newPerm)
        
        prevPermutations = allPermutations

    allPermutations.sort()
    return allPermutations

if __name__ == "__main__":
    nums = [1,3,5]
    expectedOutput = [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]]
    output = AllPermutations(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
```
# Chapter 12: Merge intervals
```python
def MergeIntervals(intervals):
    mergedIntervals = []
    intervals.sort()

    for interval in intervals:
        if not mergedIntervals or not IsOverlap(mergedIntervals[-1], interval):
            mergedIntervals.append(interval)
        else:
            mergedIntervals[-1] = Merge(mergedIntervals[-1], interval)
    
    return mergedIntervals

def Merge(intervalA, intervalB):
    start = min(intervalA[0], intervalB[0])
    end =   max(intervalA[1], intervalB[1])
    return [start, end]

def IsOverlap(intervalA, intervalB):
    return not (intervalA[1] < intervalB[0] or intervalB[1] < intervalA[0])

if __name__ == "__main__":
    intervals = [[1,4], [2,5], [7,9]]
    expectedOutput = [[1,5], [7,9]]
    output = MergeIntervals(intervals)
    print(intervals)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
```
# Chapter 13: Dynamic programming
```python
# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
#
# Time complexity: O(n * s)
# Space complexity: O(n * s)
def TotalNumberOfSubsetsWithSumS(nums, s):
    rows = len(nums)
    cols = s + 1

    # Initialize the dynamic programming table (dp)
    dp = [[0 for col in range(cols)] for row in range(rows)]

    # Base case: Mark the fist colum as every set has an empty set that adds up to zero.
    for row in range(rows):
        dp[row][0] = 1

    # Base case: A set containing only the first element from nums can add up to the value
    #            of the first element of nums, mark its corresponding colum.
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

if __name__ == "__main__":
    # Example 1
    nums = [1, 1, 2, 3]
    s = 4
    expectedOutput = 3 # The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
                       # Note that we have two similar sets {1, 3}, because we have two '1' in our
                       # input.
    output = TotalNumberOfSubsetsWithSumS(nums, s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 2, 7, 1, 5] 
    s = 9
    expectedOutput = 3 # The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
    output = TotalNumberOfSubsetsWithSumS(nums, s)
    print(output, expectedOutput, output == expectedOutput)
```
# Chapter 14: Backtracking
```python
def PlaceNQueens(board, queens):
    if queens == 0:
        return True
    
    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        for col in range(cols):
            if IsValid(board, row, col):
                board[row][col] = 1
                
                if PlaceNQueens(board, queens - 1):
                    return True

                board[row][col] = 0 # backtrack
    
    return False

def IsValid(board, targetRow, targetCol):
    rows = len(board)
    cols = len(board[0])

    # Check cell
    if board[targetRow][targetCol]:
        return False
    
    # Check row
    for row in range(rows):
        if board[row][targetCol]:
            return False

    # Check col
    for col in range(cols):
        if board[targetRow][col]:
            return False

    # Check top left diagonal
    row = targetRow
    col = targetCol
    while row >= 0 and col >= 0:
        if board[row][col]:
            return False
        row -= 1
        col -= 1

    # Check top right diagonal
    row = targetRow
    col = targetCol
    while row >= 0 and col < cols:
        if board[row][col]:
            return False
        row -= 1
        col += 1

    # Check bottom left diagonal
    row = targetRow
    col = targetCol
    while row < rows and col >= 0:
        if board[row][col]:
            return False
        row += 1
        col -= 1

    # Check bottom right diagonal
    row = targetRow
    col = targetCol
    while row < rows and col < cols:
        if board[row][col]:
            return False
        row += 1
        col += 1

    return True

def PrintBoard(board):
    for row in board:
        print(row)

def MakeBoard(n, m):
    return [[0 for col in range(m)] for row in range(n)]

if __name__ == "__main__":
    n = 8 # Number of queens and board size (n x n)
    board = MakeBoard(n, n)
    if PlaceNQueens(board, n):
        PrintBoard(board)
    else:
        print("No solution found")
```
# Chapter 15: Topological sort
```python
def TopologicalSort(vertices, edges):
    graph = BuildGraph(vertices, edges)
    inDegree = BuildInDegreeTracker(graph)

    # Find initial sources (nodes with no incoming edges)
    sources = []
    for v in inDegree:
        if inDegree[v] == 0:
            sources.append(v)

    sortedVertices = []
    while sources:
        v = sources.pop(0)
        sortedVertices.append(v)

        # For each vertex u, children of v, decrease the inDegree value of u by one.
        # If the inDegree value of u has reached zero, add u to the sources list
        for u in graph[v]:
            inDegree[u] -= 1
            if inDegree[u] == 0:
                sources.append(u)

    # Return an empty list if the graph is not acyclical
    if len(sortedVertices) != vertices:
        return []

    # Otherwise, return sorted vertices
    return sortedVertices


def BuildGraph(vertices, edges):
    graph = {i: [] for i in range(vertices)}
    for e in edges:
        v, u = e
        graph[v].append(u)
    return graph

def BuildInDegreeTracker(graph):
    inDegree = {i: 0 for i in graph}
    for v in graph:
        for u in graph[v]:
            inDegree[u] += 1
    return inDegree

if __name__ == "__main__":
    # Example 1
    vertices = 4
    edges = [[3, 2], [3, 0], [2, 0], [2, 1]]
    expectedOutput = [3, 2, 0, 1]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 2
    vertices = 3
    edges = [[1, 0], [2, 1]]
    expectedOutput = [2, 1, 0]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 3
    vertices = 4
    edges = [[0, 1], [1, 2], [2, 3]]
    expectedOutput = [0, 1, 2, 3]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 4
    vertices = 3
    edges = [[0, 2], [1, 2], [1, 0]]
    expectedOutput = [1, 0, 2]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 5
    vertices = 1
    edges = []
    expectedOutput = [0]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 6
    vertices = 2
    edges = [[0, 1]]
    expectedOutput = [0, 1]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 7
    vertices = 2
    edges = [[1, 0]]
    expectedOutput = [1, 0]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()

    # Example 8
    vertices = 3
    edges = [[0, 1], [0, 2], [1, 2]]
    expectedOutput = [0, 1, 2]
    output = TopologicalSort(vertices, edges)
    print(output)
    print(output == expectedOutput)
    print()
```
