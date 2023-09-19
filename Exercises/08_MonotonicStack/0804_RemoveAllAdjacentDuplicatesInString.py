# Problem:
# Given a string S, remove all adjacent duplicate characters recursively to
# generate the resultant string.
#
# Examples
#
#   Input: s = "abccba"
#   Output: ""
#   Explanation: First, we remove "cc" to get "abba". Then, we remove
#                "bb" to get "aa". Finally, we remove "aa" to get an
#                empty string.
#
#   Input: s = "foobar"
#   Output: "fbar"
#   Explanation: We remove "oo" to get "fbar".
#
#   Input: s = "abcd"
#   Output: "abcd"
#   Explanation: No adjacent duplicates so no changes.
#

class Solution:
    # Solution:
    # 1. Initialize an empty stack.
    #    stack = []
    #
    # 2. For each character C in the string S, check if the top item on the
    #    stack equals C. If so, pop the stack, otherwise, push C into the stack.
    #
    # 3. Return and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def RemoveAdjacentDuplicates(self, s):
        stack = []

        for i in range(len(s)):
            if stack and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    s = "abccba"
    expectedOutput = ""
    output = solution.RemoveAdjacentDuplicates(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    s = "foobar"
    expectedOutput = "fbar"
    output = solution.RemoveAdjacentDuplicates(s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    s = "abcd"
    expectedOutput = "abcd"
    output = solution.RemoveAdjacentDuplicates(s)
    print(output, expectedOutput, output == expectedOutput)

