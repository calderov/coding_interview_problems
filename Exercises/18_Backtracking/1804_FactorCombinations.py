# Problem:
# Numbers can be regarded as the product of their factors.
#
# For example:
#
#   8 = 2 x 2 x 2
#   8 = 2 x 4
#
# Given an integer n, return all possible combinations of its factors. You
# may return the answer in any order.
# Examples:
#
#   Input: n = 8
#   Output: [[2, 2, 2], [2, 4]]
# 
#   Input: n = 20
#   Output: [[2, 2, 5], [2, 10], [4, 5]]
#
class Solution:
    # Solution:
    # 1. Given a target number to factor n, a list of candidate factors (candidates), the current
    #    product of such candidates (candidatesProduct) and a list to hold the results (results).
    #    Pass them as arguments to the FindFactors function.
    #
    # 2. In The FindFactors function, iterate over all the integers from 2 to n, considering each number i
    #    as a candidate factor of n if n % i == 0.
    #
    # 3. Append this number i to the list of candidates and update the candidatesProduct to account for i:
    #
    #    candidatesProduct = candidatesProduct * i
    #
    # 4. If the candidatesProduct becomes greater than n, remove i from the candidates list and return.
    #
    # 5. If the candidatesProduct is equal to n, we have found that our candidates list holds a valid set of factors of n,
    #    add a copy of the candidates list to the results (take care so the results list does not contain duplicate
    #    combinations).
    #
    # 6. Recursively, call FindFactors with the updated parameters for candidates, candidatesProduct and results.
    #    This will make it propose new candidates.
    #
    # 7. Backtrack, by dividing the candidates product by i, and removing i from the candidates list (just pop the last
    #    item of the list).
    #
    # 8. Increase i by 1 and iterate once again.
    #
    # Solution complexity:
    # Time complexity: O(n ^ 2)
    # Space complexity: O(log (n)) Ignoring the space required for the results list.
    def FactorCombinations(self, n):
        results = []
        self.FindFactors(n, [1], 1, results)
        return results

    def FindFactors(self, n, candidates, candidatesProduct, results):
        i = 2
        while i < n:
            if n % i != 0:
                i += 1
                continue

            candidatesProduct *= i
            candidates.append(i)

            if candidatesProduct > n:
                candidates.pop()
                return

            if candidatesProduct == n:
                validCandidate = sorted(candidates[1:])
                if validCandidate not in results:
                    results.append(validCandidate)

            self.FindFactors(n, candidates, candidatesProduct, results)

            candidatesProduct //= i
            candidates.pop()

            i += 1

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    n = 8
    expectedOutput = [[2, 2, 2], [2, 4]]
    output = solution.FactorCombinations(n)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2:
    n = 20
    expectedOutput = [[2, 2, 5], [2, 10], [4, 5]]
    output = solution.FactorCombinations(n)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3:
    n = 9
    expectedOutput = [[3, 3]]
    output = solution.FactorCombinations(n)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)