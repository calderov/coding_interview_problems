# Problem:
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

# Solution 1:
# Given an integer x, loop through all the integers from 0 onwards until you find a number i such that i * i > x (this will happen one iteration after i is the square root).
# Then, just return i - 1 as it is the square root. 
#
# Solution 1 complexity:
# Time complexity: O(x) where x is the given number to extract the square root of.
# Space complexity: O(1) constant space.
def SqrtV1(x):
    i = 0
    while i * i <= x:
        i += 1
    return i - 1


# Solution 2:
# Altough, Solution 1 is easy to reason about. We can do a bit better in time complexity by using binary search to find the square root.
#
# Solution 2 complexity:
# Time complexity: O(nlog(x)) where x is the given number to extract the square root of. This is due to the binary search nature of the search.
# Space complexity: O(1) constant space.
def SqrtV2(x):
    # Return early on the special cases of 0 and 1
    if x == 0 or x == 1:
        return x
    
    root = 0
    rootSquared = 0

    low = 2
    high = x // 2
    while low <= high:
        root = low + (high - low) // 2
        rootSquared = root * root

        if rootSquared == x:
            return root
        
        elif rootSquared > x:
            high = root - 1

        elif rootSquared < x:
            low = root + 1

    return high

if __name__ == "__main__":
    print(41, 6, SqrtV1(41), SqrtV2(41))
    print(36, 6, SqrtV1(36), SqrtV2(36))
    print(27, 5, SqrtV1(27), SqrtV2(27))
    print(25, 5, SqrtV1(25), SqrtV2(25))
    print(17, 4, SqrtV1(17), SqrtV2(17))
    print(8, 2, SqrtV1(8), SqrtV2(8))
    print(3, 1, SqrtV1(3), SqrtV2(3))
    print(2, 1, SqrtV1(2), SqrtV2(2))
    print(1, 1, SqrtV1(1), SqrtV2(1))
    print(0, 0, SqrtV1(0), SqrtV2(0))