# Problem:
# Given an integer array nums and an integer k, return true if there are two
# distinct indices i and j in the array such that nums[i] == nums[j] and
# abs(i - j) <= k.
# 
# Examples:
# 
#   Input: nums = [1,2,3,1], k = 3
#   Output: true
# 
#   Input: nums = [1,0,1,1], k = 1
#   Output: true
# 
#   Input: nums = [1,2,3,1,2,3], k = 2
#   Output: false
#  

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def ContainsDuplicateAtMostKCharsAppart(self, nums, k):
        indexMap = {}
        n = len(nums)

        for i in range(n):
            if nums[i] in indexMap:
                if i - indexMap[nums[i]] <= k:
                    return True

            indexMap[nums[i]] = i

        return False

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1,2,3,1]
    k = 3
    expectedOutput = True
    output = solution.ContainsDuplicateAtMostKCharsAppart(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [1,0,1,1]
    k = 1
    expectedOutput = True
    output = solution.ContainsDuplicateAtMostKCharsAppart(nums, k)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    nums = [1,2,3,1,2,3]
    k = 2
    expectedOutput = False
    output = solution.ContainsDuplicateAtMostKCharsAppart(nums, k)
    print(output, expectedOutput, output == expectedOutput)