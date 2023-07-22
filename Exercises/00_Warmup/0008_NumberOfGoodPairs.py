# Problem:
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Solution:
# Check for all the combinations of i and j such that nums[i] == nums[j] and i < j.
# Time complexity: O(n^2) square.
# Time space: O(1)
def NumberOfGoodPairs(nums):
    totalGoodPairs = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            # Check if (i, j) is good!
            if nums[i] == nums[j] and i < j:
                totalGoodPairs += 1
    return totalGoodPairs

if __name__ == "__main__":
    print(NumberOfGoodPairs([1,2,3,1,1,3]), 4)
    print(NumberOfGoodPairs([1,1,1,1]), 6)
    print(NumberOfGoodPairs([1,2,3]), 0)