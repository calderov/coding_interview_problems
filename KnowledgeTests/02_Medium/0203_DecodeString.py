# Problem:
# You have a string that represents encodings of substrings, where each
# encoding is of the form k[encoded_string], where k is a positive integer,
# and encoded_string is a string that contains letters only.
#
# Your task is to decode this string by repeating the encoded_string k times
# and return it. It is given that k is always a positive integer.
#
# Examples
#   Input: "3[a3[c]]"
#   Expected Output: "acccacccaccc"
#   Justification: The inner 3[c] is decoded as ccc, and then a is appended to
#   the front, forming acc. This is then repeated 3 times to form
#   acccacccaccc.
#
#   Input: "2[b3[d]]"
#   Expected Output: "bdddbddd"
#   Justification: The inner 3[d] is decoded as ddd, and then b is appended to
#   the front, forming bddd. This is then repeated 2 times to form bddd bddd.
#
#   Input: "4[z]"
#   Expected Output: "zzzz"
#   Justification: The 4[z] is decoded as z repeated 4 times, forming zzzz.

class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def DecodeString(self, inputString):
        stack = []
        multiplier = 0
        substring = ""

        for character in inputString:
            if character.isdigit():
                multiplier = multiplier * 10 + int(character)
                continue

            if character == "[":
                stack.append(multiplier)
                stack.append(substring)
                multiplier = 0
                substring = ""
                continue

            if character == "]":
                prevSubstring = stack.pop()
                repetitions = stack.pop()
                substring = prevSubstring + substring * repetitions
                continue

            substring += character

        return substring

if __name__ == "__main__":
    solution = Solution()

    inputString = "3[a3[c]]"
    expectedOutput = "acccacccaccc"
    output = solution.DecodeString(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    inputString = "2[b3[d]]"
    expectedOutput = "bdddbddd"
    output = solution.DecodeString(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    inputString = "4[z]"
    expectedOutput = "zzzz"
    output = solution.DecodeString(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
