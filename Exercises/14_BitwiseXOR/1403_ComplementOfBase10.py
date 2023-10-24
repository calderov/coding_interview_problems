# Problem: 
# Every non-negative integer N has a binary representation, for example, 8
# can be represented as “1000” in binary and 7 as “0111” in binary.
# 
# The complement of a binary representation is the number in binary that we
# get when we change every 1 to a 0 and every 0 to a 1. For example, the
# binary complement of “1010” is “0101”.
# 
# For a given positive number N in base-10, return the complement of its
# binary representation as a base-10 integer.
# 
# Examples:
# 
#   Input: 8
#   Output: 7
#   Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which
#   is 7 in base-10.
# 
#   Input: 10
#   Output: 5
#   Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which
#   is 5 in base-10.
# 

class Solution:
    # Solution:
    # Create a mask of bits, all set to 1 that is as long 
    # as the binary representation of the given number num.
    # Then, the complement of num can be computed as num XOR mask.
    # Return num XOR mask and finish.
    #
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def GetComplement(self, num):
        mask = 1

        while mask < num:
            mask = mask << 1
            mask += 1
        
        return mask ^ num


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    num = 8
    expectedOutput = 7
    output = solution.GetComplement(num)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    num = 10
    expectedOutput = 5
    output = solution.GetComplement(num)
    print(output, expectedOutput, output == expectedOutput)