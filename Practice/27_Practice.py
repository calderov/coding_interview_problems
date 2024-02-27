# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times as it
# shows in both arrays and you may return the result in any order.
# 
# Examples:
#   Input: nums1 = [1,2,2,1], nums2 = [2,2]
#   Output: [2,2]
# 
#   Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#   Output: [4,9]
#   Explanation: [9,4] is also accepted.

def InteresectionWithDupes(nums1, nums2):
    frequencies = {}
    intersection = []

    for num in nums1:
        if num not in frequencies:
            frequencies[num] = 0
        frequencies[num] += 1

    for num in nums2:
        if num in frequencies and frequencies[num] > 0:
            frequencies[num] -= 1
            intersection.append(num)

    return intersection

def AreEqual(nums1, nums2):
    if len(nums1) != len(nums2):
        return False
    
    for num in nums1:
        if num not in nums2:
            return False
        
    return True

if __name__ == "__main__":
    # Example 1:
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    expectedOutput = [2,2]
    output = InteresectionWithDupes(nums1, nums2)
    print(output)
    print(expectedOutput)
    print(AreEqual(output, expectedOutput))
    print()
     
    # Example 2:
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    expectedOutput = [4,9]
    output = InteresectionWithDupes(nums1, nums2)
    print(output)
    print(expectedOutput)
    print(AreEqual(output, expectedOutput))
    print()

