# Trapping Rain Water
# HARD
# https://docs.google.com/document/d/1HD03095RdpTRL9z4B0qGvHgQCraJUksNtaHWQLLeQkQ/edit?tab=t.0

# Description
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
# can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation:

# 3|
# 2|              #
# 1|      # W W W # # W #
# 0|  # W # # W # # # # # #
# --------------------------
#  |0 1 0 2 1 0 1 3 2 1 2 1

# The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2:
# Input: height = [4,2,0,3,2,5]
# Output: 9

# Constraints:
#     n == height.length
#     1 <= n <= 2 * 104
#     0 <= height[i] <= 105

# Time: O(n)
# Space: O(n)
def TrappedWaterV1(height):
    if not height:
        return 0

    n = len(height)

    leftToRight = [0] * n
    rightToLeft = [0] * n
    
    # Compute max heights from left to right
    maxH = 0
    for i in range(n):
        maxH = max(maxH, height[i])
        leftToRight[i] = maxH

    # Compute max heights from right to left
    maxH = 0
    for i in range(n - 1, -1, -1):
        maxH = max(maxH, height[i])
        rightToLeft[i] = maxH

    water = 0
    for i in range(1, n - 1):
        water += max(0, min(leftToRight[i], rightToLeft[i]) - height[i])
    
    return water

def TrappedWaterV2(height):
    if not height:
        return 0
    
    n = len(height)
    
    left = 0
    right = n - 1

    maxLeft = 0
    maxRight = 0

    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                water += maxLeft - height[left]
            left += 1
        
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                water += maxRight - height[right]
            right -= 1
    
    return water

def TrappedWater(height):
    return TrappedWaterV2(height)


if __name__ == "__main__":
    # Example 1:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    expected = 6
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    height = [4,2,0,3,2,5]
    expected = 9
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()