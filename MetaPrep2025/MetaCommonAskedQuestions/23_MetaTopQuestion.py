# Next permutation
# https://www.geeksforgeeks.org/dsa/next-permutation/
#
# Given an array of integers arr[] representing a permutation (i.e., all
# elements are unique and arranged in some order), find the next
# lexicographically greater permutation by rearranging the elements of the
# array.
# If such a permutation does not exist (i.e., the array is the last possible
# permutation), rearrange the elements to form the lowest possible order
# (i.e., sorted in ascending order).
# 
# Example 1:
#   Input: arr[] = [2, 4, 1, 7, 5, 0]
#   Output: [2, 4, 5, 0, 1, 7]
#   Explanation: The next lexicographically greater arrangement of the
#   elements in the array arr[] is [2, 4, 5, 0, 1, 7].
# 
# Example 2:
#   Input: arr[] = [3, 2, 1]
#   Output: [1, 2, 3]
#   Explanation: This is the last permutation, so we return the lowest
#   possible permutation (ascending order).
# 
# Example 3:
#   Input: arr[] = [1, 3, 5, 4, 2]
#   Output: [1, 4, 2, 3, 5]
#   Explanation: The next lexicographically greater arrangement of the
#   elements in the array arr[] is [1, 4, 2, 3, 5].
# 

def getAllPermutations(nums):
    allPermutations = []
    prevPermutations = [[]]

    for num in nums:
        allPermutations = []
        for permutation in prevPermutations:
            for i in range(len(permutation) + 1):
                newPerm = permutation.copy()
                newPerm.insert(i, num)
                allPermutations.append(newPerm)
        prevPermutations = allPermutations
    
    return allPermutations

# Time complexity: O(n!*n*log(n))
# Space complexity: O(n!)
def nextPermutationNaive(permutation):
    allPermutations = getAllPermutations(permutation)
    allPermutations.sort() # Lexicographic sort
    nextPermutation = None

    for i in range(len(allPermutations)):
        if allPermutations[i] == permutation:
            if i == len(allPermutations) - 1:
                nextPermutation = allPermutations[0]
            else:
                nextPermutation = allPermutations[i + 1]
    
    return nextPermutation

# Time complexity: O(n)
# Space complexity: O(1)
def nextPermutationBetter(permutation):
    # 1. Find pivot index (right most element smaller than its right element).
    pivot = None
    i = len(permutation) - 2
    while i >= 0:
        if permutation[i] < permutation[i + 1]:
            pivot = i
            break
        i -= 1

    # 2. If there was no pivot, this is the last permutation in lexicographical order,
    #    reverse it and return.
    if not pivot:
        return permutation[::-1]

    # 3. Find target index (right most element greater than the pivot).
    target = None
    i = pivot + 1
    while i < len(permutation):
        if permutation[i] > permutation[pivot]:
            target = i
        i += 1

    # 4. Swap values at pivot and target indexes.
    permutation[pivot], permutation[target] = permutation[target], permutation[pivot]

    # 5. Reverse elements at the right of the pivot index and return. This is the next lexicographical
    #    permutation.
    i = pivot + 1
    j = len(permutation) - 1
    while i < j:
        permutation[i], permutation[j] = permutation[j], permutation[i]
        i += 1
        j -= 1

    return permutation    

def nextPermutation(permutation):
    return nextPermutationBetter(permutation)

if __name__=="__main__":
    # Example 1:
    permutation = [2, 4, 1, 7, 5, 0]
    expected = [2, 4, 5, 0, 1, 7]
    output = nextPermutation(permutation)
    print(permutation)
    print(expected)
    print(output)
    print(output == expected)
    print()
    
    # Example 2:
    permutation = [3, 2, 1]
    expected = [1, 2, 3]
    output = nextPermutation(permutation)
    print(permutation)
    print(expected)
    print(output)
    print(output == expected)
    print()
    
    # Example 3:
    permutation = [1, 3, 5, 4, 2]
    expected = [1, 4, 2, 3, 5]
    output = nextPermutation(permutation)
    print(permutation)
    print(expected)
    print(output)
    print(output == expected)
    print()
