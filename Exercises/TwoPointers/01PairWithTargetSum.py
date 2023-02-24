# Given an array of sorted numbers and a target sum, find a pair in the 
# array whose sum is equal to the given target.
#
# Time complexity: O(n) where n is the number of elements in the array
# Space complexity: O(1) constant space
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

    return []

if __name__ == "__main__":
    # Example 1
    arr = [1, 2, 3, 4, 6]
    target = 6
    print(PairWithTargetSum(arr, target))

    # Example 2
    arr = [2, 5, 9, 11]
    target = 11
    print(PairWithTargetSum(arr, target))