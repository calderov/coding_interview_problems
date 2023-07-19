# Problem: 
# Given an array of numbers sorted in incremental order and a target number, return a pair of indexes from the array
# that point to numbers whose sum is equal to the given target. If no such pair exists, return [-1, -1].
#
# For example, an input of: [1, 2, 3, 4, 6], 6
# should produce an output of: [1, 3]
# as the positions 1 and 3 of the array (zero index based) correspond to the numbers 2 and 4,
# and 2 + 4 = 6
#
# Constraints:
# Time complexity: O(n) where n is the number of elements in the array
# Space complexity: O(1) constant space
#
# Solution:
# Use two indexes, and place them at the begining and the end of the array.
# The first index (low) will traverse the array from left to right.
# The second index (high) will traverse the array from from right to left.
# The values referenced by the indexes will be added and compared to the target number in the folowing way:
# - If both indexes are equal, return an array of this form [-1, -1] regardless of the sum, as it means that both indexes
#   are pointing to the same element.
# - If the sum equals the target, return an array with the two pointers i.e. [low, high].
# - If the sum is lower than the target, increment the lower pointer (low += 1).
# - If the sum is higher than the target, decrement the higher pointer (high -= 1).
def PairWithTargetSum(arr, target):
    low = 0
    high = len(arr) - 1

    while low < high:
        currentSum = arr[low] + arr[high]

        if currentSum == target:
            return [low, high]

        if currentSum > target:
            high -= 1
            continue

        if currentSum < target:
            low += 1
            continue

    return [-1, -1]

if __name__ == "__main__":
    # Example 1
    arr = [1, 2, 3, 4, 6]
    target = 6
    print(PairWithTargetSum(arr, target))

    # Example 2
    arr = [2, 5, 9, 11]
    target = 11
    print(PairWithTargetSum(arr, target))

    # Example 3
    arr = [3, 4, 5, 6]
    target = 12
    print(PairWithTargetSum(arr, target))