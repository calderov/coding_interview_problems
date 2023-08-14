# Problem:
# Given an array of unsorted numbers and a target number,
# find all unique quadruplets in it, whose sum is equal
# to the target number.

# Solution 1:
# Brute force, generate and evaluate all the possible quadruplets in nums. If a quadruplet Q satisfies that
# sum(Q) == target, add it to the list of quadruplets that will be returned at the end. 
#
# Solution 1 complexity:
# Time complexity: O(n^4) as we use 4 nested loops to produce all the possible quadruplets in nums.
# Space complexity: O(n choose 4) as that is the max number of possible quadruplet combinations in nums.
def QuadrupletSumToTarget(nums, target):
    quadruplets = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    quadruplet = sorted([nums[i], nums[j], nums[k], nums[l]])
                    currentSum = sum(quadruplet)
                    if currentSum == target and quadruplet not in quadruplets:
                        quadruplets.append(quadruplet)
    
    return quadruplets

# Solution 2:
# Sort nums to simplify the construction of viable quadruplets.
# Use two pointers i and j to traverse the nums array from start to finish and from finish to start respectively.
# In each iteration use two additional pointers k and l to construct quadruplets as follows:
#     quadruplet = sorted([nums[i], nums[j], nums[k], nums[l]])
# and its sum as:
#     quadrupletSum = sum(quadruplet)
#
# By manipulating k and l we could end up finding quadruplets that satisfy the condition:
#      quadrupletSum == target
# in which case, they should be added to the list of quadruplets that will be returned.
# 
# The trick is to move k and l around while k < l in the following way.
#
# 0. Initialize k and l as k = i + 1 and l = j - 1 respectively.
# 1. While k < l, use the pointers to create a quadruplet and evaluate its sum.
# 2. Compare the quadruplet sum with the target. 
# 3. If the quadruplet sum and the target are equal, add the quadruplet to the quadruplets list. 
#    Then, add 1 to k and substract 1 from l, so k and l move towards the center of the array.
#    Loop back to step 1 and continue.
# 3. If the quadruplet sum is less than the target, add 1 to k so it moves to one position to the right.
#    Thus pointing to a larger value. Loop back to step 1 and continue.
# 4. If the quadruplet sum is greater than the target, substract 1 from l so it moves to one position to the left.
#    Thus pointing to a smaller value. Loop back to step 1 and continue.
# 5. Once k == l it means that all the intermediate elements between those pointed by i and j have been
#    exhausted for this iteration. Move i and j as to their new positions and repeat the process from step 0 onwards.
# 
# If i and j have reached the end and the start of the array respectively, return the list of quadruplets we
# have been populating.
# 
# Solution 2 complexity:
# Time complexity: O(n^3) as we use 3 nested loops to produce candidate quadruplets from nums.
# Space complexity: O(n choose 4) as that is the max number of possible quadruplet combinations in nums.
def QuadrupletSumToTargetV2(nums, target):
    quadruplets = []
    n = len(nums)
    nums.sort()

    for i in range(n - 1):
        for j in range(n - 1, 0, -1):
            k = i + 1 # Left
            l = j - 1 # Right
            while k < l:
                quadruplet = sorted([nums[i], nums[j], nums[k], nums[l]])
                quadrupletSum = sum(quadruplet)
                
                if quadrupletSum == target:
                    if quadruplet not in quadruplets:
                        quadruplets.append(quadruplet)
                    k += 1
                    l -= 1
                elif quadrupletSum < target:
                    k += 1
                elif quadrupletSum > target:
                    l -= 1
    return quadruplets

def AreArraysEqual(array1, array2):
    if len(array1) != len(array2):
        return False

    for element in array1:
        if element not in array2:
            return False
    
    for element in array2:
        if element not in array1:
            return False
    
    return True

if __name__ == "__main__":
    # Example 1
    nums = [4, 1, 2, -1, 1, -3]
    target = 1
    expectedOutput = [[-3, -1, 1, 4], [-3, 1, 1, 2]]

    output = QuadrupletSumToTargetV2(nums, target)

    print(output)
    print(expectedOutput)
    print(AreArraysEqual(output, expectedOutput))

    # Example 2
    nums = [2, 0, -1, 1, -2, 2]
    target = 2
    expectedOutput = [-2, 0, 2, 2], [-1, 0, 1, 2]

    output = QuadrupletSumToTargetV2(nums, target)

    print(output)
    print(expectedOutput)
    print(AreArraysEqual(output, expectedOutput))
