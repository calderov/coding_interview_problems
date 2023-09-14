# Problem:
# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized
# sub-list starting from the head.
#
# If, in the end, you are left with a sub-list with less than ‘k’ elements,
# reverse it too.
#
# Example:
#
#   Input:
#
#     list = head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> null
#     k = 3
#
#   Output:
#
#     list = head -> 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 8 -> 7 -> null
#

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

    for i in range(len(nums)):
        node = Node(nums[i])

        if head == None:
            head = node
            tail = head

        else:
            tail.next = node
            tail = node

    return head

class Solution:
    # Solution:
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def ReverseEveryKElementSuList(self, head, k):
        n = self.GetLength(head)

        # Reverse substrings of length k
        for i in range(n // k):
            p = k * i + 1
            q = k * (i + 1)
            head = self.ReverseSubstring(head, p, q)

        # Reverse residual string (if any)
        if n % k != 0:
            p = q + 1
            q = n
            head = self.ReverseSubstring(head, p, q)

        return head

    # For an explaination see 0702_ReverseSublist.py
    def ReverseSubstring(self, head, p, q):
        P = self.NodeAtIndex(head, p)
        Q = self.NodeAtIndex(head, q)

        P_prev = self.NodeAtIndex(head, p - 1)
        Q_next = Q.next

        if not P_prev:
            Q.next = None

            R_head = self.Reverse(head)
            R_tail = self.GetTail(R_head)

            head = R_head
            R_tail.next = Q_next

            return head
        else:
            P_prev.next = None
            Q.next = None

            R_head = self.Reverse(P)
            R_tail = self.GetTail(R_head)

            P_prev.next = R_head
            R_tail.next = Q_next

            return head

    def GetTail(self, head):
        tail = head
        while tail.next:
            tail = tail.next
        return tail

    def GetLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def NodeAtIndex(self, head, index):
        if index <= 0 or not head:
            return None

        i = 1
        while i < index:
            head = head.next
            i += 1

        return head

    def Reverse(self, head):
        node = head
        prevNode = None

        while node:
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node = nextNode

        return prevNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 4, 5, 6]
    k = 2
    expectedOutput = [2, 1, 4, 3, 6, 5]
    output = ToPythonList(solution.ReverseEveryKElementSuList(ToLinkedList(nums), k))
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 4
    expectedOutput = [4, 3, 2, 1, 7, 6, 5]
    output = ToPythonList(solution.ReverseEveryKElementSuList(ToLinkedList(nums), k))
    print(output, expectedOutput, output == expectedOutput)
