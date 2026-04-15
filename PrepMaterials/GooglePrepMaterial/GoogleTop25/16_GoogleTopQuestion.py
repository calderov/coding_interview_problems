# Jump Game II
# MEDIUM
# https://scaleengineer.com/dsa/problems/jump-game-ii

# Description
# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#     0 <= j <= nums[i] and
#     i + j < n

# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
 
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

# Example 2:
# Input: nums = [2,3,0,1,4]
# Output: 2

# Constraints:
#     1 <= nums.length <= 104
#     0 <= nums[i] <= 1000
#     It's guaranteed that you can reach nums[n - 1].

from collections import deque

# Time: O(n)
# Space: O(n)
def MinJumpsBFS(nums):
    # Track visited indices
    visited = set()

    # Track min number of jumps required to reach the current index    
    pending = deque([(0, 0)])

    while pending:
        minJumps, index = pending.popleft()
        
        if index == len(nums) - 1:
            return minJumps

        visited.add(index)

        for i in range(1, nums[index] + 1):
            nextIndex = index + i
            nextMinJumps = minJumps + 1
            if nextIndex < len(nums) and nextIndex not in visited:
                pending.append((nextMinJumps, nextIndex))

    return -1  

# Time: O(n)
# Space: O(1)
def MinJumpsGreedy(nums):
    if len(nums) == 1:
        return 0
    
    jumps = 0
    farthest = 0
    currentIndex = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == currentIndex:
            currentIndex = farthest
            jumps += 1

            if farthest >= len(nums) - 1:
                break
    
    return jumps

def MinJumps(nums):
    return MinJumpsGreedy(nums)

if __name__ == "__main__":
    # Example 1:
    nums = [2,3,1,1,4]
    expected = 2
    output = MinJumps(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nums = [2,3,0,1,4]
    expected = 2
    output = MinJumps(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 3: Single element
    nums = [0]
    expected = 0
    output = MinJumps(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 4: Simple linear jumps
    nums = [1,1,1,1]
    expected = 3
    output = MinJumps(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 5: Jump over zeros
    nums = [1,1,2,0,1]
    expected = 3
    output = MinJumps(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 6: Large jump
    nums = [3,2,1]
    expected = 1
    output = MinJumps(nums)
    print(expected)
    print(output)
    print(expected == output)
    print()