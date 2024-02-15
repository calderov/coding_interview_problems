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

def IntersectionWithoutSet(nums1, nums2):
    nums1.sort()
    nums2.sort()

    result = []

    for num in nums1:
        if result and result[-1] == num:
            continue

        if BinarySearch(nums2, num) == -1:
            continue

        result.append(num)

    result.sort(reverse=True)
    
    return result

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