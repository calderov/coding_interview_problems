# Find the Missing Number (easy)
# Problem Statement
# 
# We are given an array containing n distinct numbers taken from the range 0
# to n. Since the array has only n numbers out of the total n+1 numbers, find
# the missing number.
# 
# Examples:
# 
#   Input: [4, 0, 3, 1]
#   Output: 2
# 
#   Input: [8, 3, 5, 2, 4, 6, 0, 1]
#   Output: 7

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def FindMissingNumberV1(self, nums):
        return set([i for i in range(len(nums) + 1)]).difference(set(nums)).pop()

    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def FindMissingNumberV2(self, nums):
        i = 0

        # Sort using cyclic sort
        while i < len(nums):
            if nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i] 
                continue
            i += 1

        # Find the missing number
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
            

    def FindMissingNumber(self, nums):
        return self.FindMissingNumberV2(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [4, 0, 3, 1]
    expectedOutput = 2
    output = solution.FindMissingNumber(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [8, 3, 5, 2, 4, 6, 0, 1]
    expectedOutput = 7
    output = solution.FindMissingNumber(nums)
    print(output, expectedOutput, output == expectedOutput)

