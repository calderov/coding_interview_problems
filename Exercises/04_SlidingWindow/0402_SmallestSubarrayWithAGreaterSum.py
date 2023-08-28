# Problem:
# Given an array of positive integers and a number S, find the length of the
# smallest contiguous subarray whose sum is greater than or equal to S.
# Return 0 if no such subarray exists.
#
# Examples:
#
# Input: [2, 1, 5, 2, 3, 2], S = 7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to 7 is [5, 2].
#
# Input: [2, 1, 5, 2, 8], S = 7
# Output: 1 
# Explanation: The smallest subarray with a sum greater than or equal to 7 is [8].
#
# Input: [3, 4, 1, 1, 6], S = 8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to 8 are [3, 4, 1] or [1, 1, 6].

class Solution:
    # Solution:
    # 1. Start by assuming that there is no subarray which sum is greater than or equal to S
    #    by initializing a variable named minWindowLength as follows:
    #    minWindowLength = len(nums) + 1
    # 
    # 2. Initialize a variable to keep track of the sliding window sum as well as two pointers
    #    that will delimit the window:
    #    windowSum = 0
    #    start = 0    
    #    end = 0    
    # 
    # 3. Use a while loop to move the end pointer to accross the array adding nums[end] to 
    #    windowSum in each iteration.
    # 
    # 4. If at any point windowSum >= S, it means that we have found a window that meets our
    #    desired criteria. Check if the size of the window is less than minWindowLength.
    #    If so, update minWindowLenght (remember that the window length is computed as
    #    windowLength = end - start + 1).
    # 
    #    Now, try reducing the window length by moving the start pointer across the array
    #    and substracting nums[start] from windowSum and updating the window length
    #    until windowSum is no longer greater or equal to S. Do this using a nested
    #    while loop.
    # 
    # 5. Once the end pointer has completely traversed the array check  (thus breaking
    #    the main loop). Check if minWindowLength is still equal to len(nums) + 1.
    #    If so, it means that we never found a subarray (window) which added to a
    #    sum greater than or equal to S. In this case, return 0. Otherwise, return
    #    minWindowLength. 
    #    
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindMinSubArray(self, nums, s):
        minWindowLength = len(nums) + 1
        windowSum = 0
        start = 0
        end = 0

        while end < len(nums):
            windowSum += nums[end]
            while windowSum >= s:
                minWindowLength = min(minWindowLength, end - start + 1)
                windowSum -= nums[start]
                start += 1
            end += 1

        if minWindowLength == len(nums) + 1:
            return 0

        return minWindowLength

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [2, 1, 5, 2, 3, 2]
    s = 7
    expectedOutput = 2
    output = solution.FindMinSubArray(nums, s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [2, 1, 5, 2, 8]
    s = 7
    expectedOutput = 1 
    output = solution.FindMinSubArray(nums, s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [3, 4, 1, 1, 6]
    s = 8
    expectedOutput = 3
    output = solution.FindMinSubArray(nums, s)
    print(output, expectedOutput, output == expectedOutput)
