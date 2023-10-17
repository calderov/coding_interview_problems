# Problem: 
# Given an array of numbers sorted in ascending order, find the element in
# the array that has the minimum difference with the given ‘key’.
# 
# Example:
# 
#   Input: [4, 6, 10], key = 7
#   Output: 6
#   Explanation: The difference between the key '7' and '6' is minimum than any
#   other number in the array 
# 

class Solution:
    # Solution:
    # Use a regular binary search but keep track of the element with the lowest difference from the key
    # while the nums array is being traversed.
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def MinimumDifferenceElement(self, nums, key):
        left = 0
        right = len(nums) - 1

        minDiffElement = nums[0]
        minDiff = abs(minDiffElement - key)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == key:
                return key
            
            if nums[mid] < key:
                left = mid + 1

            else: # nums[mid] > key:
                right = mid - 1

            # Update min difference element
            diff = abs(nums[mid] - key)
            
            if diff < minDiff:
                minDiff = diff
                minDiffElement = nums[mid]
                continue
            
            if diff == minDiff:
                minDiffElement = min(minDiffElement, nums[mid])

        return minDiffElement

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [4, 6, 10]
    key = 7
    expectedOutput = 6
    output = solution.MinimumDifferenceElement(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [4, 6, 10]
    key = 4
    expectedOutput = 4
    output = solution.MinimumDifferenceElement(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 3, 8, 10, 15]
    key = 12
    expectedOutput = 10
    output = solution.MinimumDifferenceElement(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = [4, 6, 10]
    key = 17
    expectedOutput = 10
    output = solution.MinimumDifferenceElement(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5
    nums = [100, 200, 300, 400, 500]
    key = 250
    expectedOutput = 200
    output = solution.MinimumDifferenceElement(nums, key)
    print(output, expectedOutput, output == expectedOutput)