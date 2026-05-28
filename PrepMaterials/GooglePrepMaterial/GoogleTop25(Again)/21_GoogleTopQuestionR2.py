# Jump Game
# MEDIUM
# https://scaleengineer.com/dsa/problems/jump-game

# Description
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your
# maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 
# Constraints:
#     1 <= nums.length <= 104
#     0 <= nums[i] <= 105

from collections import deque

# Time: O(n)
# Space: O(n)
def CanReachLastIndexBFS(nums):
    if not nums:
        return False
    
    n = len(nums)
    pending = [(0, nums[0])]

    while pending:
        index, jumps = pending.pop()

        if index == n - 1 or index + jumps == n - 1:
            return True
        
        for i in range(1, jumps + 1):
            pending.append((index + i, nums[index + i]))

    return False

# Time: O(n)
# Space: O(1)
def CanReachLastIndexGreedy(nums):
    if not nums:
        return False

    n = len(nums)
    jumps = 0 # Remaining jumps

    for i in range(n):
        if jumps < nums[i]:
            jumps = nums[i]

        if jumps > 0:
            jumps -= 1
        else:
            return False
        
    return True

def CanReachLastIndex(nums):
    return CanReachLastIndexGreedy(nums)

if __name__=="__main__":
    # Example 1:
    nums = [2,3,1,1,4]
    expected = True
    output = CanReachLastIndex(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nums = [3,2,1,0,4]
    expected = False
    output = CanReachLastIndex(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()
