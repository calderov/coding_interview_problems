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

# Solution:
# Start with an empty list of results and an empty combination.
#
# Iterate through the candidates array, adding each candidate to the current
# combination and recursively call the function with the updated combination
# and remaining target.
#
# If the target becomes 0, we add the current combination to the result list.
# If the target becomes negative, we backtrack and remove the last added candidate
# from the combination.
#
# Once this finishes, return the results list.
#
# Time complexity: O(n ^ (t / m + 1)) where: n is the number of elements in the input, 
#                                            t is the target number, 
#                                            m is the smallest number in the input
# Space complexity: O(t / n)
class Solution:
    def CombinationSum(self, candidates, target):
        result = []
        self.Backtrack(candidates, target, 0, [], result)
        return result
    
    def Backtrack(self, candidates, target, start, combination, result):
        # If the target is 0, we found a valid combination,
        # append a copy of this combination to the result
        if target == 0:
            result.append(list(combination)) # Cast to list to ensure a new copy
            return
        
        # Iterate through the candidates array, starting from the given index
        for i in range(start, len(candidates)):
            # If the current candidate is greater than the remaining target, 
            # move on to the next candidate
            if candidates[i] > target:
                continue

            # Otherwise, add the candidate to the current combination
            combination.append(candidates[i])

            # Recursively call the function with the updated combination and remaining target
            self.Backtrack(candidates, target - candidates[i], i, combination, result)

            # Backtrack by removing the last added candidate from the combination
            combination.pop()

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
