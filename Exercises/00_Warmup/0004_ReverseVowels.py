# Problem:
# Given a string s, reverse all the vowels in the string and return it.
# For example:
# - An input string "Hello" should return "Holle".
# - An input string "AEIOU" should return "UOIEA".
# - An input string "DesignGurus" should return "DusugnGires".

class Solution:
    # Solution:
    # First, copy the input string into a list of characters. We do this so we can manipulate this list in place, as Python strings are immutable.
    # Then, use two pointers to traverse the array. Place the first at the beginning of the list (left) and the other at the end (right).
    # While the left pointer is lesser than the right one do the following:
    # - If both pointers are pointing to vowels, swap the vowels in the list.
    # - If the left pointer is not pointing to a vowel, move it one position to the right (left += 1).
    # - If the right pointer is not pointing to a vowel, move it one position to the left (right -= 1).
    # When both pointers converge, you will have a list with the original input but with reversed vowels.
    # Turn this list into a string and return it.
    #
    # Solution complexity:
    # Time complexity: O(n) where n is number of characters in the input.
    # Space complexity: O(n) space.
    def ReverseVowels(self, s):
        S = list(s) # Copy string to a list as Python strings are immutable
        vowels = "aeiouAEIOU"
        left = 0
        right = len(S) - 1

        while left < right:
            leftChar = S[left]
            rightChar = S[right]

            if leftChar in vowels and rightChar in vowels:
                temp = S[left]
                S[left] = S[right]
                S[right] = temp
                
                left += 1
                right -= 1
                continue
            
            if leftChar not in vowels:
                left += 1
                continue

            if rightChar not in vowels:
                right -= 1

        return ''.join(S)
    
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    string = "Hello"
    expectedOutput = "Holle"
    output = solution.ReverseVowels(string)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    string = "AEIOU"
    expectedOutput = "UOIEA"
    output = solution.ReverseVowels(string)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    string = "DesignGurus"
    expectedOutput = "DusugnGires"
    output = solution.ReverseVowels(string)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    string = ""
    expectedOutput = ""
    output = solution.ReverseVowels(string)
    print(output, expectedOutput, output == expectedOutput)
