# Problem:
# Given a set of numbers that might contain duplicates, find all of its
# distinct subsets.
#
# Examples:
#
#   Input: [1, 3, 3]
#   Output: [], [1], [3], [1,3], [3,3], [1,3,3]
#
#   Input: [1, 5, 3, 3]
#   Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3],
#           [3,3,5], [1,5,3,3]
#

class Solution:
    # Solution:
    # 1. Let nums be the array of numbers that we receive as input.
    #
    # 2. Sort nus so numbers are processed in order (optional).
    #
    # 3. For num in nums.
    #
    #    3.1 Let n be the length of the current subsets list.
    #
    #    3.2 For i in [0, n).
    #
    #        3.2.1 Create a new subset by appending num to the end of
    #              the ith element in the subsets list.
    #
    #        3.2.2 If the new subset is not already in the subsets list,
    #              append it at the end of the subsets list.
    #
    # 4. Sort subsets by cardinality (optional).
    #
    # 5. Return subsets list and finish.
    #
    # Solution complexity:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(n)
    def AllSets(self, nums):
        # Sort nums so numbers are processed in order (optional)
        nums.sort()

        # Initialize the subsets list and add the empty set to it
        subsets = [[]]

        # For num in nums
        for num in nums:
            # Let n be the length of the current subsets list
            n = len(subsets)

            # For i in [0, n)
            for i in range(n):
                # Create a new subset by appending num to the end of
                # the ith element in the subsets list. 
                newSubset = subsets[i] + [num]

                # If the new subset is not already in the subsets list,
                # append it at the end of the subsets list
                if newSubset not in subsets:
                    subsets.append(newSubset)

        # Sort subsets by cardinality (optional)
        subsets.sort(key=lambda x: len(x))
        
        # Return subsets list and finish.
        return subsets

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 3, 3]
    expectedOutput = [[], [1], [3], [1, 3], [3, 3], [1, 3, 3]]
    output = solution.AllSets(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    nums = [1, 5, 3, 3]
    expectedOutput = [[], [1], [3], [5], [1, 3], [3, 3], [1, 5], [3, 5], [1, 3, 3], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]]
    output = solution.AllSets(nums)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()