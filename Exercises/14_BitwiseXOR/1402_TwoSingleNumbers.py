# Problem:
# In a non-empty array of numbers, every number appears exactly twice except
# two numbers that appear only once. Find the two numbers that appear only
# once.
# 
# Examples:
# 
#   Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
#   Output:[4, 6]
# 
#   Input: [2, 1, 3, 2]
#   Output:[1, 3]
# 

class Solution:
    # Solution:
    # Use a hash map to count the frequencies of each value
    # and return a list of those values with just once instance.
    #
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def TwoSingleNumbersV1(self, nums):
        n = len(nums)
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1

        singles = []
        for key in frequencies:
            if frequencies[key] == 1:
                singles.append(key)

        return singles
    
    # Solution:
    # Let num1 and num2 represent the two singles present in the
    # input array. 
    #
    # Since num1 != num2 by definition, then the XOR of all the numbers
    # in the array (xorAllNums) must be equal to num1 XOR num2, as all the
    # other numbers in the array will cancel out with their duplicate.
    #
    # Then, num1 and num2 can be derived from xorAllNums by using a bit
    # in xorAllNums set to 1 as a discriminator. For the sake of convenience
    # let this be the right most bit in xorAllNums that is set to 1, lets
    # call it rightMostBit.
    #
    # As we mentioned, rightMostBit can be used to infer num1 and num2.
    # Since rightMostBit comes from xorAllNums, and xorAllNums = num1 xor num2,
    # then num1 and num2 differ at the bit position that corresponds to rightMostBit.
    # Thus, the XOR of all the nums that have that bit set to 0 must equal num1 (by convention)
    # and the XOR of all the nums that have that bit set to 1 must equal num2.
    # 
    # In other words, num1 and num2 can be computed as:
    #
    #   num1 = XOR({n in nums such that n XOR rightMostBit == 0})
    #   num2 = XOR({n in nums such that n XOR rightMostBit == 1})
    # 
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def TwoSingleNumbersV2(self, nums):
        n = len(nums)

        # Compute the XOR of all the numbers in the input array
        xorAllNums = 0
        for num in nums:
            xorAllNums = xorAllNums ^ num
        
        # Get the right most bit of xorAllNums that is set to 1
        rightMostBit = 1
        while rightMostBit & xorAllNums == 0:
            rightMostBit = rightMostBit << 1
        
        # Compute num1 and num2
        num1 = 0
        num2 = 0
        for num in nums:
            if rightMostBit & num != 0: # The bit is set
                num1 = num1 ^ num
            else:
                num2 = num2 ^ num
        
        return sorted([num1, num2])

    def TwoSingleNumbers(self, nums):
        return self.TwoSingleNumbersV2(nums)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
    expectedOutput = [4, 6]
    output = solution.TwoSingleNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [2, 1, 3, 2]
    expectedOutput = [1, 3]
    output = solution.TwoSingleNumbers(nums)
    print(output, expectedOutput, output == expectedOutput)
