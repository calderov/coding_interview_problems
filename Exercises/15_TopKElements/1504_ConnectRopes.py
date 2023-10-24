# Problem: 
# Given ‘N’ ropes with different lengths, we need to connect these ropes into
# one big rope with minimum cost. The cost of connecting two ropes is equal
# to the sum of their lengths.
# 
# Example:
# 
#   Input: [1, 3, 11, 5]
#   Output: 33
#   Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So
#   the total cost is 33 (4+9+20)
# 

from heapq import *

class Solution:
    # Solution:
    # 1. Heapify the rope lengths into a min heap.
    #
    # 2. Initialize a total cost variable.
    #    totalCost = 0
    #
    # 3. While the min heap has more than 1 item.
    #
    #    3.1 Extract the top most items of the heap r1 and r2.
    #
    #    3.2 Compute r3 = r1 + r2.
    #
    #    3.3 Increment the total cost by r3.
    #
    #    3.4 Push r3 into the heap and go to step 3.
    #
    # 4. Return the total cost.
    #
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def ConnectRopes(self, ropes):
        heapify(ropes)
        
        totalCost = 0
        while len(ropes) > 1:
            r1 = heappop(ropes)
            r2 = heappop(ropes)
            
            r3 = r1 + r2
            totalCost += r3

            heappush(ropes, r3)

        return totalCost

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    ropes = [1, 3, 11, 5]
    expectedOutput = 33
    output = solution.ConnectRopes(ropes)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    ropes = [3, 4, 5, 6]
    expectedOutput = 36
    output = solution.ConnectRopes(ropes)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3
    ropes = [1, 3, 11, 5, 2]
    expectedOutput = 42
    output = solution.ConnectRopes(ropes)
    print(output, expectedOutput, output == expectedOutput)
