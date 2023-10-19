# Problem:
# Find the maximum value in a given Bitonic array. An array is considered
# bitonic if it is monotonically increasing and then monotonically
# decreasing. Monotonically increasing or decreasing means that for any index
# i in the array arr[i] != arr[i+1].
# 
# Example:
# 
#   Input: [1, 3, 8, 12, 4, 2]
#   Output: 12
#   Explanation: The maximum number in the input bitonic array is '12'.
# 

class Solution:
    # Solution:
    # 1. Initialize 'left' and 'right' pointers.
    #    left = 0
    #    right = n - 1 
    #
    # 2. Initialize maxValue variable to keep track of the largest value found so far.
    #    maxValue = fist element in input array
    #
    # 3. While 'left' is less than 'right'
    #
    #   3.1 Compute the 'middle' pointer (that between 'left' and 'right').
    #
    #   3.2 If we are in the ascending section, compare maxValue against nums['middle' + 1] and update it if necessary.
    #       Then, move 'left' one position to the right of 'middle'
    #
    #      Otherwise, we are in the descending section. Compare maxValue against nums['middle'] and update it if necessary
    #      and move 'right' up to 'middle'.
    #
    # 4. Return maxValue and finish.
    # 
    # Solution complexity:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def FindMaxValue(self, nums):
        # Initialize 'left' and 'right' pointers
        left = 0
        right = len(nums) - 1

        # Initialize maxValue variable to keep track of the largest value found so far
        maxValue = nums[0]

        # While 'left' is less than 'right'
        while left < right:
            # Compute the 'middle' pointer (that between 'left' and 'right')
            mid = (left + right) // 2

            # If we are in the ascending section, compare maxValue against nums['middle' + 1] and update it if necessary
            # then move 'left' one position to the right of 'middle'
            if nums[mid] < nums[mid + 1]:
                maxValue = max(maxValue, nums[mid + 1])
                left = mid + 1
        
            # Otherwise, we are in the descending section. Compare maxValue against nums['middle'] and update it if necessary
            # then move 'right' up to 'middle'
            else: # nums[mid] > nums[mid + 1]
                maxValue = max(maxValue, nums[mid])
                right = mid

        # Return maxValue and finish
        return maxValue

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 3, 8, 12, 4, 2]
    expectedOutput = 12
    output = solution.FindMaxValue(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [3, 8, 3, 1]
    expectedOutput = 8
    output = solution.FindMaxValue(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    nums = [1, 3, 8, 12]
    expectedOutput = 12
    output = solution.FindMaxValue(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 4
    nums = [10, 9, 8]
    expectedOutput = 10
    output = solution.FindMaxValue(nums)
    print(output, expectedOutput, output == expectedOutput)
    