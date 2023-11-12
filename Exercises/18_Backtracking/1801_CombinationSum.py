# Problem:
# Given an array of distinct positive integers candidates and a target
# integer target, return a list of all unique combinations of candidates
# where the chosen numbers sum to target. You may return the combinations in
# any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen
# numbers is different.
#
# Example 1:
#
# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Explanation: The elements in these two combinations sum up to 7.
#
# Example 2:
#
# Input: candidates = [2, 4, 6, 8], target = 10
# Output: [[2,2,2,2,2], [2,2,2,4], [2,2,6], [2,4,4], [2,8], [4,6]]
# Explanation: The elements in these six combinations sum up to 10.

class Solution:
    # Solution:
    # Brute force approach, generate all the subsets of the input candidates set
    # and pick those which match the target value. In the evaluation of subsets
    # we can prune those which sum is greater than the target.
    #
    # Time complexity: O(2 ^ n)
    # Space complexity: O(2 ^ n)
    def CombinationSum(self, candidates, target):
        visitedSubsets = [[]]
        resultSubsets = []

        for num in candidates:
            subsets = visitedSubsets

            for prevSubset in subsets:
                subset = prevSubset + [num]
                sumSubset = sum(subset)

                if sumSubset == target:
                    resultSubsets.append(subset)

                elif sumSubset < target:
                    visitedSubsets.append(subset)

        return resultSubsets

def AreEqual(list1, list2):
    if len(list1) != len(list2):
        return False

    for item in list1:
        if item not in list2:
            return False

    for item in list2:
        if item not in list1:
            return False

    return True

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    candidates = [2, 3, 6, 7]
    target = 7
    expectedOutput = [[2, 2, 3], [7]]
    output = solution.CombinationSum(candidates, target)
    print(output)
    print(expectedOutput)
    print(AreEqual(output, expectedOutput))
    print()

    # Example 2
    candidates = [2, 4, 6, 8]
    target = 10
    expectedOutput = [[2,2,2,2,2], [2,2,2,4], [2,2,6], [2,4,4], [2,8], [4,6]]
    output = solution.CombinationSum(candidates, target)
    print(output)
    print(expectedOutput)
    print(AreEqual(output, expectedOutput))
