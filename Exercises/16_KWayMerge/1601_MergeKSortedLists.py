# Problem:
# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
# 
# Example:
# 
#   Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
#   Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]
# 

from heapq import *

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    # Solution:
    # Push every item of every list into a min heap. Then extract all the items
    # from the min heap and store them into a different list (merged).
    # Return the merged list and finish.
    #
    # Solution complexity:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)
    def MergeKSortedLists(self, lists):
        minHeap = []
        for head in lists:
            while head:
                heappush(minHeap, head.val)
                head = head.next
        
        mergedHead = None
        mergedTail = None
        while minHeap:
            node = ListNode(heappop(minHeap))
            
            if mergedHead == None:
                mergedHead = node
                mergedTail = mergedHead

            else:
                mergedTail.next = node
                mergedTail = mergedTail.next

        return mergedHead

def ToLinkedList(nums):
    head = None
    tail = None

    for num in nums:
        node = ListNode(num)

        if head == None:
            head = node
            tail = head

        else:
            tail.next = node
            tail = node
    
    return head

def ToPythonList(head):
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums

def ToListOfLists(pythonLists):
    listOfLists = []
    for _list in pythonLists:
        listOfLists.append(ToLinkedList(_list))
    return listOfLists

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    lists = ToListOfLists([[2, 6, 8], [3, 6, 7], [1, 3, 4]])
    expectedOutput = [1, 2, 3, 3, 4, 6, 6, 7, 8]
    output = ToPythonList(solution.MergeKSortedLists(lists))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    assert(output == expectedOutput)
    print()

    # Example 2
    lists = ToListOfLists([[5, 8, 9], [1, 7]])
    expectedOutput = [1, 5, 7, 8, 9]
    output = ToPythonList(solution.MergeKSortedLists(lists))
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    assert(output == expectedOutput)
    print()
