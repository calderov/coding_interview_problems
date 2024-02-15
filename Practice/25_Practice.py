# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# Examples:
# 
#   Input: nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]
# 
#   Input: nums = [1], k = 1
#   Output: [1]

def GetKMostFrequent(nums, k):
    frequencies = {}

    for num in nums:
        if num not in frequencies:
            frequencies[num] = 0 
        frequencies[num] += 1

    return sorted(frequencies.keys(), key=lambda x: frequencies[x], reverse=True)[:k]

if __name__ == "__main__":
    # Example 1
    nums = [1,1,1,2,2,3]
    k = 2
    expectedOutput = [1,2]
    output = GetKMostFrequent(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [1]
    k = 1
    expectedOutput = [1]
    output = GetKMostFrequent(nums, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()