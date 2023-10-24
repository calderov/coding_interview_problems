# Problem:
# In a non-empty array of integers, every number appears twice except for
# one, find that single number.
# 
# Examples:
# 
#   Input: 1, 4, 2, 1, 3, 2, 3
#   Output: 4
# 
#   Input: 7, 9, 7
#   Output: 9
# 

class Solution:
    # Solution:
    # XOR all the items in the input array, since each item in the array is repeated
    # except for the singular number we are looking for, # those with repetitions will
    # cancel out, leaving just the singular number as result.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindSingleNumber(self, nums):
        n = len(nums)
        
        single = nums[0]
        for i in range(1, n):
            single = single ^ nums[i]

        return single

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [1, 4, 2, 1, 3, 2, 3]
    expectedOutput = 4
    output = solution.FindSingleNumber(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    nums = [7, 9, 7]
    expectedOutput = 9
    output = solution.FindSingleNumber(nums)
    print(output, expectedOutput, output == expectedOutput)
