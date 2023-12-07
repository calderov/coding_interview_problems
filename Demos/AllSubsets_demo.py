def AllSubsets(nums):
    subsets = [[]]
    
    for num in nums:
        n = len(subsets)

        for i in range(n):
            subset = subsets[i] + [num]
            subsets.append(subset)
    
    subsets.sort(key=lambda x: len(x)) # Optional
    
    return subsets


if __name__ == "__main__":
    nums = [1, 2, 3]
    expectedOutput = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    output = AllSubsets(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)