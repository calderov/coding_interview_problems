# Problem:
# Given the head of a LinkedList that contains a cycle,
# write a function to find the starting node of the cycle.
# 
# Example:
#
#                   Cycle start
#                        │
#                        ▼
#           ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐
#   Head───►│1├──►│2├──►│3├──►│4├──►│5├──►│6│
#           └─┘   └─┘   └─┘   └─┘   └─┘   └┬┘
#                        ▲                 │
#                        └─────────────────┘
#

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    # Solution:
    # Use a fast and slow pointer to detect the cycle, keep track of how many
    # jumps did the slow pointer made along the way, and keep this count in a
    # variable named slowJumps.
    #
    # Once we know how far the slow pointer was when the cycle was detected,
    # (head + slowJums) we know that the cycle starts somewhere up to that point.
    #
    # Reset the slow pointer to point at the head of the list and move the fast
    # pointer one position ahead of slow.
    #
    # Now, lets run two nested loops. One will move the slow pointer through the
    # list while the other moves the fast pointer up to jumpSlow positions ahead
    # of it. At every position touched by the fast pointer, compare the nodes
    # pointed by both pointers. If they have the same value, it means that we
    # have found the node that starts the cycle. Return the node and finish.
    #
    # Solution complexity:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(1)
    def FindCycleStart(self, head):
        fast = head
        slow = head

        # Find how far the slow pointer goes at the time the cycle is detected
        slowJumps = 0

        while True:
            # Return early if there is noloop in the list
            if fast == None or fast.next == None or fast.next.next == None:
                return None
            
            fast = fast.next.next
            slow = slow.next

            slowJumps += 1

            if fast.val == slow.val:
                break

        # Find the exact point where the cycle starts
        cycleIndex = 0
        slow = head
        fast = head.next # One position ahead of slow

        # Slow loop
        while cycleIndex < slowJumps + 1:

            # Fast loop
            for i in range(slowJumps + 1):
                if fast.val == slow.val:
                    return slow

                fast = fast.next

            # Move the slow pointer one position and reset fast pointer            
            slow = slow.next
            fast = slow.next # One position ahead of slow

            cycleIndex += 1
        
        # This should be unreachable!
        return None

# Example 1:
#
#                   Cycle start
#                        │
#                        ▼
#           ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐
#   Head───►│1├──►│2├──►│3├──►│4├──►│5├──►│6│
#           └─┘   └─┘   └─┘   └─┘   └─┘   └┬┘
#                        ▲                 │
#                        └─────────────────┘
#
def Example1():
    # Insert elements
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Insert loops
    head.next.next.next.next.next.next = head.next.next # Point tail to the 3rd node
    return head, head.next.next # Return the head of the list and 
                                # the node where the cycle begins

# Example 2:
#
#                         Cycle start
#                              │
#                              ▼
#           ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐
#   Head───►│1├──►│2├──►│3├──►│4├──►│5├──►│6│
#           └─┘   └─┘   └─┘   └─┘   └─┘   └┬┘
#                              ▲           │
#                              └───────────┘
#
def Example2():
    # Insert elements
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Insert loops
    head.next.next.next.next.next.next = head.next.next.next # Point tail to the 4th node
    return head, head.next.next.next # Return the head of the list and 
                                     # the node where the cycle begins 

# Example 3:
#
#        Cycle start
#            │
#            ▼
#           ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐   ┌─┐
#   Head───►│1├──►│2├──►│3├──►│4├──►│5├──►│6│
#           └─┘   └─┘   └─┘   └─┘   └─┘   └┬┘
#            ▲                             │
#            └─────────────────────────────┘
#
def Example3():
    # Insert elements
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    # Insert loops
    head.next.next.next.next.next.next = head # Point tail to the 1st node
    return head, head

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head, expectedOutput = Example1()
    output = solution.FindCycleStart(head)
    print(output.val, expectedOutput.val, output == expectedOutput)

    # Example 2
    head, expectedOutput = Example2()
    output = solution.FindCycleStart(head)
    print(output.val, expectedOutput.val, output == expectedOutput)

    # Example 3
    head, expectedOutput = Example3()
    output = solution.FindCycleStart(head)
    print(output.val, expectedOutput.val, output == expectedOutput)
