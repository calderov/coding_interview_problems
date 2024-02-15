# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
# 
# Examples:
# 
#   Input: nums1 = [1,2,2,1], nums2 = [2,2]
#   Output: [2]
# 
#   Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#   Output: [9,4]
#   Explanation: [4,9] is also accepted.
# 

def BinarySearch(nums, value):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == value:
            return mid
        
        if nums[mid] < value:
            left += 1

        else: # nums[mid] > value
            right -= 1

    return -1

def Intersection(nums1, nums2):
    return list(set(nums1).intersection(nums2))

if __name__ == "__main__":
    # Example 1
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    expectedOutput = [2]
    output = Intersection(nums1, nums2)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    
    # Example 2
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    expectedOutput = [9,4]
    output = Intersection(nums1, nums2)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)

    # Examples 3
    nums1 = [34, 40, 59, 13, 76, 95, 58, 27, 19, 16, 55, 7, 71, 19, 93, 11, 99, 75, 68, 78, 94, 48, 92, 93, 15, 61, 46, 47, 84, 97, 45, 15, 82, 98, 66, 7, 34, 56, 62, 33, 5, 7, 94, 84, 2, 44, 55, 23, 2, 75, 66, 40, 63, 88, 99, 75, 52, 35, 18, 18, 67, 96, 24, 79, 61, 96, 95, 49, 16, 81, 21, 67, 48, 98, 13, 74, 84, 51, 46, 12]
    nums2 = [56, 78, 38, 78, 16, 27, 54, 6, 21, 6, 53, 42, 51, 55, 76, 8, 83, 73, 80, 22, 12, 9, 65, 36, 23, 51, 98, 34, 48, 75, 88, 53, 58, 87, 39, 92, 78, 30, 11, 82, 69, 38, 87, 99, 68, 81, 73, 15, 61, 97, 78, 84, 23, 45, 61, 62, 73, 1, 86, 70, 73, 42, 46, 24, 35, 23, 26, 64, 84, 71, 60, 82, 70, 45, 3, 58, 82, 96, 1, 23]
    expectedOutput = [11, 12, 15, 16, 21, 23, 24, 27, 34, 35, 45, 46, 48, 51, 55, 56, 58, 61, 62, 68, 71, 75, 76, 78, 81, 82, 84, 88, 92, 96, 97, 98, 99]
    output = Intersection(nums1, nums2)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
