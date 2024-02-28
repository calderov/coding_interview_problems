# 528. Random Pick with Weight (Medium)
# You are given a 0-indexed array of positive integers w where w[i] describes
# the weight of the ith index.
# 
# You need to implement the function pickIndex(), which randomly picks an
# index in the range [0, w.length - 1] (inclusive) and returns it. 
# The probability of picking an index i is w[i] / sum(w).
# 
# For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%),
# and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

import random

class Solution:
    # Time complexity: 
    # Space complexity: 
    def __init__(self, w):
        sumW = sum(w)
        self.w = list(w)

        for i in range(len(self.w)):
            self.w[i] = self.w[i] / sumW
            if i > 0:
                self.w[i] += self.w[i - 1]
        
    def PickIndex(self):
        n = random.uniform(0, 1)

        index = -1

        while index < len(self.w):
            index += 1
            if n <= self.w[index]:
                break

        return index
        
if __name__ == "__main__":
    # Initialize sample
    w = [1, 3]
    solution = Solution(w)

    # Initialize frequency map
    frequencies = {i:0 for i in range(len(w))}

    # Sample one million indexes
    for i in range(int(1e6)):
        frequencies[solution.PickIndex()] += 1
    
    # Print frequencies
    print(frequencies)