# Reverse a LinkedList (easy)
# Problem Statement
# 
# Given the head of a Singly LinkedList, reverse the LinkedList. Write a
# function to return the new head of the reversed LinkedList.
#
# Example:
#
#   Input: 
#
#     head -> 2 -> 4 -> 6 -> 8 -> 10 -> null
#
#   Output:
#
#     null <- 2 <- 4 <- 6 <- 8 <- 10 <- head

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

def ToPythonList(head):
    nums = []
    
    while head:
        nums.append(head.val)
        head = head.next

    return nums

def ToLinkedList(nums):
    head = None
    tail = None

    for val in nums:
        if tail == None:
            tail = Node(val)
            head = tail
        else:
            node = Node(val)
            tail.next = node
            tail = node
        
    return head

class Solution:
    # Solution:
    # 1. Initialize three pointers, to track the current, previous and next nodes
    #    when we traverse the input list.
    #      node = head
    #      prevNode = None
    #      nextNode = None
    #
    # 2. While node is not null (None):
    #    2.1 Store the next node after the current node in nextNode.
    #        nextNode = node.next
    #
    #    2.2 Point the current node to the previous pointer.
    #        node.next = prevNode
    #
    #    2.3 Store the current node in prevNode.
    #        prevNode = node
    #    
    #    2.4 Move the current node to the next node.
    #        node = nextNode
    #
    #
    # 3. After the loop, prevNode points to the new head of the reversed list.
    #    Return prevNode and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def ReverseLinkedList(self, head):
        node = head
        prevNode = None
        nextNode = None
        
        while node:
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node= nextNode

        return prevNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [2, 4, 6, 8, 10]
    expectedOutput = list(reversed(nums))
    output = ToPythonList(solution.ReverseLinkedList(ToLinkedList(nums)))
    print(output, expectedOutput, output == expectedOutput)