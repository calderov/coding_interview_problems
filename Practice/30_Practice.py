# 179. Largest Number (Medium)
# Given a list of non-negative integers nums, arrange them such that they
# form the largest number and return it.
# 
# Since the result may be very large, so you need to return a string instead
# of an integer.
# 
# Example 1:
#   Input: nums = [10,2]
#   Output: "210"
# 
# Example 2:
#   Input: nums = [3,30,34,5,9]
#   Output: "9534330"
# 
# Constraints:
#   1 <= nums.length <= 100
#   0 <= nums[i] <= 109

class CustomKey(str):
    def __lt__(x, y):
        return x + y > y + x

class Solution:
    # Time complexity: O(n log n)
    # Space complexity: O(n)
    def largestNumber(self, nums):
        numsStr = [str(num) for num in nums]
        numsStr.sort(key=CustomKey)

        largest = ''.join(numsStr)

        if largest[0] == '0':
            return '0'

        return largest

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    nums = [10,2]
    expectedOutput = "210"
    output = solution.largestNumber(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2:
    nums = [3,30,34,5,9]
    expectedOutput = "9534330"
    output = solution.largestNumber(nums)
    print(output, expectedOutput, output == expectedOutput)
     