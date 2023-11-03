# Problem:
# Given ‘M’ sorted arrays, find the smallest range that includes at least one
# number from each of the ‘M’ lists.
# 
# Examples:
# 
#   Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
#   Output: [4, 7]
#   Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.
# 
#   Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
#   Output: [9, 12]
#   Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3
# 

import math
from heapq import *

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(N log(M))
    # Space complexity: O(M)
    def SmallestNumberRange(self, lists):
        minHeap = []
        rangeMin = 0
        rangeMax = math.inf
        currentMax = -math.inf

        for _list in lists:
            heappush(minHeap, (_list[0], 0, _list))
            currentMax = max(currentMax, _list[0])

        while len(minHeap) == len(lists):
            number, i, _list = heappop(minHeap)

            if rangeMax - rangeMin > currentMax - number:
                rangeMin = number
                rangeMax = currentMax

            if len(_list) > i + 1:
                heappush(minHeap, (_list[ i + 1], i + 1, _list))
                currentMax = max(currentMax, _list[i + 1])

        return [rangeMin, rangeMax]


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    lists = [[1, 5, 8], [4, 12], [7, 8, 10]]
    expectedOutput = [4, 7]
    output = solution.SmallestNumberRange(lists)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    lists = [[1, 9], [4, 12], [7, 10, 16]]
    expectedOutput = [9, 12]
    output = solution.SmallestNumberRange(lists)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
