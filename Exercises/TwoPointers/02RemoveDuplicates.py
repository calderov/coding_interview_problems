# Given an array of sorted numbers, remove all duplicate number
# instances from it in-place, such that each element appears only
# once. The relative order of the elements should be kept the same
# and you should not use any extra space so that that the solution
# have a space complexity of O(1).
#
# Time complexity: O(n) where n is the number of elements in the array
# Space complexity: O(1) constant space
def RemoveDuplicates(arr):
    # Return early for the trivial cases of empty and singular arrays
    if len(arr) <= 1:
        return len(arr)
    
    next = 1
    last_non_duplicate = 0 # Index pointing to the last non duplicate element

    while next < len(arr):
        if arr[last_non_duplicate] != arr[next]:
            last_non_duplicate += 1
            arr[last_non_duplicate] = arr[next]
        next += 1

    return last_non_duplicate + 1 # Add one to the index to get the length of the non dupe region

def RunRemoveDuplicateExamples():
    # Example 1
    arr = [2, 3, 3, 3, 6, 9, 9]
    unique = RemoveDuplicates(arr)
    print(unique)
    print(arr)

    # Example 2
    arr = [2, 2, 2, 11]
    unique = RemoveDuplicates(arr)
    print(unique)
    print(arr)

# Given an unsorted array of numbers and a target ‘key’, 
# remove all instances of ‘key’ in-place and return the new length of the array.
#
# Time complexity: O(n) where n is the number of elements in the array
# Space complexity: O(1) constant space
def RemoveKeyFromUnsortedArray(arr, key):
    lnk = 0 # Last non-key index
    for i in range(len(arr)):
        if arr[i] != key:
            arr[lnk] = arr[i]
            lnk += 1
    
    # Ensure values after lnk are set to key
    for i in range(lnk, len(arr)):
        arr[i] = key

    return lnk

def RunRemoveKeyFromUnsortedArrayExamples():
    # Example 1
    arr = [3, 2, 3, 6, 3, 10, 9, 3]
    key = 3
    filtered = RemoveKeyFromUnsortedArray(arr, key)
    print(filtered)
    print(arr)

    arr = [2, 11, 2, 2, 1]
    key = 2
    filtered = RemoveKeyFromUnsortedArray(arr, key)
    print(filtered)
    print(arr)

if __name__ == "__main__":
    print("Remove duplicate examples")
    RunRemoveDuplicateExamples()

    print("Remove unsorted array examples")
    RunRemoveKeyFromUnsortedArrayExamples()


