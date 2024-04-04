# 84. Largest Rectangle in Histogram (Hard)
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle
# in the histogram.
# 
# Example 1:
#   Input: heights = [2,1,5,6,2,3]
#   Output: 10
#   Explanation: The above is a histogram where width of each bar is 1.
#                The largest rectangle is shown in the red area, which has
#                an area = 10 units.
# 
# Example 2:
#   Input: heights = [2,4]
#   Output: 4
# 
# Constraints:
#   1 <= heights.length <= 105
#   0 <= heights[i] <= 104

class Solution:
    # Brute force
    # Time complexity: O(n log n)
    # Space complexity: O(1)
    def LargestRectangleAreaV1(self, nums):
        maxArea = -1

        for i in range(len(nums)):
            start = i
            end = i

            while start > 0 and nums[start - 1] >= nums[i]:
                start -= 1

            while end < len(nums) - 1 and nums[end + 1] >= nums[i]:
                end += 1

            area = (end - start + 1) * nums[i]

            maxArea = max(maxArea, area)

        return maxArea

    # Divide and conquer (divide on min height)
    # Time complexity: O(n log n) on average O(n ^ 2) worst case
    # Space complexity: O(1)
    def LargestRectangleAreaV2(self, nums, start=None, end=None):
        if start == None or end == None:
            start = 0
            end = len(nums) - 1

        if start > end:
            return 0

        minIndex = start
        minValue = nums[minIndex]

        for i in range(start, end + 1):
            if nums[i] < minValue:
                minIndex = i
                minValue = nums[minIndex]

        area = minValue * (end - start + 1)

        return max(area,
                    self.LargestRectangleAreaV2(nums, start, minIndex - 1),
                    self.LargestRectangleAreaV2(nums, minIndex + 1, end))

    # Time complexity: O(n)
    # Space complexity: O(n)
    def LargestRectangleAreaV3(self, heights, start=None, end=None):
        stack = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index

            while stack:
                prevIndex, prevHeight = stack[-1]
                if prevHeight < height:
                    break

                stack.pop()

                maxArea = max(maxArea, (index - prevIndex) * prevHeight)
                start = prevIndex

            stack.append((start, height))

        for index, height in stack:
            maxArea = max(maxArea, (len(heights) - index) * height)

        return maxArea


    def LargestRectangleArea(self, nums):
        return self.LargestRectangleAreaV3(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [2,1,5,6,2,3]
    expectedOutput = 10
    output = solution.LargestRectangleArea(nums)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 2
    nums = [6,7,5,2,4,5,9,3]
    expectedOutput = 16
    output = solution.LargestRectangleArea(nums)
    print(output, expectedOutput, output == expectedOutput)