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
    def __init__(self, w):
        self.cumP = []
        sumW = sum(w)
        p = 0
        for i in range(len(w)):
            p += w[i] / sumW
            self.cumP.append(p)

    def pickIndex(self):
        x = random.random()
        for i in range(len(self.cumP)):
            if x < self.cumP[i]:
                return i
        return None
        
if __name__ == "__main__":
    # Initialize sample
    w = [1, 3]
    expected = [0.25, 0.75]
    solution = Solution(w)

    # Initialize frequency map
    frequencies = {i:0 for i in range(len(w))}

    # Sample one million indexes
    for i in range(int(1e6)):
        frequencies[solution.pickIndex()] += 1
    
    # Print frequencies
    for i in range(len(w)):
        print(f"probability({i}) = {frequencies[i]/1e6} expected({i}) = {expected[i]}")
