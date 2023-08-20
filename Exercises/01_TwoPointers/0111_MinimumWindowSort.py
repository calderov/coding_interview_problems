# Problem:
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
# 
# Example 1:
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# 
# Example 2:
# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

class Solution:
    # Solution 1:
    # Brute force, generate all the possible subarrays and evaluate them keeping track of the smallest one that will sort the whole array.
    #
    # Solution 1 complexity:
    # Time complexity: O(n^3) as three nested loops are used to check all possible subarrays and evaluate them as sorted.
    # Space complexity: O(n) as the largest subarray is potentially as long as the original array.
    def MinimumWindowSortV1(self, nums):
        n = len(nums)

        if self.IsSorted(nums):
            return 0
        
        minSubarrayLength = n
        for i in range(n):
            for j in range(i, n + 1):
                subarray = nums[i:j]
                if self.IsSorted(nums[0:i] + sorted(subarray) + nums[j:n]):
                    if len(subarray) < minSubarrayLength:
                        minSubarrayLength = len(subarray)

        return minSubarrayLength

    def IsSorted(self, nums):
        n = len(nums)
        for i in range(n - 1):
            if not nums[i] <= nums[i + 1]:
                return False
        return True

    # Solution 2:
    # Use two pointers to find the unsorted segment. These pointers will be called
    # low and high and our goal will be for them to point to the beginning and the 
    # end of the subarray that needs to be sorted to make the original array sorted
    # as well.
    # 
    # Start by initializing low and high at the extremes of the original array:
    # low = 0
    # high = n - 1 (where n is the length of the nums array)
    #
    # Now move low from left to right of the original array until it finds an item
    # out of order. If low reaches the end of the original array without finding
    # items out of order, it means that the array is already sorted, return 0 if
    # this is the case as the subarray that needs to be sorted is empty.
    # 
    # Analogously, move high from right to left of the original array until it
    # finds an item out of order.
    #
    # Now high and low sit at the edges of a subarray containing items that make
    # the original array unsorted. Since a sorted array would have its minimum
    # element at the beginning and the maximim at its end, then lets use this
    # fact to or advantage. Find the minimum and maximum elements contained
    # between low and high and save them to their respective variables E.g.
    # minSubarray and maxSubarray.
    #
    # Then, move low to the left until all the items greater than minSubarray
    # are reached or low reaches zero. Similarly, move high to the right until
    # all the items lower than maxSubarray are reached or high reaches the
    # last position of the array.
    #
    # At this point, low and high are at the edges of the minimum subarray
    # that needs to be sorted to sort the original array, its length
    # should be high - low + 1. Thus return high - low + 1

    # Solution 2 complexity:
    # Time complexity: O(n) linear.
    # Space complexity: O(1) constant.
    def MinimumWindowSortV2(self, nums):
        n = len(nums)

        # Find the last ordered item from left to right
        low = 0
        while low < n - 1 and nums[low] <= nums[low + 1]:
            low += 1
        
        # Return early if the array is sorted
        if low == n - 1:
            return 0

        # Find the last ordered item from right to left
        high = n - 1
        while high > 0 and nums[high] >= nums[high - 1]:
            high -= 1

        # Find min and max elements between i and j
        minInSubarray = nums[low]
        maxInSubarray = nums[low]
        for k in range(low, high + 1):
            minInSubarray = min(minInSubarray, nums[k])
            maxInSubarray = max(maxInSubarray, nums[k])

        # Extend the range of the subarray to the left to include any number bigger than the minimum in the subarray
        while low > 0 and nums[low - 1] > minInSubarray:
            low -= 1

        # Extend the subarray to the right to include any number smaller than the maximum in the subarray
        while high < n - 1 and nums[high + 1] < maxInSubarray:
            high += 1

        return high - low + 1

    def MinimumWindowSort(self, nums):
        return self.MinimumWindowSortV2(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 2, 5, 3, 7, 10, 9, 12]
    expectedOutput = 5
    output = solution.MinimumWindowSort(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 3, 2, 0, -1, 7, 10]
    expectedOutput = 5
    output = solution.MinimumWindowSort(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 2, 3]
    expectedOutput = 0
    output = solution.MinimumWindowSort(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = [3, 2, 1]
    expectedOutput = 3
    output = solution.MinimumWindowSort(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5
    nums = [2, 3, 3, 2]
    expectedOutput = 3
    output = solution.MinimumWindowSort(nums)
    print(output, expectedOutput, output == expectedOutput)
