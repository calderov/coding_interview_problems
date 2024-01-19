# Problem:
# Given an array of integers, return a new array where each element at index
# i of the new array is the product of all the numbers in the original array
# except the one at i. You must solve this problem without using division.
# 
# Examples:
# 
#   Input: [2, 3, 4, 5]
#   Expected Output: [60, 40, 30, 24]
#   Justification: For the first element: 3*4*5 = 60, for the second element:
#   2*4*5 = 40, for the third element: 2*3*5 = 30, and for the fourth element:
#   2*3*4 = 24.
# 
#   Input: [1, 1, 1, 1]
#   Expected Output: [1, 1, 1, 1]
#   Justification: Every element is 1, so the product of all other numbers for
#   each index is also 1.
# 
#   Input: [10, 20, 30, 40]
#   Expected Output: [24000, 12000, 8000, 6000]
#   Justification: For the first element: 20*30*40 = 24000, for the second
#   element: 10*30*40 = 12000, for the third element: 10*20*40 = 8000, and for
#   the fourth element: 10*20*30 = 6000.

class Solution:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def GetProductsExceptFromSelf(self, nums):
        products = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    products[i] *= nums[j]

        return products

    # Time complexity: O(n)
    # Space complexity: O(n)
    def GetProductsExceptFromSelfV2(self, nums):
        productsLeft = [1] * len(nums)
        productsRight = [1] * len(nums)

        for i in range(1, len(nums)):
            productsLeft[i] = nums[i - 1] * productsLeft[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            productsRight[i] = nums[i + 1] * productsRight[i + 1]

        products = [productsLeft[i] * productsRight[i] for i in range(len(nums))]

        return products

if __name__ == "__main__":
    solution = Solution()

    nums = [2, 3, 4, 5]
    expectedOutput = [60, 40, 30, 24]
    output = solution.GetProductsExceptFromSelfV2(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    nums = [1, 1, 1, 1]
    expectedOutput = [1, 1, 1, 1]
    output = solution.GetProductsExceptFromSelfV2(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
 
    nums = [10, 20, 30, 40]
    expectedOutput = [24000, 12000, 8000, 6000]
    output = solution.GetProductsExceptFromSelfV2(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()