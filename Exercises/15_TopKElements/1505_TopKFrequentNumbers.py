# Problem:
# Given an unsorted array of numbers, find the top ‘K’ frequently occurring
# numbers in it.
#
# Examples:
#
#   Input: [1, 3, 5, 12, 11, 12, 11], K = 2
#   Output: [12, 11]
#   Explanation: Both '11' and '12' apeared twice.
#
#   Input: [5, 12, 11, 3, 11], K = 2
#   Output: [11, 5] or [11, 12] or [11, 3]
#   Explanation: Only '11' appeared twice, all other numbers appeared once.
#

from heapq import *

class Solution:
    # Solution:
    # 1. Use a hash map to track the frequency of each number in the input array.
    #
    # 2. For each number in the frequencies map.
    #
    # 3. Insert the number and its frequency into the min heap (the min heap should minimize based on the frequency).
    #
    # 4. If the length of the min heap is greater than k, pop the top out (that would correspond with the number with
    #    the lowest frequency in the heap).
    #
    # 5. Extract the numbers from the min heap and save them to a list (these are the top k most frequent numbers).
    #
    # 6. Sort the top k list (optional).
    #
    # 7. Return the top k list of most frequent numbers.
    #
    # Solution complexity:
    # Time complexity: O(n + n log(k))
    # Space complexity: O(n)
    def GetTopKFrequentNumbers(self, nums, k):
        # Use a hash map to track the frequency of each number in the input array
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 0
            frequencies[num] += 1

        # For each number in the frequencies map
        minHeap = []
        for num, freq in frequencies.items():
            # Insert the number and its frequency into the min heap (the min heap should minimize based on the frequency)
            heappush(minHeap, (freq, num))

            # If the length of the min heap is greater than k, pop the top out (that would correspond with the number with
            # the lowest frequency in the heap)
            if len(minHeap) > k:
                heappop(minHeap)

        # Extract the numbers from the min heap and save them to a list (these are the top k most frequent numbers)
        topK = [i[1] for i in minHeap]

        # Sort the top k list (optional)
        topK.sort()

        # Return the top k list of most frequent numbers
        return topK

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 3, 5, 12, 11, 12, 11]
    k = 2
    expectedOutput = [11, 12]
    output = solution.GetTopKFrequentNumbers(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [5, 12, 11, 3, 11]
    k = 2
    expectedOutput = [[3, 11], [5, 11], [11, 12], ]
    output = solution.GetTopKFrequentNumbers(nums, k)
    print(output, expectedOutput, output in expectedOutput)
