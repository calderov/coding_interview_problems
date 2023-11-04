# Problem: 
# Given a set with distinct elements, find all of its distinct subsets.
# 
# Examples:
# 
#   Input: [1, 3]
#   Output: [], [1], [3], [1,3]
# 
#   Input: [1, 5, 3]
#   Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
# 

class Solution:
    # Solution:
    # 1. Initialize a subsets list to serve as our result and add the empty set to it.
    #      subsets = [[]]
    #
    # 2. For each num in nums. 
    #
    #   2.1 Let n be the length the current subsets list.
    #
    #   2.2 For i in [0, n). Create a new subset by appending num
    #       to the end of the ith element in the subsets list. 
    #       Then, append this new subset at the end of the subsets
    #       list.
    #
    # 3. Sort the subsets list (optional).
    #
    # 4. Return subsets list and finish.
    # 
    # Solution complexity:
    # Time complexity: O(n * 2 ^ n)
    # Space complexity: O(n * 2 ^ n)
    def AllSubsets(self, nums):
        # Add the empty set
        subsets = [[]]

        # For each num in nums
        for num in nums:
            # Let n be the length the current subsets list
            n = len(subsets)

            # For i in [0, n)
            for i in range(n):
                # Create a new subset by appending num to the end of
                # the ith element in the subsets list. Then, append
                # this new subset at the end of the subsets list
                subsets.append(subsets[i] + [num])

        # Sort the subsets list (optional)
        subsets.sort(key=lambda x: len(x))

        # Return subsets list and finish
        return subsets

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 3]
    expectedOutput = [[], [1], [3], [1,3]]
    output = solution.AllSubsets(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [1, 5, 3]
    expectedOutput = [[], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]]
    output = solution.AllSubsets(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
