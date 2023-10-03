# Problem:
# Design a class to calculate the median of a number stream. The class should
# have the following two methods:
# 
#  insertNum(int num): stores the number in the class
#  findMedian(): returns the median of all numbers inserted in the class
# 
# If the count of numbers inserted in the class is even, the median will be
# the average of the middle two numbers.
# 
# Example 1:
# 
# 1. insertNum(3)
# 2. insertNum(1)
# 3. findMedian() -> output: 2
# 4. insertNum(5)
# 5. findMedian() -> output: 3
# 6. insertNum(4)
# 7. findMedian() -> output: 3.5
#

from heapq import *

# Solution:
# Use two heaps to store the numbers fed into the object. These heaps will effectively
# separate the numbers in two halfs, one containing the smallest numbers in the sample
# and one with the largest numbers in the sample.
#
# The small numbers heap must be a max-heap, so we can retrieve its maximum value easily.
# Analogously, the large numbers must be a min-heap, so the retrieval of its minimum value
# is also easy.
#
# Lets make this clear with the folowing example:
#   Input:
# 
#     [1, 2, 3, 4, 5]
# 
#   Internal representation
#
#     self.smallNumbers = [-3, -2, -1] (as small numbers are stored in a max-heap)
#     self.largeNumbers = [4, 5] (as large numbers are stored in a min-heap)
#
# From the example we can notice a couple of things. First, notice how the numbers in the
# small numbers heap are now negative. This was made on purpose so we can reuse the code
# for handling min-heaps to simulate the behavior of a max-heap. Just remember that whenever
# a value needs to be inserted to self.smallNumbers it needs to be multiplied by -1 first, the
# same goes for numbers retrieved from it, they need to be multiplied by -1 to restore their
# original value.
# 
# The second thing to notice is how self.smallNumbers is a bit longer than self.largeNumbers.
# This is because the total amount of numbers is odd, so by convention we place the additional
# number into self.smallNumbers when this is the case. The idea is that both heaps have roughly
# the same amount of numbers, differing by at most one number, in which case it will always be
# placed in self.smallNumbers.
#
# Insertion:
# With this restrictions in place we can describe the process of insertion as adding the given
# number into the self.smallNumbers heap if this heap is empty or if the given number is less
# than -1 * self.smallNumbers[0] (the largest original valued number in the heap). If this
# is not the case, then insert the given number into the self.largeNumbers heap.
#
# Then, if the amount of small numbers is greater than the amount of large numbers by more than 1,
# move the largest of the small numbers (-1 * self.smallNumbers[0]) to the large numbers heap.
# Otherwise, check if the amount of small numbers is less than the amount of large numbers.
# If so, move the smallest of the large numbers into the small numbers heap.
#
# This whole procedure balances the heaps containing small and large numbers, ensuring
# their sizes are equal if the total amount of numbers is even, or differing for at most
# one number which will always be placed on the small numbers heap.
#
# Find median:
# The inner balance between the heaps of large and small numbers make the procedure to find
# the median quite easy.
# 
# If the small numbers heap and the large numbers heap are the same size, the median will
# be the average between the largest number in the small numbers heap and the smallest number
# in the large numbers heap.
#
#   median = (-self.smallNumbers[0] + self.largeNumbers[0]) / 2.0
#
# Otherwise, the median is the largest number in the small numbers heap.
#
#   median = -self.smallNumbers[0])
#
# Solution complexity:
# Insertion time complexity:  O(log(n))
# Insertion space complexity: O(1)
# Find mean time complexity:  O(1)
# Find mean space complexity: O(1)
#
class Solution:

    def __init__(self):
        self.smallNumbers = [] # max-heap to store the first half of the given numbers
        self.largeNumbers = [] # min heap to store the second half of the given numbers

    def insertNum(self, num):
        # If the small numbers heap is empty, or the given number is less or equal than
        # the largest number in the small numbers heap, insert the number in the small
        # numbers heap.
        #
        # Otherwise, insert the number in the large numbers heap.
        if not self.smallNumbers or num <= -self.smallNumbers[0]:
            heappush(self.smallNumbers, -num)
        else:
            heappush(self.largeNumbers, num)

        # If the amount of small numbers is greater than the amount of large numbers by more than 1,
        # move the largest of the small numbers to the large numbers heap.
        #
        # Otherwise, check if the amount of small numbers is less than the amount of large numbers.
        # If so, move the smallest of the large numbers into the small numbers heap
        #
        # This whole procedure will balance the heaps containing small and large numbers, ensuring
        # their sizes are equal if the total amount of numbers is even, or differing for at most
        # one number which will always be placed on the small numbers heap.
        if len(self.smallNumbers) > len(self.largeNumbers) + 1:
            heappush(self.largeNumbers, -heappop(self.smallNumbers))

        elif len(self.smallNumbers) < len(self.largeNumbers):
            heappush(self.smallNumbers, -heappop(self.largeNumbers))
        
        return

    def findMedian(self):
        # If the small numbers heap and the large numbers heap are the same size,
        # return the average between the largest number in the small numbers heap
        # and the smallest number in the large numbers heap.
        #
        # Otherwise, return the largest number in the small numbers heap.
        if len(self.smallNumbers) == len(self.largeNumbers):
            return -self.smallNumbers[0] / 2.0 + self.largeNumbers[0] / 2.0
        return float(-self.smallNumbers[0])

if __name__ == "__main__":

    # Example 1
    solution = Solution()
    solution.insertNum(3)
    solution.insertNum(1)
   
    median = solution.findMedian()
    print(median,median == 2)

    solution.insertNum(5)
    
    median = solution.findMedian()
    print(median,median == 3)

    solution.insertNum(4)
    
    median = solution.findMedian()
    print(median,median == 3.5)

    # Example 2
    solution = Solution()
    solution.insertNum(5)
    solution.insertNum(1)
    solution.insertNum(4)

    median = solution.findMedian()
    print(median,median == 4.0)