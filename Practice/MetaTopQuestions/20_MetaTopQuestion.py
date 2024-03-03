# 50. Pow(x, n) (Medium)
# Implement pow(x, n), which calculates x raised to the power n (i.e., x ^ n).
# 
# Example 1:
#   Input: x = 2.00000, n = 10
#   Output: 1024.00000
# 
# Example 2:
#   Input: x = 2.10000, n = 3
#   Output: 9.26100
# 
# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
#  
# Constraints:
# - -100.0 < x < 100.0
# - -231 <= n <= 231-1
# - n is an integer.
# - Either x is not zero or n > 0.
# - -104 <= xn <= 104

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def powNaive(self, x, n):
        if n < 0:
            n = -1 * n
            x = 1 / x

        result = 1
        for _ in range(n):
            result *= x
        
        return result

    # Time complexity: O(log(n))
    # Time complexity: O(1)
    def pow(self, x, n):
        if n < 0:
            n = -1 * n
            x = 1 / x

        result = 1
        while n != 0:
            if n % 2 == 1:
                result *= x
                n -= 1

            x *= x
            n //= 2

        return result


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    x = 2.00000
    n = 10
    expectedOutput = 1024.00000
    output = round(solution.pow(x, n), 5)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    x = 2.10000
    n = 3
    expectedOutput = 9.26100
    output = round(solution.pow(x, n), 5)
    print(output, expectedOutput, output == expectedOutput)
    
    # Example 3
    x = 256
    n = 0
    expectedOutput = 1
    output = round(solution.pow(x, n), 5)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    x = 0.00001
    n = 2147483647
    expectedOutput = 0
    output = solution.pow(x, n)
    print(output, expectedOutput, output == expectedOutput)