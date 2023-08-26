# Problem Statement
# Given an array of positive numbers and a positive number 'k,' find
# the maximum sum of any contiguous subarray of size 'k'.
#
# Example:
#  Input: [2, 1, 5, 1, 3, 2], k=3 
#  Output: 9
#  Explanation: Subarray with maximum sum is [5, 1, 3].

class Solution:
    # Solution:
    # 1. Set two pointers to delimit a sliding window on the array.
    #    The first will mark the start of the sliding window and the
    #    second will mark its end. They should be initialized as
    #    0 and k - 1 respectively.
    #
    # 2. Declare two auxiliar variables, windowSum and maxWindowSum,
    #    the first will contain the sum of all the elements contained
    #    in the current window, and the second will track the maximum
    #    window sum found so far.
    #
    # 2. While the end of the sliding window is less than the length
    #    of the array, check if the start value is zero.
    # 
    # 3. If start equals zero, it means that we have not computed any
    #    windowSum yet. Sum the first k elements on the array and save
    #    the value to windowSum and maxWindowSum.
    #
    # 4. If the start is not equal to zero, it means that we have an
    #    existing windowSum and maxWindowSum. Update windowSum by 
    #    substracting the previous start value and adding the current
    #    end value. In other words:
    #        windowSum = windowSum - arr[start - 1] + arr[end]
    #
    # 5. Check if windowSum is greater than maxWindowSum, 
    #    if so, update maxWindowSum.
    #
    # 6. Once the array has been traversed, return maxWindowSum.
    # 
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindMaxSumSubarray(self, nums, k):
        start = 0
        end = k - 1
        windowSum = 0
        maxWindowSum = 0
        
        while end < len(nums):
            if start == 0:
                windowSum = sum(nums[0 : k])
                maxWindowSum = windowSum
            else:
                windowSum -= nums[start - 1]
                windowSum += nums[end]
            
            if windowSum > maxWindowSum:
                maxWindowSum = windowSum

            start += 1
            end += 1

        return maxWindowSum

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [2, 1, 5, 1, 3, 2]
    k = 3 
    expectedOutput = 9
    output = solution.FindMaxSumSubarray(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [2, 3, 4, 1, 5]
    k = 2 
    expectedOutput = 7
    output = solution.FindMaxSumSubarray(nums, k)
    print(output, expectedOutput, output == expectedOutput)
