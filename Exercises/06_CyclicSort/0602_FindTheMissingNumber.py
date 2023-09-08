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
    # 1. Make a set out of all the numbers from 0 to n where n = len(nums) + 1.
    # 
    # 2. Make a set ouf of all the numbers in the nums array.
    #
    # 3. Compute the difference between the set with all the numbers from 0 to n,
    #    and the set with all the numbers in nums.
    # 
    # 4. The resulting set should have a single member, the missing number.
    # 
    # 5. Return the missing number.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def FindMissingNumberV1(self, nums):
        return set([i for i in range(len(nums) + 1)]).difference(set(nums)).pop()

    # Solution:
    # 1. Initialize an index i = 0.
    #
    # 2. While i < len(nums), check if nums[i] < len(nums) and nums[i] != nums[nums[i]]
    #    this is, check if the number pointed by i in nums is less than the length of nums
    #    (thus is subject to serve as an index later on), and if the number pointed by i
    #    in nums is out of its correct place. If this is the case, swap the values at
    #    nums[i] and nums[nums[i]] and continue. Otherwise, increment i by 1.
    #
    # 3. Once the while loop in step 2 is finished, the nums array should be in a
    #    semisorted state.
    #
    #    Use a for loop to traverse the nums array from 0 to len(nums).
    #    If there is an i such that nums[i] != i, then i is the missing number,
    #    return it and finish. Otherwise, the array is completely sorted, meaning
    #    that the missing number is n. Since n = len(nums) by definition, return it
    #    and finish.  
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

