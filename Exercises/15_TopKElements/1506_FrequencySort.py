# Problem Statement
# 
# Given a string, sort it based on the decreasing frequency of its characters.
# 
# Examples:
# 
#   Input: "Programming"
#   Output: "rrggmmPiano"
#   Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear
#   before any other character.
#   
#   Input: "abcbab"
#   Output: "bbbaac"
#   Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared
#   only once.
# 

from heapq import *

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def FrequencySort(self, inputString):
        characters = [inputString[i] for i in range(len(inputString))]
        
        frequencies = {}

        for c in characters:
            if c not in frequencies:
                frequencies[c] = 0
            frequencies[c] += 1
        
        maxHeap = []
        for num, freq in frequencies.items():
            heappush(maxHeap, (-freq, num))

        result = []
        while maxHeap:
            freq, c = heappop(maxHeap)
            freq *= -1

            for i in range(freq):
                result.append(c)

        return "".join(result)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    inputString = "Programming"
    expectedOutput = "ggmmrrPaino"
    output = solution.FrequencySort(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()

    # Example 2
    inputString = "abcbab"
    expectedOutput = "bbbaac"
    output = solution.FrequencySort(inputString)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)