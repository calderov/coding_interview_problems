# Code question 1
# 
# Imagine you are shopping on Amazon.com for some good weight lifting
# equipment. The equipment you want has plates of many different weights that
# you can combine to lift.
# 
# The listing on Amazon gives you an array 'plates', that consists of n
# different weighted plates, in kilograms. There are no two plates with the
# same weight. The element plates[i] denotes the weight of the ith plate from
# the top of the stack. You consider weight lifting equipment to be good if
# the plate at the top is the lightest, and the plate at the bottom is the
# heaviest.
# 
# More formally, the equipment with array plates will be called good weight
# lifting equipment if it satisfies the following conditions (assuming the
# index of the array starts from 1):
# 
# - plates[1] < plates[i] for all (2 <= i <= n)
# - plates[i] < plates[n] for all (1 <= i <= n - 1)
# 
# In one move, you can swap the order of adjacent plates. Find out the
# minimum number of moves required to form good weight lifting equipment.
# 
# Example:
#   Let the plates be in the order:
#   plates = [3, 2, 1]  
# 
#   In the first move, we swap the first and the second plates. After
#   swapping the order becomes:
#   plates = [2, 3, 1]  
# 
#   In the second move we swap the second and third plates. After swapping,
#   the order becomes:
#   plates = [2, 1, 3]  
# 
#   In the third move, we swap the first and the second plates. After
#   swapping, the order becomes:
#   plates = [1, 2, 3]  
# 
#   Now, the array satisfies the condition after 3 moves.
# 
# Function description:
# getMinMoves has the following parameter:
# int plates[n]: the distinct weights
# 
# Returns:
# int: the minimum number of operations required
# 
# Constraints:
# - 2 <= n <= 10 ^ 5
# - 1 <= plates[i] <= 10 ^ 9 for all (1 <= i <= n)
# - plates consist of distinct integers

# Time complexity: O(n)
# Space complexity: O(1)
def getMinMoves(plates):
    if not plates:
        return 0

    n = len(plates)

    minPlateIndex = plates.index(min(plates))
    maxPlateIndex = plates.index(max(plates))
    minMoves = minPlateIndex + (n - 1 - maxPlateIndex)

    # If minPlateIndex is greater than maxPlate index, 
    # substract one from minMoves as we counted the swap
    # between minPlateIndex and maxPlateIndex twice.
    if minPlateIndex > maxPlateIndex:
        minMoves -= 1 

    return minMoves

if __name__ == "__main__":
    # Example 1 (empty stack of plates)
    plates = []
    expectedOutput = 0
    output = getMinMoves(plates)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2 (trivial case, fully sorted)
    plates = [1, 2, 3, 4, 5]
    expectedOutput = 0
    output = getMinMoves(plates)
    print(output, expectedOutput, output == expectedOutput)

    # Example 3 (reversed)
    plates = [3, 2, 1]
    expectedOutput = 3
    output = getMinMoves(plates)
    print(output, expectedOutput, output == expectedOutput)

    # Example 4 (shuffled with minPlateIndex < maxPlateIndex)
    plates = [1, 5, 4, 3, 2]
    expectedOutput = 3
    output = getMinMoves(plates)
    print(output, expectedOutput, output == expectedOutput)

    # Example 5 (shuffled with maxPlateIndex < minPlateIndex)
    plates = [2, 5, 3, 1, 4]
    expectedOutput = 5
    output = getMinMoves(plates)
    print(output, expectedOutput, output == expectedOutput)
