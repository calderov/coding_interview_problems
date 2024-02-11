# Problem:
# Given a string s, reverse all the vowels in the string and return it.
# For example:
# - An input string "Hello" should return "Holle".
# - An input string "AEIOU" should return "UOIEA".
# - An input string "DesignGurus" should return "DusugnGires".

class Solution:
    def ReverseVowels(self, inputString):
        vowels = "aeiouAEIOU"
        output = list(inputString)

        left = 0
        right = len(inputString) - 1

        while left < right:
            if output[left] in vowels and output[right] in vowels:
                output[left], output[right] = output[right], output[left]
                left += 1
                right -= 1
                continue

            if output[left] not in vowels:
                left += 1

            if output[right] not in vowels:
                right -= 1

        return ''.join(output)

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
