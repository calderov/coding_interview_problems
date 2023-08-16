# Problem:
# Given a sorted array, create a new array containing squares of
# all the numbers of the input array in the sorted order.

class Solution:
    # Solution 1:
    # A straightforward solution is to create an array of squares and
    # then sort it.
    #
    # Solution 1 complexity:
    # Time complexity: O(nlogn) due to the additional sorting step.
    # Space complexity: O(n) as a fresh array is required.
    def SquareSortedArrayV1(self, nums):
        return sorted([i ** 2 for i in nums])

    # Solution 2:
    # First declare an empty array to store the
    # squared values comming from the original 
    # nums array.
    #
    # Use two pointers to traverse the nums array. 
    # One from right to left, and one from left to right.
    #  
    # While the left pointer is less than or equal to the right pointer,
    # take the pointed values from the nums array and square them.
    #
    # If the square of the right value is greater than the square of the
    # right value. Insert it to the beginning of the squared values array,
    # and move the right pointer one step to the left. Otherwise, insert the 
    # square of the left value instead, and move the left pointer one step to
    # the right.
    #
    # Once the left pointer is greater than the right one, the array of squared
    # values should be complete and properly sorted. Return it.
    #
    # Solution 2 complexity:
    # Time complexity: O(n) linear, as the whole process happens in a single pass.
    # Space complexity: O(n) as a fresh array is required.
    def SquareSortedArrayV2(self, nums):
        idxLeft = 0
        idxRight = len(nums) - 1
        sortedSquares = []
        
        while idxLeft <= idxRight:
            valLeft = nums[idxLeft] ** 2
            valRigth = nums[idxRight] ** 2
            if valRigth > valLeft:
                sortedSquares.insert(0, valRigth)
                idxRight -= 1
            else:
                sortedSquares.insert(0, valLeft)
                idxLeft += 1

        return sortedSquares
    
    def SquareSortedArray(self, nums):
        return self.SquareSortedArrayV2(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [-2, -1, 0, 2, 3]
    expectedOutput = [0, 1, 4, 4, 9]
    output = solution.SquareSortedArray(nums)
    print(output, output == expectedOutput)

    # Example 2
    nums = [-3, -1, 0, 1, 2]
    expectedOutput = [0, 1, 1, 4, 9]
    output = solution.SquareSortedArray(nums)
    print(output, output == expectedOutput)
