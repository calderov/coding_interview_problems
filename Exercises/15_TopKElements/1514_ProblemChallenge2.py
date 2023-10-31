# Problem:
# Design a class that simulates a Stack data structure, implementing the
# following two operations:
# 
#  push(int num): Pushes the number ‘num’ on the stack.
#  
#  pop(): Returns the most frequent number in the stack. If there is a tie,
#         return the number which was pushed later.
# 
# Example:
# 
#   After following push operations: push(1), push(2), push(3), push(2),
#   push(1), push(2), push(5)
# 
#   1. pop() should return 2, as it is the most frequent number
#   2. Next pop() should return 1
#   3. Next pop() should return 2
# 

from heapq import *

# Solution:
# For insertion:
#  Use a class scoped hash map to track the instances of each number in the stack.
#  Each instance is registered as the time 't' when the number was pushed
#  into the stack.
#  
#  For example, lets assume the following sequence of operations
#   
#   push(1)
#   push(1)
#   push(1)
#   push(2)
#   push(3)
#
#  These will produce the internal instances map and time tracker t to look like this
#   
#   instances = {1:[1, 2, 3], 2:[4], 3:[5]}
#   t = 5
#
#  Notice how t = 5 and the last instance of 3 is also 5. This is because t is increased
#  just before inserting a new item, this is an implementation detail that may be changed
#  if desired.
#
# For extraction:
#  Push the items of the instances tracker into a max heap based on their frequency (how 
#  many instances does a number have). Let's refer to this heap as the most frequent heap.
#  
#  If the number at the top of the most frequent heap is more  frequent than the one that
#  follows, discard the last of it's instances and return it.
#
#  Otherwise, use another max heap as a buffer to store the last instance of each number 
#  that is as frequent as the most frequent number. This max heap should maximize based
#  on how 'late' the last instance of each number came.
#  
#  Since the buffer is a max heap, its number at the top should be that which is among 
#  the most frequent numbers and came later into the stack. Pop it, discard it's last
#  instance and return it.
#
#  Solution complexity:
#  Time complexity: Insertion O(1) assuming perfect hashing. Extraction O(n log(n))
#  Space complexity: O(n)
class Solution:
    def __init__(self):
        self.t = 0
        self.instances = {}

    def push(self, num):
        self.t += 1
        if num not in self.instances:
            self.instances[num] = []
        self.instances[num].append(self.t)

    def pop(self):
        # Push the items in the instances tracker into a max heap
        # based on their frequency (how many instances does a number have).
        # Let's refer to this heap as the most frequent heap
        mostFrequent = [] # max heap
        for num, instances in self.instances.items():
            heappush(mostFrequent, (-len(instances), num))

        # If the number at the top of the most frequent heap is more 
        # frequent than the one that follows, discard the last of it's
        # instances and return it.
        freq, num = heappop(mostFrequent)
        if -freq > -mostFrequent[0][0]:
            self.instances[num].pop()
            return num
        
        # Otherwise, use another max heap as a buffer to store
        # the last instance of each number that is as frequent
        # as the most frequent number. The max heap should maximize
        # based on how 'late' the last instance of each number came
        buffer = [(-self.instances[num][-1], num)] # max heap
        while mostFrequent and freq == mostFrequent[0][0]:
            _, num = heappop(mostFrequent)
            heappush(buffer, (-self.instances[num][-1], num))
        
        # Since the buffer is a max heap, its number at the top
        # should be that which is among the most frequent numbers
        # and came later into the stack. Pop it, discard it's
        # last instance and return it
        _, num = heappop(buffer)
        self.instances[num].pop()
        return num


if __name__ == "__main__":
    stack = Solution()

    # Example 1
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.push(2)
    stack.push(5)

    output = stack.pop()
    expectedOutput = 2
    print(output, expectedOutput, output == expectedOutput)

    output = stack.pop()
    expectedOutput = 1
    print(output, expectedOutput, output == expectedOutput)

    output = stack.pop()
    expectedOutput = 2
    print(output, expectedOutput, output == expectedOutput)
