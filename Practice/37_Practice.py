# 138. Copy List with Random Pointer (Medium)
# A linked list of length n is given such that each node contains an
# additional random pointer, which could point to any node in the list, or
# null.
# 
# Construct a deep copy of the list. The deep copy should consist of exactly
# n brand new nodes, where each new node has its value set to the value of
# its corresponding original node. Both the next and random pointer of the
# new nodes should point to new nodes in the copied list such that the
# pointers in the original list and copied list represent the same list
# state. None of the pointers in the new list should point to nodes in the
# original list.
# 
# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.
# 
# Return the head of the copied linked list.
# 
# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:
# 
# - val: an integer representing Node.val
# - random_index: the index of the node (range from 0 to n-1) that the random
#   pointer points to, or null if it does not point to any node.
# 
# Your code will only be given the head of the original linked list.
#  
# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
#  
# 
# Constraints:
# - 0 <= n <= 1000
# - -104 <= Node.val <= 104
# - Node.random is null or is pointing to some node in the linked list.


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        # Keep a map of original and copied nodes to their respective counterpart
        nodeMap = {None: None}
        headCopy = None

        # Populate node map and determine head copy
        node = head
        while node:
            nodeCopy = Node(node.val)
            nodeMap[node] = nodeCopy
            nodeMap[nodeCopy] = node

            if not headCopy:
                headCopy = nodeCopy

            node = node.next

        # Connect copied nodes
        node = head
        while node:
            nodeCopy = nodeMap[node]
            nodeCopy.next = nodeMap[node.next]
            nodeCopy.random = nodeMap[node.random]
            node = node.next
        
        return headCopy
       

def pythonListToLinkedList(pythonList):
    nodes = [None] * len(pythonList)
    head = None

    for i in range(len(pythonList)):
        value, _ = pythonList[i]
        node = Node(value)
        nodes[i] = node
        
        if not head:
            head = node

        if i > 0:
            nodes[i - 1].next = nodes[i]

    for i in range(len(pythonList)):
        _, randomIndex = pythonList[i]
        nodes[i].random = nodes[randomIndex] if randomIndex != None else None

    return head

def linkedListToPythonList(linkedList):
    nodeIndex = {None: None}

    i = 0
    node = linkedList
    while node:
        nodeIndex[node] = i
        node = node.next   
        i += 1

    pythonList = []
    n = i

    node = linkedList
    while node:
        value = node.val
        randomIndex = nodeIndex[node.random]
        pythonList.append([value, randomIndex])
        node = node.next

    return pythonList

if __name__=="__main__":
    solution = Solution()

    # Example 1
    originalInput =  [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    expectedOutput = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    output = linkedListToPythonList(solution.copyRandomList(pythonListToLinkedList(originalInput)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2:
    originalInput = [[1, 1], [2, 1]]
    expectedOutput = [[1, 1], [2, 1]]
    output = linkedListToPythonList(solution.copyRandomList(pythonListToLinkedList(originalInput)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3:
    originalInput = [[3, None], [3, 0], [3, None]]
    expectedOutput = [[3, None], [3, 0], [3, None]]
    output = linkedListToPythonList(solution.copyRandomList(pythonListToLinkedList(originalInput)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()