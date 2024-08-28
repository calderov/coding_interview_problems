from collections import deque

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        pending = deque([(0, nums[0])])

        while pending:
            index, maxJump = pending.popleft()

            if index == len(nums) - 1:
                return True

            for jump in range(maxJump, 0, -1):
                nextIndex = index + jump

                if nextIndex >= len(nums):
                    continue

                pending.append((nextIndex, nums[nextIndex]))

        return False
    

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1,2,0,1,0]
    expectedOutput = True
    output = solution.canJump(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1,2,1,0,1]
    expectedOutput = False
    output = solution.canJump(nums)
    print(output, expectedOutput, output == expectedOutput)