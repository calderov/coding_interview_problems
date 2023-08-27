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
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindMinSubArray(self, nums, s):
        windowSum = 0
        minWindowLength = len(nums) + 1

        start = 0
        for end in range(len(nums)):
            windowSum += nums[end]
            while windowSum >= s:
                minWindowLength = min(minWindowLength, end - start + 1)
                windowSum -= nums[start]
                start += 1

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
