# Problem:
# Any number will be called a happy number if, after repeatedly replacing it
# with a number equal to the sum of the square of all of its digits, leads us
# to number '1'.
#
# All other (not-happy) numbers will never reach '1'. Instead, they will be
# stuck in a cycle of numbers which does not include '1'.
#
# Examples:
# 23 is a happy number, 12 is not

class Solution:
    # Solution:
    # Add the squared digits of the number as stated in the problem description
    # but use the fast and slow approach to detect cycles, if a cycle is found
    # return False (as no cycles contain 1 in non-happy numbers). Otherwise
    # keep adding the digits until they converge to 1, then return True.
    # 
    # Solution complexity:
    # Time complexity: O(log(N)) where N is the given number
    # Space complexity: O(1)
    def IsHappyNumber(self, number):
        slow = number
        fast = number

        while True:
            slow = self.GetSquaredDigitsSum(slow)
            fast = self.GetSquaredDigitsSum(self.GetSquaredDigitsSum(fast))

            if fast == slow:
                return False

            if slow == 1 or fast == 1:
                return True
    
    def GetSquaredDigitsSum(self, number):
        squaredDigitsSum = 0

        while number > 0:
            digit = number % 10
            number //= 10 # number = int(number / 10)
            squaredDigitsSum += digit ** 2

        return squaredDigitsSum
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    number = 23
    expectedOutput = True
    output = solution.IsHappyNumber(number)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    number = 12
    expectedOutput = False
    output = solution.IsHappyNumber(number)
    print(output, expectedOutput, output == expectedOutput)
