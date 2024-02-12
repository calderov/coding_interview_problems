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

def WaterCapacity(elevation):
    n = len(elevation)

    maxLeft  = [0] * n # Largest elevation so far form the left
    maxRight = [0] * n # Largest elevation so far form the right
    water = [0] * n

    for i in range(1, n):
        maxLeft[i] = max(maxLeft[i - 1], elevation[i - 1])

        j = n - 1 - i
        maxRight[j] = max(maxRight[j + 1], elevation[j + 1])

    for i in range(n):
        potential = min(maxLeft[i], maxRight[i])
        water[i] = max(potential - elevation[i], 0)

    return sum(water)

if __name__ == "__main__":
    elevation = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    expectedOutput = 6
    output = WaterCapacity(elevation)
    print(output, expectedOutput, output == expectedOutput)
