# Problem:
# Given the head of a Singly LinkedList, write a method to return the middle node
# of the LinkedList.
#
# If the total number of nodes in the LinkedList is even, return the second middle node.
#
# Examples:
#
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3
#
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    # Solution:
    # Use a slow and fast pointer, the slow pointer will traverse the list
    # one item at a time, while the fast pointer will traverse it two items
    # at a time. Thus, when the fast pointer reaches the end of the list, the
    # slow pointer will be placed in the middle (as it moved at half the speed)
    # return the slow pointer at this point.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindMiddle(self, head):
        # Return early on empty lists
        if head == None:
            return None

        slow = head
        fast = head.next

        while True:
            if fast == None:
                return slow

            if fast.next == None:
                return slow.next

            slow = slow.next
            fast = fast.next.next
    
# Example 1:
# List: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Middle: 3
def Example1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    return head, head.next.next

# Example 2:
# List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Middle: 4
def Example2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    return head, head.next.next.next

# Example 3:
# List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Middle: 4
def Example3():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    return head, head.next.next.next


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head, expectedOutput = Example1()
    output = solution.FindMiddle(head)
    print(output.val, expectedOutput.val, output == expectedOutput)

    # Example 2
    head, expectedOutput = Example2()
    output = solution.FindMiddle(head)
    print(output.val, expectedOutput.val, output == expectedOutput)

    # Example 3
    head, expectedOutput = Example3()
    output = solution.FindMiddle(head)
    print(output.val, expectedOutput.val, output == expectedOutput)
