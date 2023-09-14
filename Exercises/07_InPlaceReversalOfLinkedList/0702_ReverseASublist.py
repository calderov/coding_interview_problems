# Problem:
# Given the head of a LinkedList and two positions p and q, reverse the
# LinkedList from position p to q.
#
# Example:
#
#   Input:
#
#     list = head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
#     p = 2
#     q = 4
#
#   Output:
#
#     list = head -> 1 -> 4 -> 3 -> 2 -> 5 -> null

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
        if tail == None:
            tail = Node(nums[i])
            head = tail
        else:
            node = Node(nums[i])
            tail.next = node
            tail = node

    return head

class Solution:
    # Solution:
    # 1. Traverse the list and get the nodes P and Q that are those at indexes p and q respectively.
    #
    # 2. Find the predecessor of P (P_prev) and the successor of Q (Q_next).
    #
    # 3. If there is not predecesor to P, it means that P is the first element of the list (a.k.a the head).
    #    In this case:
    #    
    #    3.1 Detach Q from its successor.
    #    
    #    3.2 Reverse the list between P and Q.
    #    
    #    3.3 Replace the head of the list with that of the reversed list and
    #        attach the tail of the reversed list to the successor of Q.
    #
    #    3.4 Return head and finish
    #
    # 4. If there is a predecessor:
    #
    #    4.1 Detach P from its predecessor and Q from its successor.
    #
    #    4.2 Reverse the list between P and Q.
    #
    #    4.3 Attach the predecessor of P to the head of the reversed list
    #       and the tail of the reversed list to the successor of Q.
    #
    #    4.4 Return head and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def ReverseSublist(self, head, p, q):
        # Return early if p == q or p == 0 or q == 0 or p > q
        if p == q or p == 0 or q == 0 or p > q:
            return head

        # Get the nodes P and Q that are those at indexes p and q respectively
        P = self.NodeAtIndex(head, p)
        Q = self.NodeAtIndex(head, q)

        # Return early if P or Q ar missing
        if not P or not Q:
            return head

        # Find the predecessor of P and the successor of Q
        P_prev = self.NodeAtIndex(head, p - 1)
        Q_next = Q.next

        # If there is no predecessor to P, it means that P is the first element in the list (a.k.a the head)
        if not P_prev:
            # Detach Q from its successor
            Q.next = None

            # Reverse the list between P and Q
            R_head = self.Reverse(P)
            R_tail = self.GetTail(R_head)

            # Replace the head of the list with that of the reversed list
            # and attach the tail of the reversed list to the successor of Q
            head = R_head
            R_tail.next = Q_next

            return head

        # Otherwise
        else:
            # Detach P from its predecessor and Q from its successor
            P_prev.next = None
            Q.next = None

            # Reverse the list between P and Q
            R_head = self.Reverse(P)
            R_tail = self.GetTail(R_head)

            # Attach the predecessor of P to the head of the reversed list
            # and the tail of the reversed list to the successor of Q
            P_prev.next = R_head
            R_tail.next = Q_next

            return head

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
        while i < index and head:
            head = head.next
            i += 1

        return head

    def GetTail(self, head):
        tail = head
        while tail.next:
            tail = tail.next
        return tail

    def Reverse(self, head):
        node = head
        prevNode = None
        nextNode = None

        while node:
            nextNode = node.next
            node.next = prevNode
            prevNode = node
            node = nextNode

        return prevNode

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 4, 5]
    p = 2
    q = 4
    expectedOutput = [1, 4, 3, 2, 5]
    output = ToPythonList(solution.ReverseSublist(ToLinkedList(nums), p, q))
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 2, 3, 4, 5, 6]
    p = 1
    q = 4
    expectedOutput = [4, 3, 2, 1, 5, 6]
    output = ToPythonList(solution.ReverseSublist(ToLinkedList(nums), p, q))
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 2, 3, 4, 5, 6, 7]
    p = 3
    q = 7
    expectedOutput = [1, 2, 7, 6, 5, 4, 3]
    output = ToPythonList(solution.ReverseSublist(ToLinkedList(nums), p, q))
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = [100, 200, 300, 400, 500]
    p = 2
    q = 5
    expectedOutput = [100, 500, 400, 300, 200]
    output = ToPythonList(solution.ReverseSublist(ToLinkedList(nums), p, q))
    print(output, expectedOutput, output == expectedOutput)
