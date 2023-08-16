# Problem:
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close
# to the target number as possible, return the sum of the triplet. If there are more than one such triplet,
# return the sum of the triplet with the smallest sum.
# 
# Example:
#  Input: [-1, 0, 2, 3], target=3 
#  Output: 2
#  Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

class Solution:
    # Solution 1:
    # Brute force the check of all the possible triplets and keeping track of their distance to the target.
    #
    # Solution 1 complexity:
    # Time complexity: O(n^3) as we use three nested loops to build all the possible triplets.
    # Space complexity: O(1) as we rely only on a few auxiliar variables.
    def TripletSumCloseToTargetV1(self, nums, target):
        closestSum = nums[0] + nums[1] + nums[2]
        targetDistance = target - closestSum
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        currentSum = nums[i] + nums[j] + nums[k]
                        currentTargetDistance = target - currentSum
                        if abs(currentTargetDistance) < abs(targetDistance):
                            closestSum = currentSum
                            targetDistance = currentTargetDistance
                            continue
                        if abs(currentTargetDistance) == abs(targetDistance):
                            if currentSum < closestSum:
                                closestSum = currentSum
                                targetDistance = currentTargetDistance

        return closestSum


    # Solution 2:
    # Sort the input array and loop over the sorted numbers. In each iteration pick one number and use two-pointers
    # to find two other numbers such that the sum of the three equals the target. If no three numbers add up to the
    # target on a given iteration, keep track of the closest sum and the closest distance to the target found so far. 
    # If the current sum of a given iteration is at the same distance to the target than the closest sum,
    # replace the closest sum with the current one if the current one is less than the closest sum.
    #  
    # Solution 2 complexity:
    # Time complexity: O(n^2) as we use two nested loops to build candidate triplets.
    # Space complexity: O(1) as we rely only on a few auxiliar variables that take constant space.
    def TripletSumCloseToTargetV2(self, nums, target):
        nums.sort()
        n = len(nums)

        closestSum = nums[0] + nums[1] + nums[2]
        closestDistance = target - closestSum

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                distance = target - currentSum

                if currentSum == target:
                    return currentSum
                elif currentSum < target:
                    left += 1
                elif currentSum > target:
                    right -= 1

                if abs(distance) < abs(closestDistance):
                    closestSum = currentSum
                    closestDistance = distance
                elif abs(distance) == abs(closestDistance) and currentSum < closestSum:
                    closestSum = currentSum
                    closestDistance = distance

        return closestSum

    def TripletSumCloseToTarget(self, nums, target):
        return self.TripletSumCloseToTargetV2(nums, target)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [-1, 0, 2, 3]
    target = 3 
    expectedOutput = 2
    output = solution.TripletSumCloseToTarget(nums, target)
    print("Input array:    ", nums)
    print("Target:         ", target)
    print("Output:         ", output)
    print("Expected output:", expectedOutput)
    print("Success:        ", output == expectedOutput)
    print()

    # Example 2
    nums = [-3, -1, 1, 2]
    target = 1
    expectedOutput = 0
    output = solution.TripletSumCloseToTarget(nums, target)
    print("Input array:    ", nums)
    print("Target:         ", target)
    print("Output:         ", output)
    print("Expected output:", expectedOutput)
    print("Success:        ", output == expectedOutput)
    print()

    # Example 3
    nums = [1, 0, 1, 1]
    target = 100
    expectedOutput = 3
    output = solution.TripletSumCloseToTarget(nums, target)
    print("Input array:    ", nums)
    print("Target:         ", target)
    print("Output:         ", output)
    print("Expected output:", expectedOutput)
    print("Success:        ", output == expectedOutput)
    print()

    # Example 4
    nums = [0, 0, 1, 1, 2, 6]
    target = 5
    expectedOutput = 4
    output = solution.TripletSumCloseToTarget(nums, target)
    print("Input array:    ", nums)
    print("Target:         ", target)
    print("Output:         ", output)
    print("Expected output:", expectedOutput)
    print("Success:        ", output == expectedOutput)
    print()
