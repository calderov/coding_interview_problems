# Problem: 
# You are given a string s and an integer k. Your task is to remove groups of
# identical, consecutive characters from the string such that each group has
# exactly k characters. The removal of groups should continue until it's no
# longer possible to make any more removals. The result should be the final
# version of the string after all possible removals have been made.
# 
# Examples
# 
#   Input: s = "abbbaaca", k = 3
#   Output: "ca"
#   Explanation: First, we remove "bbb" to get "aaaca". Then, we remove
#                "aaa" to get "ca".
#
#   Input: s = "abbaccaa", k = 3
#   Output: "abbaccaa"
#   Explanation: There are no instances of 3 adjacent characters being
#                the same.
#
#   Input: s = "abbacccaa", k = 3
#   Output: "abb"
#   Explanation: First, we remove "ccc" to get "abbaaa". Then, we
#                remove "aaa" to get "abb".
# 

class Solution:
    # Solution:
    # 1. Initialize an empty stack.
    #    stack = []
    #
    # 2. For each character c in the input string s:
    #
    #    2.1 Push c into the stack.
    #
    #    2.1 If the size of the stack is greater or equal than k, check if the
    #        last k elements of the stack are repetitions. If so, pop the stack
    #        k times.
    #
    # 3. Merge the characters in the stack from bottom to top into an output string.
    #
    # 4. Return the output string and finish.
    #
    # Solution complexity:
    # Time complexity: O(k * n)
    # Space complexity: O(n)
    def RemoveKDuplicates(self, s, k):
        stack = []

        for c in s:
            stack.append(c)
            
            if stack and len(stack) >= k:
                substack = stack[-k:]
                
                repetitions = 0
                for i in range(k):
                    if substack[0] == substack[i]:
                        repetitions += 1
                        continue
                    break

                if repetitions == k:
                    for i in range(k):
                        stack.pop()

        return ''.join(stack)

if __name__ == "__main__":
    solution = Solution()

    # Example
    s = "abbbaaca"
    k = 3
    expectedOutput = "ca"
    output = solution.RemoveKDuplicates(s, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example
    s = "abbaccaa"
    k = 3
    expectedOutput = "abbaccaa"
    output = solution.RemoveKDuplicates(s, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example
    s = "abbacccaa"
    k = 3
    expectedOutput = "abb"
    output = solution.RemoveKDuplicates(s, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
