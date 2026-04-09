# Median of Two Sorted Arrays
# HARD
# https://scaleengineer.com/dsa/problems/median-of-two-sorted-arrays

# Description
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     1 <= m + n <= 2000
#     -106 <= nums1[i], nums2[i] <= 106
from math import inf

# Time: O(m + n + (m + n) * log(m + n))
# Space: O(m + n)
def GetMedianBruteForce(nums1, nums2):
    nums = nums1 + nums2
    nums.sort()
    
    n = len(nums)
    if n % 2 == 0:
        return (nums[int(n / 2) - 1] + nums[int(n / 2)]) / 2
    return nums[int(n / 2)]

# Time: O(m + n)
# Space: O(1)
def GetMedianBetter(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    total = m + n
    i = 0
    j = 0

    prev = 0
    curr = 0

    for _ in range(total // 2 + 1):
        prev = curr
        if i < m and j < n:
            if nums1[i] < nums2[j]:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            continue

        if i < m:
            curr = nums1[i]
            i += 1
            continue

        if j < n:
            curr = nums2[j]
            j += 1

    if total % 2 == 1:
        return curr
    return (prev + curr) / 2

# Time: O(log(m + n))
# Space: O(1)
def GetMedianBest(nums1, nums2):
    if len(nums1) > len(nums2):
        return GetMedianBest(nums2, nums1)
    
    m = len(nums1)
    n = len(nums2)

    lo = 0
    hi = m

    while lo <= hi:
        i = (lo + hi) // 2
        j = (m + n + 1) // 2 - i

        left1 =  nums1[i - 1] if i > 0 else -inf
        right1 = nums1[i]     if i < m else inf
        left2 =  nums2[j - 1] if j > 0 else -inf
        right2 = nums2[j]     if j < n else inf

        # Check if partitions are correct
        if left1 <= right2 and left2 <= right1:
            if (m + n) % 2 == 1:
                return max(left1, left2)
            return (max(left1, left2) + min(right1, right2)) / 2
        
        # Partitions were not correct, partition again
        if left1 > right2:
            hi = i - 1
        else:
            lo = i + 1

    # Unreachable if nums1 and nums2 are sorted
    return None

def GetMedian(nums1, nums2):
    return GetMedianBest(nums1, nums2)

if __name__ == "__main__":
    # Example 1:
    nums1 = [1,3]
    nums2 = [2]
    expected = 2
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nums1 = [1,2]
    nums2 = [3,4]
    expected = 2.5
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3: One empty array
    nums1 = []
    nums2 = [1]
    expected = 1
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: Both arrays same size, odd total
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    expected = 3.5
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Negative numbers
    nums1 = [-5, -3, -1]
    nums2 = [-4, -2, 0]
    expected = -2.5
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: Duplicates
    nums1 = [1, 2, 2]
    nums2 = [2, 3, 3]
    expected = 2
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: Single elements
    nums1 = [5]
    nums2 = [10]
    expected = 7.5
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 8: Large numbers
    nums1 = [1000000, 2000000]
    nums2 = [1500000]
    expected = 1500000
    output = GetMedian(nums1, nums2)
    print(expected)
    print(output)
    print(expected == output)
    print()
