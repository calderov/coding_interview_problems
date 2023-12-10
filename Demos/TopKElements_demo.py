from heapq import *

def TopKElements(nums, k):
    if k > len(nums):
        return None

    maxHeap = [-num for num in nums]
    heapify(maxHeap)

    return [-heappop(maxHeap) for i in range(k)]

if __name__ == "__main__":
    nums = [1, 5, 4, 2, 7, 3, 10, 8, 9, 6]
    k = 4
    expectedOutput = [10, 9, 8, 7]
    output = TopKElements(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)