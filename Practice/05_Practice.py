# Problem:
# Given a string s, reverse all the vowels in the string and return it.
# For example:
# - An input string "Hello" should return "Holle".
# - An input string "AEIOU" should return "UOIEA".
# - An input string "DesignGurus" should return "DusugnGires".

class Solution:
    def ReverseVowels(self, inputString):
        vowels = "aeiouAEIOU"
        outputString = list(inputString)

        left = 0
        right = len(inputString) - 1

        while left < right:
            leftChar = inputString[left]
            rightChar = inputString[right]

            if leftChar in vowels and rightChar in vowels:
                outputString[left], outputString[right] = outputString[right], outputString[left]
                left += 1
                right -= 1
                continue

            if leftChar not in vowels:
                left += 1

            if rightChar not in vowels:
                right -= 1

        return ''.join(outputString)

if __name__ == "__main__":
    solution = Solution()

    inputString = "Hello"
    expectedOutput = "Holle"
    output = solution.ReverseVowels(inputString)
    print(output, expectedOutput, output == expectedOutput)

    inputString = "AEIOU"
    expectedOutput = "UOIEA"
    output = solution.ReverseVowels(inputString)
    print(output, expectedOutput, output == expectedOutput)

    inputString = "DesignGurus"
    expectedOutput = "DusugnGires"
    output = solution.ReverseVowels(inputString)
    print(output, expectedOutput, output == expectedOutput)
