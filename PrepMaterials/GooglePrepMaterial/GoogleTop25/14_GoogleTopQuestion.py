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
        leftToRight[i] = maxH
        maxH = max(maxH, height[i])

    # Compute max heights from right to left
    maxH = 0
    for i in range(n - 1, -1, -1):
        rightToLeft[i] = maxH
        maxH = max(maxH, height[i])

    water = 0
    for i in range(1, n - 1):
        water += max(0, min(leftToRight[i], rightToLeft[i]) - height[i])
    
    return water

# Time: O(n)
# Space: O(1)
def TrappedWaterV2(height):
    if not height:
        return 0

    n = len(height)

    left = 0
    right = n - 1

    maxLeft = height[left]
    maxRight = height[right]

    water = 0

    while left < right:
        if maxLeft < maxRight:
            left += 1
            maxLeft = max(maxLeft, height[left])
            water += maxLeft - height[left]
        else:
            right -= 1
            maxRight = max(maxRight, height[right])
            water += maxRight - height[right]

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

    # Example 3: Simple two-bar trap
    height = [3,0,2]
    expected = 2
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: Ascending (no water trapped)
    height = [1,2,3,4,5]
    expected = 0
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Descending (no water trapped)
    height = [5,4,3,2,1]
    expected = 0
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: Single bar
    height = [1]
    expected = 0
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 7: All zeros
    height = [0,0,0]
    expected = 0
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 8: Mountain shape
    height = [3,2,1,2,3]
    expected = 4
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 9: Multiple valleys
    height = [3,0,0,2,0,4]
    expected = 10
    output = TrappedWater(height)
    print(expected)
    print(output)
    print(expected == output)
    print()