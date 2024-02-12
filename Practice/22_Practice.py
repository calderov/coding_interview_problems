# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
# Example:
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
# 3 |               ■        
# 2 |       ■ □ □ □ ■ ■ □ ■  
# 1 |   ■ □ ■ ■ □ ■ ■ ■ ■ ■ ■
#   + - - - - - - - - - - - -
#     0 1 0 2 1 0 1 3 2 1 2 1
#
# Explanation: The above elevation map (black section) is represented by
# array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
# section) are being trapped.

def IsAllZeros(nums):
    for num in nums:
        if num != 0:
            return False
    return True

def GetNonZeroIndexes(nums):
    indexes = []

    for i in range(len(nums)):
        if nums[i] != 0:
            indexes.append(i)

    return indexes

def WaterCapacity(elevationArray):
    water = 0

    while not IsAllZeros(elevationArray):
        nonZeroIndexes = GetNonZeroIndexes(elevation)
    
        # Compute water at the bottom
        for i in range(len(nonZeroIndexes) - 1):
            left = nonZeroIndexes[i]
            right = nonZeroIndexes[i + 1]

            water += right - left - 1

        # Reduce the elevation by one layer
        for i in range(len(elevationArray)):
            elevationArray[i] = max(elevationArray[i] - 1, 0)

    return water

if __name__ == "__main__":
    elevation = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expectedOutput = 6
    output = WaterCapacity(elevation)
    print(output, expectedOutput, output == expectedOutput)
