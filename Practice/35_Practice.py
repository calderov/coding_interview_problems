# 143. Reorder List (Medium)
# You are given the head of a singly linked-list. The list can be represented as:
#
#   L0 → L1 → … → Ln - 1 → Ln
#
# Reorder the list to be on the following form:
#
#   L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
# You may not modify the values in the list's nodes. Only nodes themselves
# may be changed.
#
# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
#
# Example 2:
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
# Constraints:
# - The number of nodes in the list is in the range [1, 5 * 104].
# - 1 <= Node.val <= 1000

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def reverse(self, head):
        node = head
        nextNode = None
        prevNode = None

        while node:
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node = nextNode

        head = prevNode
        return head

    def splitAtMiddle(self, head):
        slow = head
        fast = head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        left = head
        right = slow.next

        slow.next = None

        return left, right

    def mergeLists(self, left, right):
        head = left
        while left and right:
            leftNext = left.next
            rightNext = right.next

            left.next = right
            right.next = leftNext

            left = leftNext
            right = rightNext

        return head

    # Time complexity: O(n)
    # Space complexity: O(1)
    def reorderList(self, head):
        left, right = self.splitAtMiddle(head)
        right = self.reverse(right)
        head = self.mergeLists(left, right)
        return head

def linkedListToPythonList(head):
    pythonList = []
    node = head

    while node:
        pythonList.append(node.val)
        node = node.next

    return pythonList

def pythonListToLinkedList(pythonList):
    head = None
    tail = None

    for value in pythonList:
        node = Node(value)

        if not head:
            head = node
            tail = node
            continue

        tail.next = node
        tail = node

    return head

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    inputList = [1,2,3,4]
    expectedOutput = [1,4,2,3]
    output = linkedListToPythonList(solution.reorderList(pythonListToLinkedList(inputList)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2:
    inputList = [1,2,3,4,5]
    expectedOutput = [1,5,2,4,3]
    output = linkedListToPythonList(solution.reorderList(pythonListToLinkedList(inputList)))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()