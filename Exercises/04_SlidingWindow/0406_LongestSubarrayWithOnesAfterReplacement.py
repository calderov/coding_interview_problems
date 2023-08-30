# Problem:
# Given an array containing 0s and 1s, if you are allowed to replace no more
# than 'k' 0s with 1s, find the length of the longest contiguous subarray
# having all 1s.
# 
# Example 1:
# 
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2  
# Output: 6  
# Explanation: Replace the '0' at index 5 and 8 to have the longest
# contiguous subarray of 1s having length 6.
# 
# Example 2:
# 
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3  
# Output: 9  
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest
# contiguous subarray of 1s having length 9.
# 

class Solution:
    # Solution:
    #
    # 1. Initialize a variable to keep track of the length of the longest subarray
    #    that matches our criteria maxLengthAfterReplace = 0.
    # 
    # 2. Initialize a couple of pointers to mark the start and the end of the sliding
    #    window that delimits our explored subarrays.
    #    start = 0
    #    end = 0
    # 
    # 3. Initialize a frequency map (dictionary) to track the amount of 0s and 1s present
    #    in the subarray induced by the sliding window.
    #     freqMap = {0:0, 1:0}
    #
    # 3. While the end of the sliding window is within the limits of the input array (nums),
    #    take the number pointed by end and add 1 to its frequency.
    #      freqMap[nums[end]] += 1
    #
    # 4. If the amount of zeros in the subarray (thus, registered in the frequency map) is
    #    lesser than or equal to k, it means the subarray matches our criteria. Check if
    #    the subarray is longer than maxLengthAfterReplace, if so, update maxLengthAfterReplace
    #    with the length of the subarray (end - start + 1).
    #
    # 5. If the amount of zeros in the subarray is greater than k, substract 1 from the frequency
    #    of nums[start] and add 1 to start. Do this while the frequency of zero is greater
    #    than k. In other words, shrink the sliding window until you have dropped enough
    #    zeros, so our subarray is once again able to be made of just ones after at most
    #    k replacements.
    # 
    # 6. Move the end of the sliding window one position to the right. If end < len(inputString)
    #    go back to step 3. Otherwise, return maxLengthAfterReplace and finish.
    #
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def Solve(self, nums, k):
        maxSubarrayOfOnesLength = 0
        start = 0
        end = 0

        frequencyMap = {0:0, 1:0}
        
        while end < len(nums):
            frequencyMap[nums[end]] += 1
            
            if frequencyMap[0] <= k:
                maxSubarrayOfOnesLength = max(maxSubarrayOfOnesLength, end - start + 1)
            else:
                while frequencyMap[0] > k:
                    frequencyMap[nums[start]] -= 1
                    start += 1
            end += 1

        return maxSubarrayOfOnesLength

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    k = 2
    expectedOutput = 6
    output = solution.Solve(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2:
    nums = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    k = 3
    expectedOutput = 9
    output = solution.Solve(nums, k)
    print(output, expectedOutput, output == expectedOutput)
