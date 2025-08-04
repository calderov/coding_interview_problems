# QHEAP1
# https://www.hackerrank.com/challenges/qheap1/problem
#
# Implement a min heap such that every item in the heap is unique
# and allows for the following operations:
#
#   push(value): Adds the given value to the heap
#
#   delete(value): Deletes the given value from the heap
#
#   peek(): Returns the item at the top of the heap (the min value in the heap)
#
#   printMin(): Prints the min value in the heap

from heapq import *

class QHeap1:
    def __init__(self):
        self.minHeap = []
        self.deleted = set()

    def push(self, value):
        heappush(self.minHeap, value)
        self.deleted.discard(value)

    def delete(self, value):
        self.deleted.add(value)

    def peek(self):
        if not self.minHeap:
            return None

        while self.minHeap:
            item = self.minHeap[0]

            if item in self.deleted:
                self.deleted.discard(item)
                while self.minHeap and item == self.minHeap[0]:
                    heappop(self.minHeap)
            else:
                return item

        return None
        
    def printMin(self):
        print(self.peek())

if __name__ == "__main__":
    heap = QHeap1()
    output = []
    expected = [
        255653921,
        274310529,
        20842598,
        -51159108,
        20842598
    ]

    heap.push(286789035)
    heap.push(255653921)
    heap.push(274310529)
    heap.push(494521015)
    output.append(heap.peek())
    heap.delete(255653921)
    heap.delete(286789035)
    output.append(heap.peek())
    heap.push(236295092)
    heap.push(254828111)
    heap.delete(254828111)
    heap.push(465995753)
    heap.push(85886315)
    heap.push(7959587)
    heap.push(20842598)
    heap.delete(7959587)
    output.append(heap.peek())
    heap.push(-51159108)
    output.append(heap.peek())
    heap.delete(-51159108)
    output.append(heap.peek())
    heap.push(789534713)

    print(expected)
    print(output)
    print(output == expected)