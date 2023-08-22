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
    # 1. Split the list in two by the center.
    # 
    # 2. Reverse the right list and compare it with the left one until the left list is
    #    traversed or a difference is found. If the comparisons are all equal, it means
    #    that the original list is a palindrome, otherwise it is not. Save this info in
    #    a variable named isPalindrome.
    # 
    # 3. Reverse the right list once again and merge the left and right lists together to
    #   restore the original list.
    # 
    # 4. Return wether or not the list is a palindrome. i.e. return isPalindrome.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def IsPalindrome(self, head):
        # Return early if the list is empty or singular
        if head == None or head.next == None:
            return True

        # Find the list center
        center = self.GetListCenter(head)
        
        # Slice the list in two
        leftList, rightList = self.SliceList(head, center)
        
        # Reverse right side
        rightList = self.Reverse(rightList)

        # Compare the lists until the left list is traversed or a difference is found
        isPalindrome = True

        leftNode = leftList
        rightNode = rightList

        while leftNode != None:
            if leftNode.val != rightNode.val:
                isPalindrome = False
                break
            leftNode = leftNode.next
            rightNode = rightNode.next

        # Reverse the right side once again
        rightList = self.Reverse(rightList)
        
        # Append the right side to the left side so the original list is restored
        self.MergeLists(leftList, rightList)

        # Return if the original list is palindrome or not
        return isPalindrome

    def MergeLists(self, leftList, rightList):
        if leftList == None:
            return rightList
        
        if rightList == None:
            return leftList
        
        leftNode = leftList
        while leftNode.next != None:
            leftNode = leftNode.next
        
        leftNode.next = rightList
        return leftList

    def SliceList(self, startNode, endNode):
        node = startNode
        while node.next != endNode:
            node = node.next
        node.next = None
        return startNode, endNode

    def GetListCenter(self, head):
        # Return early if the list is empty or singular
        if head == None or head.next == None:
            return head

        # Find the middle
        slow = head
        fast = head.next

        while True:
            if fast == None:
                return slow
            
            if fast.next == None:
                return slow.next

            slow = slow.next
            fast = fast.next.next   
    
    def Reverse(self, head, prevNode=None):
        # Return early if the list is empty or singular
        if head == None or head.next == None:
            return head

        node = head
        nextNode = node.next

        while True:
            node.next = prevNode
            if nextNode == None:
                break
            prevNode = node
            node = nextNode
            nextNode = node.next

        return node

# Example1
#   Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
#   Output: True
def Example1():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    return head, True

# Example2
#   Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
#   Output: False
def Example2():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(2)
    return head, False

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
        5: ([1,2], True),
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
        print("Palindrome:", output)
        print("Expected:  ", expectedOutput)
        print()
    