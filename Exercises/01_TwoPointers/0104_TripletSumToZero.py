# Problem:
# Given an array of unsorted numbers, find all unique triplets in it that add to zero.

class Solution:
    # Solution 1:
    # Brute force the search by evaluating all the possible triplets and checking them to sum zero.
    #
    # Solution 1 complexity:
    # Time complexity: O(n3) as we use three nested loops for traversing nums.
    # Space complexity: O(n choose 3) as that is the max number of possible triplets in nums.
    def TripletSumToZeroV1(self, nums):
        triplets = []
        n = len(nums)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k \
                    and nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in triplets:
                            triplets.append(triplet)
        return sorted(triplets)

    # Solution 2:
    # Sort the input array to simplify the triplet search process.
    # Loop over the sorted nums picking one number X in each iteration and use two-pointers
    # to find two values Y and Z such that X + Y + Z = 0. Do this while skiping duplicate
    # elements to avoid duplicate triplets in the result. When a triplet (X, Y, Z) is found
    # push it into a triplets list. Once all the items have been traversed, return the triplets
    # list.
    #
    # Solution 2 complexity:
    # Time complexity: O(n2) as we use two nested loops for traversing nums.
    # Space complexity: O(n) as the triplets list can hold up to n/3 triplets.
    def TripletSumToZeroV2(self, nums):
        nums.sort()
        triplets = []
        n = len(nums)

        for i in range(n - 2):
            # Skip dupes!
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = n - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])

                    # Skip dupes!
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    right -= 1
                
        return triplets

    def TripletSumToZero(self, nums):
        return self.TripletSumToZeroV1(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [-3, 0, 1, 2, -1, 1, -2]
    expectedOutput = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    output = solution.TripletSumToZero(nums)
    print("Input:            ", nums)
    print("Zero Triplets:    ", output)
    print("Expected Triplets:", expectedOutput)
    print("Success:", output == expectedOutput)

    print()

    # Example 2
    nums = [-5, 2, -1, -2, 3]
    expectedOutput = [[-5, 2, 3], [-2, -1, 3]]
    output = solution.TripletSumToZero(nums)
    print("Input:            ", nums)
    print("Zero Triplets:    ", output)
    print("Expected Triplets:", expectedOutput)
    print("Success:", output == expectedOutput)

    print()

    # Example 3
    nums = [1, 0, -1, 1, 0, -1, 1, 0, -1]
    expectedOutput = [[-1, 0, 1], [0, 0, 0]]
    output = solution.TripletSumToZero(nums)
    print("Input:            ", nums)
    print("Zero Triplets:    ", output)
    print("Expected Triplets:", expectedOutput)
    print("Success:", output == expectedOutput)