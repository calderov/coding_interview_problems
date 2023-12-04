# Problem:
# Given a positive integer num, return true if num is a perfect square or
# false otherwise.
# 
# A perfect square is an integer that is the square of an integer. In other
# words, it is the product of some integer with itself.
# 
# You must not use any built-in library function, such as sqrt.
#
# Examples
# 
#   Input: 49
#   Expected Output: true
#   Justification: (7 * 7) equals 49.
#
#   Input: 55
#   Expected Output: false
#   Justification: There is no integer whose square is 55.
#
#   Input: 0
#   Expected Output: false
#   Justification: 0 is not considered a perfect square.
# 

class Solution:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def IsPerfectSquareV1(self, num):
        if num < 1: return False

        for i in range(1, num // 2 + 2):
            if i * i == num:
                return True
        return False
    
    def IsPerfectSquareV2(self, num):
        if num < 1:
            return False

        left = 1
        right = num // 2 

        while left <= right:
            midSquared = ((right - left) // 2) ** 2
            
            if midSquared == num:
                return True
            
            if midSquared < num:
                left += 1

            else: # midSquared > num:
                right -= 1

        return False
    
    def IsPerfectSquare(self, num):
        return self.IsPerfectSquareV2(num)

if __name__ == "__main__":
    solution = Solution()

    num = 49
    expectedOutput = True
    output = solution.IsPerfectSquare(num)
    print(output, expectedOutput, output == expectedOutput)

    num = 55
    expectedOutput = False
    output = solution.IsPerfectSquare(num)
    print(output, expectedOutput, output == expectedOutput)

    num = 0
    expectedOutput = False
    output = solution.IsPerfectSquare(num)
    print(output, expectedOutput, output == expectedOutput)
