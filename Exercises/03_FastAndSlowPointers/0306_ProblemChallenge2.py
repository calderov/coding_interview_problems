# Problem:
# Given the head of a LinkedList, write a method to modify it such that the
# nodes from the second half of the LinkedList are inserted alternately to
# the nodes from the first half in reverse order.
#
# So if the LinkedList has nodes:
#   1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
#
# your method should return
#   1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null
#
# Your algorithm should not use any extra space and the input LinkedList
# should be modified in-place.
#
# Examples:
#
#   Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
#   Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null
#
#   Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
#   Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    # Solution:
    # 1. Find the center of the list.
    # 2. Split the list at the center
    # 3. Reverse the second half of the list.
    # 4. Merge both lists in alternating order and return.
    #
    # Solution complexity: O(n)
    # Solution complexity: O(1) as the transformations to the list are made in place
    def Reorder(self, head):
        # Return early if list is empty or singular
        if head is None or head.next is None:
            return head

        # Find the center of the list
        center = self.GetListCenter(head)

        # Split the list at the center
        self.Split(head, center)

        # Reverse the second half of the list
        center = self.Reverse(center)

        # Merge both lists in alternating order
        head = self.MergeAlternated(head, center)

        return head
    
    def Split(self, head, cutNode):
        node = head
        while node is not None and node.next is not cutNode:
            node = node.next
        if node:
            node.next = None

    def InsertAfter(self, node, newNode):
        if node:
            oldNext = node.next
            node.next = newNode
            newNode.next = oldNext

    def MergeAlternated(self, headL, headR):
        originalHead = headL
        while headR is not None:
            # Pop first node from headR
            node = headR
            headR = headR.next
            node.next = None

            # Insert node after headL
            self.InsertAfter(headL, node)

            # Move headL two nodes forward
            headL = headL.next
            if headL.next:
                headL = headL.next

        return originalHead

    def Reverse(self, head):
        prevNode = None
        while head is not None:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode

    def GetListCenter(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

def MakeLinkedList(arr):
    head = None
    tail = None

    for val in arr:
        # If this is the fist item in the list
        if tail == None:
            tail = Node(val)
            head = tail
        else:
            node = Node(val)
            tail.next = node
            tail = node

    return head

def LinkedListToPythonList(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums

def Reorder(nums):
    solution = Solution()
    
    head = MakeLinkedList(nums)
    head = solution.Reorder(head)

    return LinkedListToPythonList(head)

if __name__=="__main__":
    # Example 1
    exampleInput = [2, 4, 6, 8, 10, 12]
    expectedOutput = [2, 12, 4, 10, 6, 8]
    output = Reorder(exampleInput)
    print("Input: ", exampleInput)
    print("Output:", output)
    print("Success:", output == expectedOutput)
    print()

    # Example 2
    exampleInput = [2, 4, 6, 8, 10]
    expectedOutput = [2, 10, 4, 8, 6]
    output = Reorder(exampleInput)
    print("Input: ", exampleInput)
    print("Output:", output)
    print("Success:", output == expectedOutput)
    print()

    # Example 3
    exampleInput = [1, 2]
    expectedOutput = [1, 2]
    output = Reorder(exampleInput)
    print("Input: ", exampleInput)
    print("Output:", output)
    print("Success:", output == expectedOutput)
    print()