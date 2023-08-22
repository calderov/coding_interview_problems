# Problem:
# Given the head of a LinkedList, write a method to check if the LinkedList
# is a palindrome or not.
#
# Your algorithm should use constant space and the input LinkedList should be
# in the original form once the algorithm is finished. The algorithm should
# have O(n) time complexity where n is the number of nodes in the LinkedList.
#
# Examples:
#
#   Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
#   Output: True
#
#   Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
#   Output: False
#

class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    # Solution:
    # 1. Find the center of the list.
    # 
    # 2. Reverse the right side of the list.
    # 
    # 3. Initialize a variable isPalidnrome to True and traverse the list comparing
    #    the elements from start to the center (left side) to the elements from the
    #    center to the end (right side). If a difference between elements if found
    #    change the value of isPalindrome to False. 
    # 
    # 3. Reverse the right side once again to restore the original list.
    # 
    # 4. Return wether or not the list is a palindrome. i.e. return isPalindrome.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def IsPalindrome(self, head):
        # Return early if the list is empty or singular
        if head is None or head.next is None:
            return True

        # Find the list center
        center = self.GetListCenter(head)

        # Reverse the list from the center onwards
        center = self.Reverse(center)

        # Compare the left and right sides of the list to see if the original list is a palindrome
        left = head
        right = center
        isPalindrome = True
        while left is not None and right is not None:
            if left.val != right.val:
                isPalindrome = False
                break
            left = left.next
            right = right.next

        # Reverse the right side once again
        center = self.Reverse(center)

        # Return if the original list is palindrome or not
        return isPalindrome

    def GetListCenter(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def Reverse(self, head):
        prevNode = None
        while head is not None:
            nextNode = head.next
            head.next = prevNode
            prevNode = head
            head = nextNode
        return prevNode

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

def PrintList(head):
    node = head
    listString = ""
    while node != None:
        listString += str(node.val) + " "
        node = node.next
    print(listString)

if __name__ == "__main__":
    solution = Solution()

    examples = {
        1: ([2,4,6,4,2], True),
        2: ([2,4,6,4,2,2], False),
        3: ([1], True),
        4: ([1,2,1], True),
        5: ([1,2], False),
        6: ([1,2,2,1], True),
        7: ([1,2,3,2,1], True),
        8: ([1,2,3,4,2,1], False),
        9: ([1,2,3,3,2,1], True),
        10: ([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1], True),
        11: ([1,2,3,4,5,6,7,8,9,10,10,8,7,6,5,4,3,2,1], False),
        12: ([1,1,2,2,3,3,4,4], False),
        13: ([4,4,3,3,2,2,1,1], False),
        14: ([10,20,30,40,50,60,70,80,90,100,90,80,70,60,50,40,30,20,10], True),
    }

    for example in examples:
        nums, expectedOutput = examples[example]
        head = MakeLinkedList(nums)
        output = solution.IsPalindrome(head)

        print("Example %d:" % example)
        PrintList(head)
        print("Palindrome:", output, "  Expected:", expectedOutput, "  Success:", output == expectedOutput)
        print()
    