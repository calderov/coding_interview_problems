# Combinations
# MEDIUM

# Description
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

# Constraints:
#     1 <= n <= 20
#     1 <= k <= n

# Time: O(k * C(n, k))
# Space: O(k)
def GetCombinations(n, k):
    combinations = []

    def Backtrack(start, current):
        if len(current) == k:
            combinations.append([x for x in current])
            return

        for i in range(start, n + 1):
            current.append(i)
            Backtrack(i + 1, current)
            current.pop()

        return
    
    Backtrack(1, [])

    return combinations

if __name__ == "__main__":
    # Example 1:
    n = 4
    k = 2
    expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    output = GetCombinations(n, k)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    n = 1
    k = 1
    expected = [[1]]
    output = GetCombinations(n, k)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    n = 3
    k = 2
    expected = [[1, 2], [1, 3], [2, 3]]
    output = GetCombinations(n, k)
    print(expected)
    print(output)
    print(expected == output)
    print()