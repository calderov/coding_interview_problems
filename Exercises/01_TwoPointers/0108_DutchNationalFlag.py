# Problem:
# Given an array containing 0s, 1s and 2s, sort the array in-place. 
# You should treat numbers of the array as objects, hence, we can’t 
# count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; 
# and since our input array also consists of three different numbers that is
# why it is called Dutch National Flag problem.

# Solution 1:
# Bubble Sort. 
#
# Solution 1 complexity:
# Time complexity: O(n^2) as all the pairs of numbers in nums are evaluated.
# Space complexity: O(1) constant space as the array is sorted in place.
def DutchNationalFlag(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            count += 1
            if nums[i] < nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    # No return as nums is sorted in place

# Solution 2:
# Traverse the array twice, one to put zeros to the left of the array
# and one to put ones just after those zeros.
#
# Solution 2 complexity:
# Time complexity: O(n) linear time
# Space complexity: O(1) constant space as the array is sorted in place
def DutchNationalFlagV2(nums):
    n = len(nums)
    left = 0

    # Stack zeros
    for i in range(left, n):
        count += 1
        if nums[i] == 0:
            # Swap
            temp = nums[i]
            nums[i] = nums[left]
            nums[left] = temp

            left += 1

    # Stack ones
    for i in range(left, n):
        count += 1
        if nums[i] == 1:
            # Swap
            temp = nums[i]
            nums[i] = nums[left]
            nums[left] = temp

            left += 1
    # No return as nums is sorted in place

if __name__ == "__main__":
    # Example 1
    nums = [1, 0, 2, 1, 0]
    expectedOutput = [0, 0, 1, 1, 2]

    print(nums)
    DutchNationalFlagV2(nums)

    print(nums)
    print(expectedOutput)
    print(nums == expectedOutput)

    # Example 2
    nums = [2, 2, 0, 1, 2, 0]
    expectedOutput = [0, 0, 1, 2, 2, 2]

    DutchNationalFlagV2(nums)

    print(nums)
    print(expectedOutput)
    print(nums == expectedOutput)
