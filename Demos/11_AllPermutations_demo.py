def AllPermutations(nums):
    prevPermutations = [[]]
    allPermutations = []

    for num in nums:
        allPermutations = []
        for permutation in prevPermutations:
            for i in range(len(permutation) + 1):
                newPerm = permutation.copy()
                newPerm.insert(i, num)
                allPermutations.append(newPerm)
        
        prevPermutations = allPermutations

    allPermutations.sort()
    return allPermutations

if __name__ == "__main__":
    nums = [1,3,5]
    expectedOutput = [[1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]]
    output = AllPermutations(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
