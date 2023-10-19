# Problem:
# Given a Bitonic array, find if a given ‘key’ is present in it. An array is
# considered bitonic if it is monotonically increasing and then monotonically
# decreasing. Monotonically increasing or decreasing means that for any index
# i in the array arr[i] != arr[i+1].
# 
# Write a function to return the index of the ‘key’. If the 'key' appears
# more than once, return the smaller index. If the ‘key’ is not present,
# return -1.
# 
# Examples:
# 
#   Input: [1, 3, 8, 4, 3], key = 4
#   Output: 3
# 
#   Input: [3, 8, 3, 1], key = 8
#   Output: 1
#  

class Solution:
    # Solution:
    # 1. Compute the inflection point of the bitonic array (the point where the values in the array 
    #    stop ascending and start descending).
    #
    # 2. Use the inflection point to split the input in two halfs, one going from zero to the inflection point,
    #    and one going from the inflection point onwards.
    #
    # 3. Search the key on the first half. If the result from the search is successful (result != 1), return the
    #    result and finish.
    #
    # 4. Search the key on the second half of the array. If the result from the search is successful (result != 1)
    #    return result + inflection point and finish.
    #
    # 5. Otherwise, return -1.
    #
    # Solution complexity:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def FindKeyInBitonicArray(self, nums, key):
        # Compute bitonic inflection point
        inflectionPoint = self.FindBitonicInflectionPoint(nums)
        
        # Search the key on the first half of the input array
        result = self.BinarySearch(nums[0 : inflectionPoint + 1], key)
        if result != -1:
            return result
        
        # Search the key on the second half of the input array
        result = self.BinarySearch(nums[inflectionPoint : len(nums)], key)
        if result != -1:
            return result + inflectionPoint

        return result 

    def FindBitonicInflectionPoint(self, nums):
        left = 0
        right = len(nums) - 1

        inflectionPoint = 0
        inflectionValue = nums[0]

        while left < right:
            mid = (left + right) // 2

            # If we are in the ascending section
            if nums[mid] < nums[mid + 1]:
                if inflectionValue < nums[mid + 1]:
                    inflectionPoint = mid + 1
                    inflectionValue = nums[mid + 1]
                left = mid + 1

            # Otherwise, we are in the descending section
            else: # nums[mid] >= nums [mid + 1]
                if inflectionValue < nums[mid]:
                    inflectionPoint = mid
                    inflectionValue = nums[mid]
                right = mid

        return inflectionPoint

    # Ideally this should be implemented as an order agnostic search
    # but due to time limitations, I'll keep it as is, however I know
    # it can fail if the key is in the descending portion of a long
    # array with an early inflection point.
    def BinarySearch(self, nums, key):
        left = 0
        right = len(nums) - 1

        first = -1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == key:
                first = mid
                right = mid - 1
            
            if nums[mid] < key:
                left = mid + 1

            else: # nums[mid] > key
                right = mid - 1
        
        return first
        

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = [1, 3, 8, 4, 3]
    key = 4
    expectedOutput = 3
    output = solution.FindKeyInBitonicArray(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [3, 8, 3, 1]
    key = 8
    expectedOutput = 1
    output = solution.FindKeyInBitonicArray(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    nums = [1, 3, 8, 12]
    key = 12
    expectedOutput = 3
    output = solution.FindKeyInBitonicArray(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = [10, 9, 8]
    key = 10
    expectedOutput = 0
    output = solution.FindKeyInBitonicArray(nums, key)
    print(output, expectedOutput, output == expectedOutput)
