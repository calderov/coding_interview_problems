from functools import reduce

# Problem:
# Given an array with positive numbers and a positive target number,
# find all of its contiguous subarrays whose product is less than the
# target number.

# Solution:
# Use two pointers i and j to produce all the subarrays in 'nums' where
# each subarray goes from the ith element of 'nums' to the jth element of
# 'nums', then pass that subarray to a routine that returns the product
# of all the elements in it and compare it with the target. If the product
# is less than the target, save the subarray to a list of subarrays and
# return such list when no more subarrays are left to be explored. 
#
# Solution complexity:
# Time complexity: O(n^3). Since the process to produce all the subarrays
# in 'nums' takes two nested loops and O(n^2) operations, and the process
# to compute the product of all the elements of a subarray takes O(j - i) 
# operations where j - i is at most n, then: 
# O(n^2) * O(j - i) = O(n^2) * O(n) = O(n^3) 
#                  
# Space complexity: O(2^n * n) as there are at most 2^n subsets on a set
# of at most n elements. 
def SubarrayWithProductLessThanATarget(nums, target):
    subarrays = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray = nums[i : j]
            subarrayProduct = reduce(lambda x, y: x*y, subarray)
            if subarrayProduct < target:
                subarrays.append(subarray)
    return subarrays

def AreArraysEqual(array1, array2):
    if len(array1) != len(array2):
        return False

    for element in array1:
        if element not in array2:
            return False
    
    for element in array2:
        if element not in array1:
            return False
    
    return True

if __name__ == "__main__":
    # Example 1
    nums = [2, 5, 3, 10]
    target = 30                                  
    expectedOutput = [[2], [5], [2, 5], [3], [5, 3], [10]]
    output = SubarrayWithProductLessThanATarget(nums, target)
    print(AreArraysEqual(output, expectedOutput))

    # Example 2
    nums = [8, 2, 6, 5]
    target = 50
    expectedOutput = [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
    output = SubarrayWithProductLessThanATarget(nums, target)
    print(AreArraysEqual(output, expectedOutput))