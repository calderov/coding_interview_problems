# 339. Nested List Weight Sum (Medium)
# You are given a nested list of integers nestedList. Each element is either
# an integer or a list whose elements may also be integers or other lists.
# 
# The depth of an integer is the number of lists that it is inside of. For
# example, the nested list [1,[2,2],[[3],2],1] has each integer's value set
# to its depth.
# 
# Return the sum of each integer in nestedList multiplied by its depth.
# 
# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: 10
# Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 +
# 1*2 = 10.
# 
# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: 27
# Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1
# + 4*2 + 6*3 = 27.
# 
# Example 3:
# Input: nestedList = [0]
# Output: 0

def nestedWeightSum(items, level=1):
    if not items:
        return 0
    
    nestedItems = []
    levelSum = 0

    for item in items:
        if type(item) == list:
            nestedItems += item
        else:
            levelSum += item * level

    levelSum += nestedWeightSum(nestedItems, level + 1)

    return levelSum

if __name__ == "__main__":
    # Example 1:
    nestedList = [[1,1],2,[1,1]]
    expected = 10
    output = nestedWeightSum(nestedList)
    print(expected)
    print(output)
    print(expected == output)
    print()

    # Example 2:
    nestedList = [1,[4,[6]]]
    expected = 27
    output = nestedWeightSum(nestedList)
    print(expected)
    print(output)
    print(expected == output)
    print()
 
    # Example 3:
    nestedList = [0]
    expected = 0
    output = nestedWeightSum(nestedList)
    print(expected)
    print(output)
    print(expected == output)
    print()
