# Amazon ships several parcels each day to multiple locations. The dispatch
# centers have conveyor belts where the parcel boxes are placed.
# 
# In one such center there are a total of n boxes numbered 0, 1, ..., (n-1),
# where the capacity of the ith box is denoted by capacity[i]. A box numbered
# x, can contain a box numbered y if capacity[x] is divisible by capacity[y].
# I.e. capacity[y] is a factor of capacity[x].
# 
# A triplet of boxes (a, b, c) is said to be sustainable if 0 <= a < b < c <= n-1
# and capacity[a] is a factor of capacity[b], and capacity[b] is a factor
# of capacity[c].
# 
# Given the capacities of boxes, capacity, among all the triplets (a, b, c)
# satisfying the above constraint, return the maximum capacity of the middle
# box b, if no such triplet exists, return -1.
# 
# Example
# There are n=7 boxes, and their capacities are capacity=[1, 2, 6, 4, 107, 109, 1024].
# 
# The possible triplets (a, b, c) are (0, 1, 2), (0, 1, 3), (0, 1, 6), (0, 3,
# 6), (1, 3, 6). Among these, possible middle box capacities are 2 and 4, the
# maximum of which is 4. Return 4.
# 
# Function description
# Complete the function findMiddleMaximumCapacity which has the following
# parameter:
# int capacity[n]: the capacities of the boxes
# 
# Returns:
# int: the maximum middle box capacity among all possible sustainable
# triplets. If no such triplet exists, return -1.
# 
# Constraints
# - 1 <= n <= 10 ^ 5
# - 1 <= capacity[i] <= 10 ^ 5, 0 <= i < n

def findMiddleMaximumCapacity(capacity):
    n = len(capacity)

    maxMiddleCapacity = -1
    
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                # A triplet of boxes (a, b, c) is said to be sustainable if 0 <= a < b < c <= n-1
                # and capacity[a] is a factor of capacity[b], and capacity[b] is a factor
                # of capacity[c].
                if capacity[b] % capacity[a] == 0 and \
                   capacity[c] % capacity[b] == 0:
                    maxMiddleCapacity = max(maxMiddleCapacity, capacity[b])

    return maxMiddleCapacity

if __name__ == "__main__":
    # Example 1
    capacity=[1, 2, 6, 4, 107, 109, 1024]
    expectedOutput = 4
    output = findMiddleMaximumCapacity(capacity)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    capacity=[]
    expectedOutput = -1
    output = findMiddleMaximumCapacity(capacity)
    print(output, expectedOutput, output == expectedOutput)