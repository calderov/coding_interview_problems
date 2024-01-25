# Problem:
# Given an array of sorted numbers, remove all duplicate number
# instances from it (in-place), such that each element appears only
# once. The relative order of the elements should be kept the same
# and you should not use any extra space so that that the solution
# have a space complexity of O(1).
#
# Move all the unique elements at the beginning of the array and after 
# moving return the length of the subarray that has no duplicate in it.

class Solution:
    def RemoveDuplicates(self, nums):
        slow = 0
        fast = 1

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    arr = [2, 3, 3, 3, 6, 9, 9]
    expectedOutput = 4
    print(arr)
    output = solution.RemoveDuplicates(arr)
    print(arr)
    print(output == expectedOutput)

    print()

    # Example 2
    arr = [2, 2, 2, 11]
    expectedOutput = 2
    print(arr)
    output = solution.RemoveDuplicates(arr)
    print(arr)
    print(output == expectedOutput)
