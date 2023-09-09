# Problem:
# We are given an array containing n objects. Each object, when created, was
# assigned a unique number from the range 1 to n based on their creation
# sequence. This means that the object with sequence number 3 was created
# just before the object with sequence number 4.
# 
# Write a function to sort the objects in-place on their creation sequence
# number in O(n) and without using any extra space. For simplicity, let’s
# assume we are passed an integer array containing only the sequence numbers,
# though each number is actually an object.
# 
# Examples:
# 
#   Input: [3, 1, 5, 4, 2]
#   Output: [1, 2, 3, 4, 5]
# 
#   Input: [2, 6, 4, 3, 1, 5]
#   Output: [1, 2, 3, 4, 5, 6]
# 
#   Input: [1, 5, 6, 4, 3, 2]
#   Output: [1, 2, 3, 4, 5, 6]

class Solution:
    # Solution:
    # 
    # 1. Initialize an index variable i to 0. This variable will track of the
    #    current position in the array during the sorting process.
    #      i = 0
    # 
    # 2. Enter a while loop that runs until i is less than the length of the
    #    nums array.
    # 
    # 3. Inside the loop, check if the current element nums[i] is equal to i + 1.
    #    If it is, this means that the element is in its correct position (since
    #    the sequence numbers start from 1). Increment i by 1 and continue to the
    #    next iteration of the loop.
    # 
    # 4. If nums[i] is not equal to i + 1, it means that the current element is
    #    out of place. In this case, swap the current element nums[i] with the
    #    element at the position nums[i] - 1 in the array. This swap places the
    #    element in its correct position.  
    # 
    #    After the swap, increment i by 1 to move to the next element in the array.
    # 
    # 5. Repeat steps 3 to 5 until i reaches the end of the array. The loop will
    #    continue swapping elements until all elements are in their correct
    #    positions.
    # 
    # 6. Once the loop completes, the array nums will be sorted in-place based on
    #    their creation sequence numbers.
    # 
    # 7. Finally, return the sorted nums array.

    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1) 
    def SortInPlace(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
                continue
            temp = nums[i]
            nums[i] = nums[nums[i] - 1]
            nums[temp - 1] = temp
        return nums

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [3, 1, 5, 4, 2]
    expectedOutput = [1, 2, 3, 4, 5]
    output = solution.SortInPlace(nums)
    print(output == expectedOutput)

    # Example 2
    nums = [2, 6, 4, 3, 1, 5]
    expectedOutput = [1, 2, 3, 4, 5, 6]
    output = solution.SortInPlace(nums)
    print(output == expectedOutput)

    # Example 3
    nums = [1, 5, 6, 4, 3, 2]
    expectedOutput = [1, 2, 3, 4, 5, 6]
    output = solution.SortInPlace(nums)
    print(output == expectedOutput)

    # Example 4
    nums = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
    expectedOutput = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    output = solution.SortInPlace(nums)
    print(output == expectedOutput)