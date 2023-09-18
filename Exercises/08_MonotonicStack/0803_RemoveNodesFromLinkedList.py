# Problem:
# Given the head node of a singly linked list, modify the list such that any
# node that has a node with a greater value to its right gets removed. The
# function should return the head of the modified list.
#
# Examples:
#
#   Input: 5 -> 3 -> 7 -> 4 -> 2 -> 1
#   Output: 7 -> 4 -> 2 -> 1
#   Explanation: 5 and 3 are removed as they have nodes with larger values
#                to their right.
#
#   Input: 1 -> 2 -> 3 -> 4 -> 5
#   Output: 5
#   Explanation: 1, 2, 3, and 4 are removed as they have nodes with larger
#                values to their right.
#
#   Input: 5 -> 4 -> 3 -> 2 -> 1
#   Output: 5 -> 4 -> 3 -> 2 -> 1
#   Explanation: None of the nodes are removed as none of them have nodes
#                with larger values to their right.
#

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    # Solution:
    # 1. Initialize a monotonically decreasing stack (use a Python list for this).
    #    stack = []
    #
    # 2. For each value in the list, insert it in the stack. Remember to follow the
    #    rules for it to be a monotonically decreasing stack.
    #
    # 3. Transform the stack into a list and return it.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def RemoveNodesV1(self, head):
        stack = []
        while head:
            value = head.val
            head = head.next

            if stack == None:
                stack.append(value)
                continue

            while stack and stack[-1] < value:
                stack.pop()

            stack.append(value)

        return ToLinkedList(stack)

    # Solution:
    # This solution is the same as the one at RemoveNodesV1, but implementing the
    # stack as a linked list from scratch.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def RemoveNodesV2(self, head):
        stack_head = None
        stack_tail = None

        while head:
            if stack_head == None:
                stack_head = Node(head.val)
                stack_tail = stack_head
                head = head.next
                continue

            if stack_head.val < head.val:
                stack_head = Node(head.val)
                stack_tail = stack_head
                head = head.next
                continue

            while stack_tail and stack_tail.val < head.val:
                stack_tail_predecessor = self.GetPredecessor(stack_head, stack_tail)
                if stack_tail_predecessor:
                    stack_tail_predecessor.next = None
                stack_tail = stack_tail_predecessor

            if stack_tail:
                stack_tail.next = Node(head.val)
                stack_tail = stack_tail.next
            else:
                stack_head = Node(head.val)
                stack_tail = stack_head

            head = head.next

        return stack_head

    def RemoveNodes(self, head):
        return self.RemoveNodesV2(head)

    def GetPredecessor(self, head, node):
        if head == node:
            return None

        predecessor = head
        while predecessor and predecessor.next != node :
            predecessor = predecessor.next

        return predecessor

def ToPythonList(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums

def ToLinkedList(nums):
    head = None
    tail = None

    for num in nums:
        node = Node(num)

        if head == None:
            head = node
            tail = head
        else:
            tail.next = node
            tail = node

    return head

if __name__ == "__main__":
    solution = Solution()

    examples = {
        1:  {'input':[5, 3, 7, 4, 2, 1], 'output': [7,4,2,1]},
        2:  {'input':[1, 2, 3, 4, 5],    'output': [5]},
        3:  {'input':[5, 4, 3, 2, 1],    'output': [5,4,3,2,1]},
        4:  {'input':[5, 4, 5, 4, 5],    'output': [5,5,5]},
        5:  {'input':[1, 1, 1, 1, 1],    'output': [1,1,1,1,1]},
        6:  {'input':[5, 4, 3, 4, 5],    'output': [5,5]},
        7:  {'input':[3],                'output': [3]},
        8:  {'input':[1, 2],             'output': [2]},
        9:  {'input':[],                 'output': []},
        10: {'input':[1, 2, 3, 2, 1],    'output': [3,2,1]},
        11: {'input':[5, 5, 3, 4, 5],    'output': [5,5,5]}
    }

    for i in examples:
        nums = examples[i]['input']
        expectedOutput = examples[i]['output']
        output = ToPythonList(solution.RemoveNodes(ToLinkedList(nums)))
        print('Example ', i)
        print(output)
        print(expectedOutput)
        print(output == expectedOutput)
        print()
