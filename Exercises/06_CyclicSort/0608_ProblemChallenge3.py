# Problem:
# Given an unsorted array containing numbers and a number k, find the first
# k missing positive numbers in the array.
#
# Examples:
#
#   Input: [3, -1, 4, 5, 5], k=3
#   Output: [1, 2, 6]
#   Explanation: The smallest missing positive numbers are 1, 2 and 6.
#
#   Input: [2, 3, 4], k=3
#   Output: [1, 5, 6]
#   Explanation: The smallest missing positive numbers are 1, 5 and 6.
#
#   Input: [-2, -3, 4], k=2
#   Output: [1, 2]
#   Explanation: The smallest missing positive numbers are 1 and 2.

class Solution:
    # Solution:
    # 1. Remove the zero and duplicate values from the input array nums.
    #
    # 2. Sort the remaining values on nums (ascending).
    #
    # 3. Initialize an empty array to store the missing numbers.
    #      missingNumbers = []
    #
    # 4. Initialize a pair of variables. The first one being an index i
    #    pointing to the first element of the nums array, while the
    #    second is meant to store the expected value at the given index.
    #      i = 0
    #      expected = 1
    #
    # 5. While k > 0, check if the value at index i satisfies these two conditions:
    #      a) The nums value at the index i is less than the length of the nums array.
    #      b) The nums value at the index i is the same as the expected.
    #
    #    If both conditions are satisfied, increase the value of i and expected by one,
    #    and continue to the next iteration.
    #
    #    Otherwise, add expected to the missingNumbers array, increment expected by one
    #    and decrement k by one.
    #
    # 6. Return missingNumbers and finish.
    #
    # Solution complexity:
    # Time complexity: O(n log(n))
    # Space complexity: O(n)
    def FindKMissingNumbers(self, nums, k):
        # Remove negatives, duplicates and zero
        nums = list(set([i for i in nums if i > 0]))

        # Sort nums
        nums.sort()

        # Initialize missing numbers array
        missingNumbers = []

        i = 0
        expected = 1

        while k > 0:
            if i < len(nums) and nums[i] == expected:
                i += 1
                expected += 1
                continue

            missingNumbers.append(expected)
            expected += 1
            k -= 1

        # Return missing numbesr array
        return missingNumbers

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3, -1, 4, 5, 5]
    k = 3
    expectedOutput = [1, 2, 6]
    output = solution.FindKMissingNumbers(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [2, 3, 4]
    k = 3
    expectedOutput = [1, 5, 6]
    output = solution.FindKMissingNumbers(nums, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [-2, -3, 4]
    k = 2
    expectedOutput = [1, 2]
    output = solution.FindKMissingNumbers(nums, k)
    print(output, expectedOutput, output == expectedOutput)
