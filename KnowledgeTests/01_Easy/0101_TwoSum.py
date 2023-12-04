# Problem:
# 
# You are given an array of integers nums and an integer target. Your task is
# to find two distinct indices i and j such that the sum of nums[i] and
# nums[j] is equal to the target. You can assume that each input will have
# exactly one solution, and you may not use the same element twice.
# Examples
# 
#     Example 1:
#         Input: [3, 2, 4], 6
#         Expected Output: [1, 2]
#         Justification: nums[1] + nums[2] gives 2 + 4 which equals 6.
# 
#     Example 2:
#         Input: [-1, -2, -3, -4, -5], -8
#         Expected Output: [2, 4]
#         Justification: nums[2] + nums[4] yields -3 + (-5) which equals -8.
# 
#     Example 3:
#         Input: [10, 15, 20, 25, 30], 45
#         Expected Output: [1, 4]
#         Justification: nums[1] + nums[3] gives 15 + 30 which equals 45.
# 

class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(1) 
    def FindSumIndexes(self, nums, target):
        n = len(nums)

        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]

        return None

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [3, 2, 4]
    target = 6
    expectedOutput = [1, 2]
    output = solution.FindSumIndexes(nums, target)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    nums = [-1, -2, -3, -4, -5]
    target = -8
    expectedOutput = [2, 4]
    output = solution.FindSumIndexes(nums, target)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3:
    nums = [10, 15, 20, 25, 30]
    target = 45
    expectedOutput = [1, 4]
    output = solution.FindSumIndexes(nums, target)
    print(output, expectedOutput, output == expectedOutput)
