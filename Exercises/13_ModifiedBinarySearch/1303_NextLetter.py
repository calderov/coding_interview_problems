# Problem: 
# Given an array of lowercase letters sorted in ascending order, find the
# smallest letter in the given array greater than a given ‘key’.
# 
# Assume the given array is a circular list, which means that the last letter
# is assumed to be connected with the first letter. This also means that the
# smallest letter in the given array is greater than the last letter of the
# array and is also the first letter of the array.
# 
# Write a function to return the next letter of the given ‘key’.
# 
# Examples:
# 
#   Input: ['a', 'c', 'f', 'h'], key = 'f'
#   Output: 'h'
#   Explanation: The smallest letter greater than 'f' is 'h' in the given array.
# 
#   Input: ['a', 'c', 'f', 'h'], key = 'b'
#   Output: 'c'
#   Explanation: The smallest letter greater than 'b' is 'c'.
# 

class Solution:
    # Solution:
    # 1. Initialize 'left' and 'right' pointers.
    #    left = 0
    #    right = n - 1 (where n is the lenght of the letters array.)
    #
    # 2. While 'left' is less than or greater than 'right'.
    #
    #   2.1 Compute 'middle' pointer (that which stands between 'left' and 'right').
    #       middle = (left + right) // 2
    #
    #   2.2 If the letter at the 'middle' is greater than the key, move the 'right' pointer
    #       one position to the left of 'middle'.
    #
    #       Otherwise, move 'left' one position to the right of 'middle'.
    #
    # 3. At this point, the next letter after the key should be sitting on the 'left' pointer,
    #    but since 'left' may be pointing outside the range of the array, and the array is supposed
    #    to be treated as a circular list, then return the actual position of the next letter is
    #    left % n where n is the length of the letters array. Thus, return letters[left % n] and finish.
    #
    # Solution complexity:
    # Time complexity: O(log(n))
    # Space complexity: O(1)
    def NextLetter(self, letters, key):
        # Initialize 'left' and 'right' pointers
        left = 0
        right = len(letters) - 1

        # While 'left' is less than or greater than 'right'
        while left <= right:
            # Compute 'middle' pointer (that which stands between 'left' and 'right')
            mid = (right + left) // 2

            # If the letter at the 'middle' is greater than the key, move the 'right' pointer
            # one position to the left of 'middle'
            if letters[mid] > key:
                right = mid - 1
            
            # Otherwise, move 'left' one position to the right of 'middle'
            else: # letters[mid] <= key
                left = mid + 1

        # At this point, the next letter after the key should be sitting on the 'left' pointer,
        # but since 'left' may be pointing outside the range of the array, and the array is supposed
        # to be treated as a circular list, then return the actual position of the next letter is
        # left % n where n is the length of the letters array. Thus, return letters[left % n] and finish
        return letters[left % len(letters)]

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums = ['a', 'c', 'f', 'h']
    key = 'f'
    expectedOutput = 'h'
    output = solution.NextLetter(nums, key)
    print(output, expectedOutput, output == expectedOutput)
  
    # Example 2
    nums = ['a', 'c', 'f', 'h']
    key = 'b'
    expectedOutput = 'c'
    output = solution.NextLetter(nums, key)
    print(output, expectedOutput, output == expectedOutput)
  
    # Example 3
    nums = ['a', 'c', 'f', 'h']
    key = 'm'
    expectedOutput = 'a'
    output = solution.NextLetter(nums, key)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    nums = ['a', 'c', 'f', 'h']
    key = 'h'
    expectedOutput = 'a'
    output = solution.NextLetter(nums, key)
    print(output, expectedOutput, output == expectedOutput)
