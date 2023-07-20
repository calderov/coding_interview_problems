# Problem:
# Given an array of integer numbers, return True if any value appears more than once, or False if all elements are distinct.
# For example: 
# - An input of the array [1, 2, 3, 4] should return False (as all its elements are distinct).
# - An input of the array [1, 2, 3, 1] should return True (as the number 1 is repeated).

# Solution 1:
# Brute force the comparison of all elements against one another, if at any point we find a duplicate, return True. Or return
# False whenever we are finished with all the comparisons.
#
# Solution 1 complexity:
# Time complexity: O(n^2) where n is the number of elements in the array.
# Space complexity: O(1) constant space.
def ContainsDuplicateV1(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] == nums[j]:
                return True
    return False


# Solution 2:
# Use a hash set to store a copy of the elements of the array. Since hash sets do not admit duplication, any duplicate value
# will accepted only once. This should make the lenght of the set different to that of the array if the original array had duplicates in it.
# Thus, copy the values of the array into a set and compare their respective lengths, if they are equal return False (as no value got discarted,
# meaning all the elements in the array are also in the set) otherwise return True.
# 
# Solution 2 complexity:
# Time complexity: O(n) where n is the number of elements in the array, as there is only one traversal of the array.
# Space complexity: O(n) space, as the set uses at most n slots to store a copy of the array.
def ContainsDuplicateV2(nums):
    hashSet = set(nums)
    return not len(nums) == len(hashSet)

if __name__ == "__main__":
    # Example 1
    arr = [1, 2, 3, 4]
    print(ContainsDuplicateV1(arr), False)
    print(ContainsDuplicateV2(arr), False)

    # Example 2
    arr = [1, 2, 3, 1]
    print(ContainsDuplicateV1(arr), True)
    print(ContainsDuplicateV2(arr), True)