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
    def find(self, number):
        return self.IsHappyNumber(number)

    # Solution:
    # Solution complexity:
    # Time complexity: O*
    # Space complexity:
    def IsHappyNumber(self, number):
        # Return early for negative numbers
        if number < 0:
            return False

        visited = set()

        while True:
            if number == 1:
                return True
            
            if number in visited:
                return False
            
            visited.add(number)
            number = sum([i * i for i in self.GetDigits(number)])
    
    def GetDigits(self, number):
        return [int(i) for i in str(number)] 
    
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
