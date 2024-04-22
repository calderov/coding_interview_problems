# 19. Remove Nth Node From End of List (Medium)
# Given the head of a linked list, remove the nth node from the end of the
# list and return its head.
# 
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# Example 2:
# Input: head = [1], n = 1
# Output: []
# 
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#  
# Constraints:
# - 1 <= nodes_in_list <= 30
# - 0 <= Node.val <= 100
# - 1 <= n <= sz

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def removeNthFromEnd(self, head, n):
        # Find list length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # If the list is less than n nodes long
        # return the head by definition
        if length < n:
            return head

        # If the list is n nodes long, then the head of the list is ought to
        # be removed
        if length == n:
            head = head.next
            return head

        # Otherwise, an inner node of the list is ought to be removed
        node = head
        for i in range(length - n - 1):
            node = node.next
        node.next = node.next.next

        return head         

def pythonListToLinkedList(pythonList):
    head = None
    tail = None

    for value in pythonList:
        node = Node(value)

        if head == None:
            head = node
            tail = node
            continue

        tail.next = node
        tail = node

    return head

def linkedListToPythonList(linkedList):
    pythonList = []

    node = linkedList
    while node:
        pythonList.append(node.val)
        node = node.next
    
    return pythonList

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    n = 2
    head = [1,2,3,4,5]
    expectedOutput = [1,2,3,5]
    output = linkedListToPythonList(solution.removeNthFromEnd(pythonListToLinkedList(head), n))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 2:
    n = 1
    head = [1]
    expectedOutput = []
    output = linkedListToPythonList(solution.removeNthFromEnd(pythonListToLinkedList(head), n))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
     
    # Example 3:
    n = 1
    head = [1,2]
    expectedOutput = [1]
    output = linkedListToPythonList(solution.removeNthFromEnd(pythonListToLinkedList(head), n))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()