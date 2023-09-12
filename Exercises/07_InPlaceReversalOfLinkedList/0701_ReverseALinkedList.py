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
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def ReverseLinkedList(self, head):
        return head

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [2, 4, 6, 8, 10]
    expectedOutput = list(reversed(nums))
    output = ToPythonList(solution.ReverseLinkedList(ToLinkedList(nums)))
    print(output, expectedOutput, output == expectedOutput)