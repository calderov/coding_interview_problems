# Jump game II
# https://neetcode.io/problems/jump-game-ii
#
# You are given an array of integers nums, where nums[i] represents the
# maximum length of a jump towards the right from index i. For example, if
# you are at nums[i], you can jump to any index i + j where:
# 
# j <= nums[i]
# i + j < nums.length
# You are initially positioned at nums[0].
# 
# Return the minimum number of jumps to reach the last position in the array
# (index nums.length - 1). You may assume there is always a valid answer.
# 
# Example 1:
# 
# Input: nums = [2,4,1,1,1,1]
# 
# Output: 2


from collections import deque

class Solution:
    def jump(self, nums: list[int]) -> int:
        level = 0
        pending = deque([(0, nums[0])])

        while pending:
            nodesInLevel = len(pending)
            level += 1
            for _ in range(nodesInLevel):
                index, maxJump = pending.popleft()

                if index == len(nums) - 1:
                    return level - 1

                for jump in range(maxJump, 0, -1):
                    nextIndex = index + jump

                    if nextIndex < len(nums):
                        pending.append((nextIndex, nums[nextIndex]))

        return level - 1
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [2,4,1,1,1,1]
    expectedOutput = 2
    output = solution.jump(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [2,1,2,1,0]
    expectedOutput = 2
    output = solution.jump(nums)
    print(output, expectedOutput, output == expectedOutput)