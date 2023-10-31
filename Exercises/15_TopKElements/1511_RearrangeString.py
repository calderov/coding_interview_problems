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
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
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

        prevChar = None
        prevFreq = 0
        result = []

        while maxHeap:
            freq, c = heappop(maxHeap)
            freq *= -1

            if prevChar and prevFreq > 0:
                heappush(maxHeap, (-prevFreq, prevChar))
        
            result.append(c)

            prevChar = c
            prevFreq = freq - 1

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
    