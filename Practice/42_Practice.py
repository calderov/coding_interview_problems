# Kth Largest Integer in a Stream (Easy)
# Design a class to find the kth largest integer in a stream of values,
# including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The
# stream is not necessarily sorted.
# 
# Implement the following methods:
# - constructor(int k, int[] nums) Initializes the object given an integer k
#   and the stream of integers nums.
# 
# - int add(int val) Adds the integer val to the stream and returns the kth
#   largest integer in the stream

from heapq import *

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.streamBuffer = []

        for num in nums:
            self.add(num)

    def add(self, val):
        heappush(self.streamBuffer, val)

        if len(self.streamBuffer) < self.k:
            return None
        
        if len(self.streamBuffer) > self.k:
            heappop(self.streamBuffer)

        return self.streamBuffer[0]

if __name__ == "__main__":
    # Example 1
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print(kthLargest.add(3), 3)
    print(kthLargest.add(5), 3)
    print(kthLargest.add(6), 3)
    print(kthLargest.add(7), 5)
    print(kthLargest.add(8), 6)

    print()

    # Example 2
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3),  4)
    print(kthLargest.add(5),  5)
    print(kthLargest.add(10), 5)
    print(kthLargest.add(9),  8)
    print(kthLargest.add(4),  8)

