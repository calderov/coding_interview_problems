# Problem:
# Given the head of a LinkedList, write a function to determine if the LinkedList
# has a cycle in it or not.
#
# Example:
#          ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐
#  Head───►│1├──►│2├──►│3├──►│4├──►│5├──►│6│
#          └─┘   └─┘   └─┘   └─┘   └─┘   └┬┘
#                       ▲                 │
#                       └─────────────────┘

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    # Solution:
    # Set two pointers on the head of the list, one named fast and one named slow.
    # 
    # The slow pointer will traverse the list one position at a time, while the fast pointer
    # will do it two positions at a time (thus its name). If the pointers reach the end of
    # the list (a node that is or points to None), return False as there is no cycle in the
    # list. Otherwise, keep moving the pointers until the value in the node pointed by both
    # is the same. i.e. slow.val == fast.val, then return True, as a cycle has been detected.
    #
    # Solution complexity:
    # Space complexity: O(n)
    # Time complexity: O(1)
    def HasCycle(self, head):
        fast = head
        slow = head

        while True:
            if fast == None or fast.next == None or fast.next.next == None:
                return False

            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                return True
            
# Example 1:
#          ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐
#  Head───►│1├──►│2├──►│3├──►│4├──►│5├──►│6│
#          └─┘   └─┘   └─┘   └─┘   └─┘   └┬┘
#                       ▲                 │
#                       └─────────────────┘
def Example1():
    # Insert elements
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Insert loop
    head.next.next.next.next.next.next = head.next.next # Point tail to the 3rd node
    return head

# Example 2:
#          ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌──┐
#  Head───►│2├──►│4├──►│6├──►│8├──►│10├──►None
#          └─┘   └─┘   └─┘   └─┘   └──┘
#
def Example2():
    # Insert elements
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    return head

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head = Example1()
    expectedOutput = True
    output = solution.HasCycle(head)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    head = Example2()
    expectedOutput = False
    output = solution.HasCycle(head)
    print(output, expectedOutput, output == expectedOutput)



    
