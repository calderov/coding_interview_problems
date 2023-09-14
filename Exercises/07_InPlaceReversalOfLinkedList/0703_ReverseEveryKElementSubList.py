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
    # 1. Let n be the length of the list.
    #
    # 2. Then n / k is the number of sub-lists of length k in the list.
    #    Since there is the chance that n is not perfectly divisible by k,
    #    lets handle this as a regular integer division n // k and address
    #    the remainder later.
    #
    # 3. For each i in the range [0, n // k) compute two indexes p and q to
    #    delimit the start and end of the sub-list we want to reverse. Then,
    #    reverse the sub-list:
    #      p = k * i * + 1
    #      q = k * (i + 1)
    #      head = ReverseSublist(head, p, q)
    # 
    # 4. After the for loop of the previous step is finished, there is a chance
    #    our list is still missing one more reversal. That is, if the remainder
    #    of n / k is different from zero (n % k != 0) then reverse the sub-list
    #    between k * (n // k) + 1 and n:
    #      p = k * (n // k) + 1
    #      q = n
    #      head = ReverseSublist(head, p, q)
    #
    # 5. Return the head of the list and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def ReverseEveryKElementSuList(self, head, k):
        n = self.GetLength(head)

        # Reverse sub-lists of length k
        for i in range(n // k):
            p = k * i + 1
            q = k * (i + 1)
            head = self.ReverseSublist(head, p, q)

        # Reverse residual sub-list (if any)
        if n % k != 0:
            p = k * (n // k) + 1
            q = n
            head = self.ReverseSublist(head, p, q)

        return head

    # Given a list and two indexes p and q, reverses the sub-list between
    # p and q in place and returns the list.
    #
    # Time complexity: O(n)
    # Space complexity: O
    def ReverseSublist(self, head, p, q):
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
