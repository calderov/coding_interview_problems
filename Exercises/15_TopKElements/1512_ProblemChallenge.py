# Problem:
# Given a string and a number ‘K’, find if the string can be rearranged such
# that the same characters are at least ‘K’ distance apart from each other.
#
# Examples:
#
#   Input: "mmpp", K=2
#   Output: "mpmp" or "pmpm"
#   Explanation: All same characters are 2 distance apart.
#
#   Input: "Programming", K=3
#   Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
#   Explanation: All same characters are 3 distance apart.
#
#   Input: "aab", K=2
#   Output: "aba"
#   Explanation: All same characters are 2 distance apart.
#
#   Input: "aappa", K=3
#   Output: ""
#   Explanation: We cannot find an arrangement of the string where any two 'a'
#   are 3 distance apart.
#

from heapq import *

class Solution:
    # Solution:
    # 1. Count the frequency of each char.
    #
    # 2. Add all chars and their frequencies into a max heap (the heap should maximize based on frequency).
    #
    # 3. Initialize variables to hold the resulting string (result), a buffer of previous chars and their frequencies (buffer).
    #
    # 4. Pick the top element from the max heap (a tuple consisting of a char and its frequency).
    #
    # 5. Append the char to the result and substract 1 from it's frequency.
    #
    # 6. If there are at most k elements in the buffer, pop the first element of
    #    the buffer (a tuple of a char and it's frequency) and push it into the max heap.
    #
    # 7. If the frequency of the current char is greater than zero, push it (ant it's
    #    frequency) into the buffer.
    #
    # 8. Append all the chars still in the buffer into the result.
    #
    # 9. Verify the character spacing in the result and return 
    #    if a given char is not at least k spaces from any of its duplicates.
    #
    # 9. Return the result string.
    #
    # Solution complexity:
    # Time complexity: O(n + n log(n))
    # Space complexity: O(n)
    def RearrangeCharsKDistanceAppart(self, inputString, k):
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

        # Initialize variables to hold the resulting string (result), a buffer of previous chars and their frequencies (buffer)
        buffer = []
        result = []
        while maxHeap:
            # Pick the top element from the max heap (a tuple consisting of a char and its frequency)
            freq, c = heappop(maxHeap)
            freq *= -1
    
            # Append the char to the result and substract 1 from it's frequency
            result.append(c)
            freq -= 1

            # If there are at most k elements in the buffer, pop the first element of
            # the buffer (a tuple of a char and it's frequency) and push it into the max heap
            if buffer and len(buffer) <= k:
                heappush(maxHeap, buffer.pop(0))

            # If the frequency of the current char is greater than zero, push it (ant it's
            # frequency) into the buffer.
            if freq > 0:
                buffer.append((-freq, c))

        # Append all the chars still in the buffer into the result
        while buffer:
            freq, c = buffer.pop(0)
            freq *= -1
            for i in range(freq):
                result.append(c)
        
        # Verify the character spacing in the result and return 
        # if a given char is not at least k spaces from any of its duplicates
        positions = {}
        for i in range(len(result)):
            c = result[i]
            
            if c not in positions:
                positions[c] = [i]
                continue
            
            distance = i - positions[c][-1]
            if distance < k:
                return ''
            
            else:
                 positions[c].append(i)

        # Return the result string
        return "".join(result)
        

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    inputString = "mmpp"
    k = 2
    expectedOutput = "mpmp"
    output = solution.RearrangeCharsKDistanceAppart(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    inputString = "Programming"
    k = 3
    expectedOutput = "gmrPagimnor"
    output = solution.RearrangeCharsKDistanceAppart(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    inputString = "aab"
    k = 2
    expectedOutput = "aba"
    output = solution.RearrangeCharsKDistanceAppart(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4
    inputString = "aappa"
    k = 3
    expectedOutput = ""
    output = solution.RearrangeCharsKDistanceAppart(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5
    inputString = "aaaab"
    k = 2
    expectedOutput = ""
    output = solution.RearrangeCharsKDistanceAppart(inputString, k)
    print(output, expectedOutput, output == expectedOutput)

    # Example 6
    inputString = "aaaaa"
    k = 1
    expectedOutput = "aaaaa"
    output = solution.RearrangeCharsKDistanceAppart(inputString, k)
    print(output, expectedOutput, output == expectedOutput)