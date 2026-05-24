# Add Two Numbers
# MEDIUM
# https://scaleengineer.com/dsa/problems/add-two-numbers

# Description
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Constraints:
#     The number of nodes in each linked list is in the range [1, 100].
#     0 <= Node.val <= 9
#     It is guaranteed that the list represents a number that does not have leading zeros.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def PythonListToLinkedList(nums):
    head = None
    tail = None

    for num in nums:
        node = Node(num)
        
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    
    return head

def LinkedListToPythonList(head):
    nums = []
    node = head
    while node:
        nums.append(node.val)
        node = node.next
    return nums

def AppendToList(head, tail, node):
    if not head:
        head = node
        tail = node
    else:
        tail.next = node
        tail = node
    return head, tail

def AddTwoNumbers(head1, head2):
    resultHead = None
    resultTail = None
    carry = 0

    node1 = head1
    node2 = head2

    while node1 and node2:
        value = (node1.val + node2.val + carry) % 10
        carry = (node1.val + node2.val + carry) // 10
        resultHead, resultTail = AppendToList(resultHead, resultTail, Node(value))
        node1 = node1.next
        node2 = node2.next

    while node1:
        value = (node1.val + carry) % 10
        carry = (node1.val + carry) // 10
        resultHead, resultTail = AppendToList(resultHead, resultTail, Node(value))
        node1 = node1.next

    while node2:
        value = (node2.val + carry) % 10
        carry = (node2.val + carry) // 10
        resultHead, resultTail = AppendToList(resultHead, resultTail, Node(value))
        node2 = node2.next

    if carry:
        resultHead, resultTail = AppendToList(resultHead, resultTail, Node(carry))

    return resultHead

if __name__ == "__main__":
    # Example 1:
    l1 = PythonListToLinkedList([2,4,3])
    l2 = PythonListToLinkedList([5,6,4])
    expected = [7,0,8]
    output = LinkedListToPythonList(AddTwoNumbers(l1, l2))
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    l1 = PythonListToLinkedList([0])
    l2 = PythonListToLinkedList([0])
    expected = [0]
    output = LinkedListToPythonList(AddTwoNumbers(l1, l2))
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3:
    l1 = PythonListToLinkedList([9,9,9,9,9,9,9])
    l2 = PythonListToLinkedList([9,9,9,9])
    expected = [8,9,9,9,0,0,0,1]
    output = LinkedListToPythonList(AddTwoNumbers(l1, l2))
    print(expected)
    print(output)
    print(expected == output)
    print()