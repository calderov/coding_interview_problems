# Problem
# Given an array of unsorted numbers and a target sum,
# count all triplets in it such that nums[i] + nums[j] + nums[k] < target
# where i, j, and k are three different indices.
# Write a function to return the count of such triplets.

# Solution 1:
# Solution 1 complexity: O(n^3) as we use three nested loops for traversing nums.
# Time complexity: O(1) as the triplets count can be maintained in just 1 variable.
def TripletsWithSmallerSum(nums, targetSum):
    tripletsCount = 0
    n = len(nums)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i < j and j < k:
                    currentSum = nums[i] + nums[j] + nums[k]
                    if currentSum < targetSum:
                        tripletsCount += 1
    return tripletsCount

# Solution 2:
# 1. Sort the 'nums' arraiy in ascending order.
# 2. The algorithm uses three pointers, 'i', 'j', and 'k', to traverse the list.
# 3. A loop iterates through 'i' from 0 to 'n - 2', where 'n' is the length of 'nums'.
# 4. The 'j' pointer starts at 'i + 1' (the next element after 'i'), and 'k' starts at 'n - 1'.
# 5. Another loop with 'j' and 'k' pointers runs while 'j' is less than 'k'.
# 6. Inside the inner loop, the sum of elements at 'i', 'j', and 'k' is calculated.
# 7. If the current sum is less than 'targetSum', all triplets formed by elements between
#     'j' and 'k' will also satisfy the condition. Therefore, 'tripletsCount' is incremented
#     by 'k - j', and 'j' is moved one step to the right.
# 8. If the current sum is not less than 'targetSum', 'k' is moved one step to the left as the
#    sum exceeds that of the target.
# 9. The outer loop continues, and 'i' is incremented to explore the next potential triplet.
# 10. The process continues until 'i' has covered all relevant elements.
# 11. The function returns 'tripletsCount', which is the count of valid triplets.

# Note:
# The algorithm leverages the sorted nature of the list to efficiently find and count
# triplets with a sum less than the specified 'targetSum'.

# Solution 2 complexity:
# Time complexity: O(n^2) as we use two nested loops to evaluate candidate triplets.
# Space complexity: O(1) as we rely only on a few auxiliar variables that take constant space.
def TripletsWithSmallerSumV2(nums, targetSum):
    nums.sort()
    n = len(nums)
    tripletsCount = 0
    for i in range(n - 2):
        j = i + 1 # Left
        k = n - 1 # Right
        while j < k:
            currentSum = nums[i] + nums[j] + nums[k]
            if currentSum < targetSum:
                # Since nums[k] >= nums[j] then the sums: 
                #   nums[i] + nums[j] + nums[k]
                #   nums[i] + nums[j] + nums[k - 1]
                #   nums[i] + nums[j] + nums[k - 2]
                #   ...
                #   nums[i] + nums[j] + nums[k - j]
                # are also less than targetSum.
                tripletsCount += k - j
                j += 1
            else:
                # We need a pair with a smaller sum.
                k -= 1
    return tripletsCount

if __name__ == "__main__":
    # Example 1
    nums = [-1, 0, 2, 3]
    targetSum = 3
    result = TripletsWithSmallerSumV2(nums, targetSum) 
    expected = 2 # Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
    print(result, expected, result == expected)

    # Example 2
    nums = [-1, 4, 2, 1, 3]
    targetSum = 5
    result = TripletsWithSmallerSumV2(nums, targetSum) 
    expected = 4 # Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
    print(result, expected, result == expected)

    # Example 3
    nums = [0, 0, 0, 0, 0]
    targetSum = 1
    result = TripletsWithSmallerSumV2(nums, targetSum) 
    expected = 10 # Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
    print(result, expected, result == expected)