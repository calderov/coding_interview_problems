# Problem:
# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest
# numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is
# not necessarily present in the array.
# 
# Examples:
# 
#   Input: [5, 6, 7, 8, 9], K = 3, X = 7
#   Output: [6, 7, 8]
# 
#   Input: [2, 4, 5, 6, 9], K = 3, X = 6
#   Output: [4, 5, 6]
# 

from heapq import *

class Solution:
    # Solution:
    # Traverse the input array and store the numbers in it into a max heap where the maximization criteria
    # is the distance from the given number x. Ensure this max heap keeps at most k elements at all times
    # by popping elements until its length is at most k if it ever exeeds this limit.
    # Make a list of the numbers in the max heap and return them in a sorted order.
    #
    # Solution complexity:
    # Time complexity: O(n log(k))
    # Space complexity: O(n)
    def KClosestNumbers(self, nums, k, x):
        maxHeap = []

        for num in nums:
            distance = abs(num - x)
            
            # If two numbers are at the same distance from X and k == 1, skip the largest one
            if k == 1 and maxHeap and -distance == maxHeap[0][0] and num > maxHeap[0][1]:
                continue

            heappush(maxHeap, (-distance, num))

            if len(maxHeap) > k:
                heappop(maxHeap)

        kClosest = [item[1] for item in maxHeap]
        kClosest.sort()

        return kClosest

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [5, 6, 7, 8, 9]
    k = 3
    x = 7
    expectedOutput = [6, 7, 8]
    output = solution.KClosestNumbers(nums, k, x)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [2, 4, 5, 6, 9]
    k = 3
    x = 6
    expectedOutput = [4, 5, 6]
    output = solution.KClosestNumbers(nums, k, x)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
 
    # Example 3
    nums = [2, 4, 5, 6, 9]
    k = 3
    x = 10
    expectedOutput = [5, 6, 9]
    output = solution.KClosestNumbers(nums, k, x)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 4
    nums = [1,3,5,7,9]
    k = 2
    x = 6
    expectedOutput = [5]
    output = solution.KClosestNumbers(nums, k, x)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()