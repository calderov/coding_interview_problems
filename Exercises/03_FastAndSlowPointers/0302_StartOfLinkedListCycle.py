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
    # Use a fast and slow pointer to detect the cycle. When the cycle is detected
    # compute the cycle lenght (N) and keep it in a variable.
    # 
    # Then set the fast pointer N positions ahead of the head and set the slow 
    # pointer on the head. Now both slow and fast are spaced by N positions.
    # Move slow and fast one position forward until their values are the same,
    # then return either of them
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindCycleStart(self, head):
        fast = head
        slow = head

        # Detect cycle
        while True:
            # Return early if there is noloop in the list
            if fast == None or fast.next == None or fast.next.next == None:
                return None
            
            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                break

        # Compute cycle lenght
        cycleLength = self.GetCycleLength(slow)
        
        # Move the fast pointer cycleLength positions ahead of the head
        # and point the slow pointer to the head
        fast = slow
        slow = head

        # Move slow and fast together until their values are equal, then return
        for i in range(cycleLength + 1):
            if slow.val == fast.val:
                return slow
            slow = slow.next
            fast = fast.next
        
        # Unreachable
        return None
        
    
    def GetCycleLength(self, nodeInLoop):
        cycleLength = 1
        val = nodeInLoop.val

        while nodeInLoop.next.val != val:
            cycleLength += 1
            nodeInLoop = nodeInLoop.next

        return cycleLength

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
