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
            return True

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

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    head, expectedOutput = Example1()
    output = solution.IsPalindrome(head)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    head, expectedOutput = Example2()
    output = solution.IsPalindrome(head)
    print(output, expectedOutput, output == expectedOutput)
    