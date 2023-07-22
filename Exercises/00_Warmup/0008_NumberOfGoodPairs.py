# Problem:
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Solution 1:
# Check for all the combinations of i and j such that nums[i] == nums[j] and i < j.

# Solution 1 complexity:
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

# Solution 2:
# Use a frequency map to register how many pairs does a given number appear on.
# Then return the sum of all those pairs.

# Solution 2 complexity:
# Time complexity: O(n) square.
# Time space: O(n)
def NumberOfGoodPairsV2(nums):
    totalGoodPairs = 0
    freq = {}
    for n in nums:
        if n not in freq:
            freq[n] = 0
        else:
            freq[n] += 1
        totalGoodPairs += freq[n]
    return totalGoodPairs

if __name__ == "__main__":
    print(NumberOfGoodPairs([1,2,3,1,1,3]), 4)
    print(NumberOfGoodPairs([1,1,1,1]), 6)
    print(NumberOfGoodPairs([1,2,3]), 0)

    print(NumberOfGoodPairsV2([1,2,3,1,1,3]), 4)
    print(NumberOfGoodPairsV2([1,1,1,1]), 6)
    print(NumberOfGoodPairsV2([1,2,3]), 0)