# Problem:
# Given a string, find if its letters can be rearranged in such a way that no
# two same characters come next to each other.
#
# Examples:
#
#   Input: "aappp"
#   Output: "papap"
#   Explanation: In "papap", none of the repeating characters come next to each
#   other.
#
#   Input: "Programming"
#   Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
#   Explanation: None of the repeating characters come next to each other.
#

from heapq import *

class Solution:
    # Solution:
    # 1. Count the frequency of each char.
    #
    # 2. Add all chars and their frequencies into a max heap (the heap should maximize based on frequency).
    #
    # 3. Initialize variables to hold the resulting string (result), a previous char (prevChar) and its
    #    frequency (prevFreq).
    #
    # 4. While there are elements in the max heap.
    #
    #   4.1 Pick the top element from the max heap (a tuple consisting of a char and its frequency).
    #
    #   4.2 Append the char to the result.
    #
    #   4.3 If there is a previous char at this time with a frequency greater than zero, insert it back
    #       into the max heap.
    #
    #   4.4 Save the current char and its frequency - 1 into prevChar and prevFreq.
    #
    # 5. If the length of the result string equals that of the input string, return the result string.
    #    Otherwise, return an empty string.
    #
    # Solution complexity:
    # Time complexity: O(n + n(log(n)))
    # Space complexity: (O(n))
    def RearrangeString(self, inputString):
        # Count the frequency of each char
        frequencies = {}
        for c in inputString:
            if c not in frequencies:
                frequencies[c] = 0
            frequencies[c] += 1

        # Add all chars and their frequencies into a max heap (the heap should maximize based on frequency)
        maxHeap = []
        for c, freq in frequencies.items():
            heappush(maxHeap, (-freq, c))

        # Initialize variables to hold the resulting string (result), a previous char (prevChar) and its frequency (prevFreq)
        prevChar = None
        prevFreq = 0
        result = []

        # While there are elements in the max heap
        while maxHeap:
            # Pick the top element from the max heap (a tuple consisting of a char and its frequency)
            freq, c = heappop(maxHeap)
            freq *= -1

            # Append the char to the result
            result.append(c)

            # If there is a previous char at this time with a frequency greater than zero, insert it
            # back into the max heap
            if prevChar and prevFreq > 0:
                heappush(maxHeap, (-prevFreq, prevChar))

            # Save the current char and its frequency - 1 into prevChar and prevFreq
            prevChar = c
            prevFreq = freq - 1

        # If the length of the result string equals that of the input string, return the result string.
        # Otherwise, return an empty string
        if len(result) == len(inputString):
            return ''.join(result)
        return ""

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    inputString = "aappp"
    expectedOutput = "papap"
    output = solution.RearrangeString(inputString)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    inputString = "Programming"
    expectedOutput = "gmrPagimnor"
    output = solution.RearrangeString(inputString)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    inputString = "aapa"
    expectedOutput = ""
    output = solution.RearrangeString(inputString)
    print(output, expectedOutput, output == expectedOutput)

    #Example 4
    inputString   = "aaaaaabbbbccc"
    expectedOutput= "ababacabacabc"
    output = solution.RearrangeString(inputString)
    print(output, expectedOutput, output == expectedOutput)
