# Next Greater Element (easy)
# Problem Statement
# 
# Given two integer arrays nums1 and nums2, return an array answer such that
# answer[i] is the next greater number for every nums1[i] in nums2. The next
# greater element for an element x is the first element to the right of x
# that is greater than x. If there is no greater number, output -1 for that
# number.
# 
# The numbers in nums1 are all present in nums2 and nums2 is a permutation of
# nums1.
# 
# Examples:
# 
#   Input: nums1 = [4,2,6], nums2 = [6,2,4,5,3,7]
#   Output: [5,4,7]
#   Explanation: The next greater number for 4 is 5, for 2 is 4, and
#   for 6 is 7 in nums2.
#   
#   Input: nums1 = [9,7,1], nums2 = [1,7,9,5,4,3]
#   Output: [-1,9,7]
#   Explanation: The next greater number for 9 does not exist, for 7 is
#   9, and for 1 is 7 in nums2.
#   
#   Input: nums1 = [5,12,3], nums2 = [12,3,5,4,10,15]
#   Output: [10,15,5]
#   Explanation: The next greater number for 5 is 10, for 12 is 15, and
#   for 3 is 5 in nums2.
# 

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(n * m) where n and m are the length of nums1 and nums2 respectively.
    # Space complexity: O(n) as the answer has n items.
    def NextGreaterElementV1(self, nums1, nums2):
        answer = []

        for num  in nums1:
            index = nums2.index(num)
            
            if index == -1:
                answer.append(-1)
                continue

            nextGreater = -1
            for i in range(index, len(nums2)):
                if num < nums2[i]:
                    nextGreater = nums2[i]
                    break
            
            answer.append(nextGreater)

        return answer

    # Solution:
    # 
    # Solution complexity:
    # Time complexity: O(m) where m is the length of nums2
    # Space complexity: O(m) due to the space required for the next greater map 
    def NextGreaterElementV2(self, nums1, nums2):
        # Use monotonic decreasing stack to populate
        # map of next greater values
        nextGreaterMap = {}
        stack = [] # max stack

        for num in nums2:
            if not stack:
                stack.append(num)
                continue

            while stack and num > stack[-1]:
                nextGreaterMap[stack[-1]] = num
                stack.pop()
            
            stack.append(num)

        # Compute answer using next greater values map
        answer = []
        for num in nums1:
            if num in nextGreaterMap:
                answer.append(nextGreaterMap[num])
            else:
                answer.append(-1)

        return answer
    
    def NextGreaterElement(self, nums1, nums2):
        return self.NextGreaterElementV2(nums1, nums2)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1 = [4,2,6]
    nums2 = [6,2,4,5,3,7]
    expectedOutput = [5,4,7]
    output = solution.NextGreaterElement(nums1, nums2)
    print(output, expectedOutput, output == expectedOutput)

    # # Example 2
    nums1 = [9,7,1]
    nums2 = [1,7,9,5,4,3]
    expectedOutput = [-1,9,7]
    output = solution.NextGreaterElement(nums1, nums2)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums1 = [5,12,3]
    nums2 = [12,3,5,4,10,15]
    expectedOutput = [10,15,5]
    output = solution.NextGreaterElement(nums1, nums2)
    print(output, expectedOutput, output == expectedOutput)
