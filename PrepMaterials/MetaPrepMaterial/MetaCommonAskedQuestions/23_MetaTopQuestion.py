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

# Time complexity: O(n!)
# Space complexity: O(n!)
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

# Time complexity: O(n!*n!*log(n!))
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
# Space complexity: O(1) if run in place, otherwise O(n)
def nextPermutationBetter(permutation):
    p = permutation.copy() # Remove this to run in place
    n = len(p)

    # 1. Find pivot, the largest index i such that p[i] < p[i + 1]. If there is no pivot, reverse and return p
    pivot = None
    for i in range(n - 2, -1, -1):
        if p[i] < p[i + 1]:
            pivot = i
            break
    
    if not pivot:
        p.reverse()
        return p

    # 2. Find successor, the largest index i such that i > pivot and p[i] > p[pivot]
    successor = None
    for i in range(n - 1, i, -1):
        if p[i] > p[pivot]:
            successor = i
            break

    # 3. Swap p[pivot] and p[successor]
    p[pivot], p[successor] = p[successor], p[pivot]

    # 4. Reverse p[pivot + 1:] and return p
    i = pivot + 1
    j = n - 1
    while i < j:
        p[i], p[j] = p[j], p[i]
        i += 1
        j -= 1

    return p

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
