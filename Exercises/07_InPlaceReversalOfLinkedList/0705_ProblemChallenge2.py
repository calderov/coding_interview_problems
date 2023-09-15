# Problem:
# Given the head of a Singly LinkedList and a number ‘k’, rotate the
# LinkedList to the right by ‘k’ nodes.
#
# Example:
#
#   Input:
#
#     head 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
#     k = 3
#
#   Output:
#
#     head 4 -> 5 -> 6 -> 1 -> 2 -> 3 -> null
#

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    # Solution:
    # 1. Let n be the length of the list and tail its last node.
    #
    # 2. Make a circular list by connecting the tail node to the head
    #
    # 3. Rotate the list backwards k times.
    #
    #    Note: The circular list can only rotate forward (to the right),
    #          and we need to rotate k positions backwards (to the left).
    #
    #          Since each backwards rotation equals n - 1 forward rotations,
    #          we need k * (n - 1) forward rotations to simulate k backwards
    #          rotations.
    #
    #          Forward rotating k * (n - 1) times can be a heavy operation.
    #          Luckily, we can reduce this by remembering that every n rotations
    #          puts the list being in the same position (is a cycle). Thus, if we
    #          substract the number of rotations spent in complete rotations from
    #          k * (n - 1) we'll get a smaller number of rotations and achieve the
    #          same effect.
    #
    #          In other words:
    #          - The list after k backwards rotations, is the same that the list 
    #            after k * (n - 1) forward rotations
    #
    #          - This in turn is the same as the list after 
    #            
    #              k * (n - 1) - ((k * (n - 1)) // n) * n
    #
    #            rotations, where ((k * (n - 1)) // n) * n is the number of rotations
    #            previously spent in complete cycles.
    #
    #          We can still do better, lets look at our latest expression once again
    #
    #            rotations = k * (n - 1) - ((k * (n - 1)) // n) * n
    #
    #          since we are substracting the rotations that completely cycle the list,
    #          this expression can be written in terms of modular arithmetic as:
    #
    #            rotation = k * (n - 1) % n
    #
    #          This expression is a bit better as it is shorter and easier to understand.
    #
    #          Finally, to simulate the rotation of the list backwards k times, just rotate
    #          the list forward for k * (n - 1) % n times.
    #
    # 4. Detach the tail from the head to go back to a regular linked list.
    # 
    # 5. Return the head and finish
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def RotateLinkedList(self, head, k):
        # Find lenght and the tail of the list
        n = self.GetLength(head)
        tail = self.GetTail(head)

        # Make a circular list by connecting the tail to the head
        tail.next = head

        # Rotate the list backwards k times.
        rotations = k * (n - 1) % n
        for i in range(rotations):
            head = head.next
            tail = tail.next

        # Dettach the tail from the head
        tail.next = None

        return head

    def GetLength(self, head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    def GetTail(self, head):
        tail = head
        while tail.next:
            tail = tail.next
        return tail

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

    # Example 1
    nums = [1, 2, 3, 4, 5, 6]
    k = 3
    expectedOutput = [4, 5, 6, 1, 2, 3]
    output = ToPythonList(solution.RotateLinkedList(ToLinkedList(nums), k))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)

    print()

    # Example 2
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 5
    expectedOutput = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    output = ToPythonList(solution.RotateLinkedList(ToLinkedList(nums), k))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)

    print()

    # Example 3
    nums = [10, 20, 30, 40, 50]
    k = 2
    expectedOutput = [40, 50, 10, 20, 30]
    output = ToPythonList(solution.RotateLinkedList(ToLinkedList(nums), k))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)