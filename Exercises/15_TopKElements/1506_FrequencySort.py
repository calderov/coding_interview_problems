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
    # 1. Use a hash map to track the frequency of each character in the input string.
    # 
    # 2. For each character in the frequencies map, insert the character and its frequency into a max heap 
    #    (the max heap should maximize based on the character frequency).
    #
    # 3. Initialize an empty list named result to store the characters from the input string in the desired order.
    #    results = []
    #
    # 4. While there are items in the max heap
    #
    #    4.1 Pop the top item of the heap (a tuple) and split it into two values, one for a character (c) and one for its frequency (freq)
    #
    #    4.2 Append 'freq' copies of the character 'c' into the 'results' variable.
    #
    #    4.3 Go back to step 4.
    #
    # 5. Join the characters in the 'result' list, into a string and return it.
    #
    # Solution complexity:
    # Time complexity: O(n + n * log(n))
    # Space complexity: O(n)
    def FrequencySort(self, inputString):
        # Use a hash map to track the frequency of each character in the input string
        frequencies = {}
        for i in range(len(inputString)):
            c = inputString[i]
            if c not in frequencies:
                frequencies[c] = 0
            frequencies[c] += 1
        
        # For each character in the frequencies map, insert the character and its frequency into a max heap 
        # (the min heap should maximize based on the character frequency).
        maxHeap = []
        for num, freq in frequencies.items():
            heappush(maxHeap, (-freq, num))

        # Initialize an empty list named result to store the characters from the input string in the desired order.
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