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
# 1. Sort the list of nums to aid in finding quadruplets efficiently.
# 2. Two nested loops traverse the first two elements of the potential quadruplet.
# 3. At each iteration of the first two elements, maintain two pointers, left and right, for the remaining elements.
#    While left is less than right, explore combinations of the third and fourth elements.
#    adjusting left and right pointers based on the comparison of the current sum with the target:
#       - If the sum matches the target, a quadruplet is found. Add the quadruplet to a list.
#         Increment left and decrement right while skipping duplicates.
#       - If the sum is less, increment left to consider larger values.
#       - If the sum is more, decrement right to consider smaller values.
# 4. When the first two pointers have finished traversing the array, return the list of quadruplets that matched the target.

# Solution 2 complexity:
# Time complexity: O(n^3) as we use 3 nested loops to produce candidate quadruplets from nums.
# Space complexity: O(n choose 4) as that is the max number of possible quadruplet combinations in nums.
def QuadrupletSumToTargetV2(nums, target):
    quadruplets = []
    n = len(nums)
    nums.sort()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            k = j + 1 # Left
            l = n - 1 # Right

            while k < l:
                quadrupletSum = nums[i] + nums[j] + nums[k] + nums[l]

                if quadrupletSum == target:
                    quadruplets.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    # Skip dupes
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
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
