# Problem:
# Given a non-negative integer represented as a string num and an integer k,
# delete k digits from num to obtain the smallest possible integer. Return
# this minimum possible integer as a string.
#
# Examples
#
#   Input: num = "1432219", k = 3
#   Output: "1219"
#   Explanation: The digits removed are 4, 3, and 2 forming the new
#                number 1219 which is the smallest.
#
#   Input: num = "10200", k = 1
#   Output: "200"
#   Explanation: Removing the leading 1 forms the smallest number 200.
#
#   Input: num = "1901042", k = 4
#   Output: "2"
#   Explanation: Removing 1, 9, 1, and 4 forms the number 2 which is
#               the smallest possible.
#

class Solution:
    # Solution:
    # 1. Initialize an empty stack.
    #
    # 2. For each digit in num:
    #    2.1  While k is greater than 0, the stack is not empty and the current
    #         digit is smaller than the top digit on the stack, pop the top digit
    #         from the stack and decrease k by 1.
    #
    #    2.2 Push the current digit onto the stack.
    #
    # 3. If k is still greater than 0, pop k digits from the stack.
    #
    # 4. Remove the leading zeros from the stack (those at the bottom).
    #
    # 5. If the stack is empty, return "0".
    #
    # 6. Otherwise, merge the stack from bottom to top into a result string.
    #
    # 7. Return the result string and finish.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def RemoveKDigits(self, num, k):
        stack = []

        # For each digit in num
        for i in range(len(num)):
            d = num[i]

            # While k is greater than 0, the stack is not empty and the current
            # digit is smaller than the top digit on the stack, pop the top digit
            # from the stack and decrease k by 1.
            while k > 0 and stack and int(d) < int(stack[-1]):
                stack.pop()
                k -= 1

            stack.append(d)

        # Add remaining digits
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Remove leading zeros
        while stack[0] == '0':
            stack.pop(0)

        # If stack is empty, return zero
        if not stack:
            return '0'

        return ''.join(stack)


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    num = "1432219"
    k = 3
    expectedOutput = "1219"
    output = solution.RemoveKDigits(num, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    num = "10200"
    k = 1
    expectedOutput = "200"
    output = solution.RemoveKDigits(num, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 3
    num = "1901042"
    k = 4
    expectedOutput = "2"
    output = solution.RemoveKDigits(num, k)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
