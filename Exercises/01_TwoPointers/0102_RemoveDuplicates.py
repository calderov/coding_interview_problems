# Problem:
# Given an array of sorted numbers, remove all duplicate number
# instances from it (in-place), such that each element appears only
# once. The relative order of the elements should be kept the same
# and you should not use any extra space so that that the solution
# have a space complexity of O(1).
#
# Move all the unique elements at the beginning of the array and after 
# moving return the length of the subarray that has no duplicate in it.
#
# Solution:
# Use two pointers, one slow and one fast. The slow pointer will keep
# unrepeated elements to its left, while the fast pointer will traverse
# the array normally looking for different elements. 
#
# Whenever the elements at the slow and fast pointers are diferent, move 
# the slow pointer to one position to the right and copy into it the value
# pointed by the fast pointer. Otherwise, the fast pointer is sitting
# on a dupe, and should be ignored. In both cases, the right pointer
# moves one position to the right in each iteration until it is
# finished traversing the array.
# 
# In the end, the slow pointer will be sitting between the regions with
# unique values (to its right) and duplicates (to its left). To return
# the  number of unique values, just add 1 to the slow pointer and return
# it as arrays are zero indexed.
#
# Solution complexity:
# Time complexity: O(n) where n is the number of elements in the array.
# Space complexity: O(1) constant space.
def RemoveDuplicates(arr):
    # Return early for the trivial cases of empty and singular arrays
    if len(arr) <= 1:
        return len(arr)
    
    fast = 1
    slow = 0

    while fast < len(arr):
        if arr[slow] != arr[fast]:
            slow += 1
            arr[slow] = arr[fast]
        fast += 1

    return slow + 1

if __name__ == "__main__":
    # Example 1
    arr = [2, 3, 3, 3, 6, 9, 9]
    print("Original:", arr)
    unique = RemoveDuplicates(arr)
    print("Clean:   ", arr)
    print("Unique elements:", unique)

    print()

    # Example 2
    arr = [2, 2, 2, 11]
    print("Original:", arr)
    unique = RemoveDuplicates(arr)
    print("Clean:   ", arr)
    print("Unique elements:", unique)