# Problem:
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

class Solution:
    # Solution 1:
    # Given an integer x, loop through all the integers from 0 onwards until you find a number i such that i * i > x (this will happen one iteration after i is the square root).
    # Then, just return i - 1 as it is the square root. 
    #
    # Solution 1 complexity:
    # Time complexity: O(x) where x is the given number to extract the square root of.
    # Space complexity: O(1) constant space.
    def SqrtV1(self, x):
        i = 0
        while i * i <= x:
            i += 1
        return i - 1

    # Solution 2:
    # Altough, Solution 1 is easy to reason about. We can do a bit better in time complexity by using binary search to find the square root.
    #
    # Solution 2 complexity:
    # Time complexity: O(nlog(x)) where x is the given number to extract the square root of. This is due to the binary search nature of the search.
    # Space complexity: O(1) constant space.
    def SqrtV2(self, x):
        # Return early on the special cases of 0 and 1
        if x == 0 or x == 1:
            return x
        
        root = 0
        rootSquared = 0

        low = 2
        high = x // 2
        while low <= high:
            root = low + (high - low) // 2
            rootSquared = root * root

            if rootSquared == x:
                return root
            
            elif rootSquared > x:
                high = root - 1

            elif rootSquared < x:
                low = root + 1

        return high
    
    def Sqrt(self, x):
        return self.SqrtV2(x)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    num = 41
    expectedOutput = 6
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 2
    num = 36
    expectedOutput = 6
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 3
    num = 27
    expectedOutput = 5
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 4
    num = 25
    expectedOutput = 5
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 5
    num = 17
    expectedOutput = 4
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 6
    num = 8
    expectedOutput = 2
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 7
    num = 3
    expectedOutput = 1
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 8
    num = 2
    expectedOutput = 1
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 9
    num = 1
    expectedOutput = 1
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)
    
    # Example 10
    num = 0
    expectedOutput = 0
    output = solution.Sqrt(num)
    print(num, output, expectedOutput, output == expectedOutput)