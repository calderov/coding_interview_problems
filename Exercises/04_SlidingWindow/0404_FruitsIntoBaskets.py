# Problem:
# You are visiting a farm to collect fruits. The farm has a single row of fruit trees.
# You will be given two baskets, and your goal is to pick as many fruits as possible
# to be placed in the given baskets.
#
# You will be given an array of characters where each character represents a fruit tree.
# The farm has following restrictions:
#
#   1. Each basket can have only one type of fruit. There is no limit to how many fruits
#      a basket can hold.
#
#   2. You can start with any tree, but you can’t skip a tree once you have started.
#
#   3. You will pick exactly one fruit from every tree until you cannot, i.e., you will
#      stop when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both baskets.
#
# Examples:
#
# Input: Fruit=['A', 'B', 'C', 'A', 'C']  
# Output: 3  
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
#
# Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']  
# Output: 5  
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we
#              start with the second letter: ['B', 'C', 'B', 'B', 'C']

class Solution:
    # Solution:
    # This problem can be stated as finding the longest subarray with at most 2 different
    # kinds of fruit. To solve it we can proceed as follows:
    #
    # 1. Initialize a variable to keep track of the length of the longest subarray
    #    that matches our criteria NumberOfDifferentKindsOfFruit(subarray) <= 2.
    #   
    #    Since we have not evaluated any subarray yet, initialize this variable to
    #    zero.
    #      maxFruitsIntoBaskets = 0
    # 
    # 2. Initialize a couple of pointers to mark the start and the end of a sliding window.
    #    start = 0
    #    end = 0
    #
    # 3. Initialize an empty list named subarray, we will use it to keep a copy of the
    #    subarray within the sliding window so it is easy to operate.
    #
    # 4. While the end of the sliding window is still within the limits of the input array 
    #   (fruits) append fruits[end] to the subarray.
    # 
    # 5. If the number of distinct fruits in the subarray is less than 2, check if the
    #    length of the subarray is greater than maxFruitsIntoBaskets, and update it if
    #    needed.
    #      maxFruitsIntoBaskets = max(maxFruitsIntoBaskets, len(subarray))
    #
    # 6. If the number of distinct characters in the subarray is greater than 2, remove the first
    #    element of the subarray until this is no longer the case. Do this using a while loop 
    #    and add 1 to the start pointer on each iteration.
    #
    # 7. Add 1 to the end pointer and loop back to step 4, unless the end pointer has passed
    #    the end of the string.
    #
    # 8. Return maxFruitsIntoBaskets and finish.
    #    
    # Solution complexity:
    # Time complexity: O(n)
    # Space complexity: O(n) as the support subarray can be as long as the original array
    def MaxNumberOfFruitsIntoBaskets(self, fruits):
        maxFruitsIntoBaskets = 0
        subarray = []
        start = 0
        end = 0

        while end < len(fruits):
            subarray.append(fruits[end])

            if len(set(subarray)) <= 2:
                maxFruitsIntoBaskets = max(maxFruitsIntoBaskets, len(subarray))
            
            while len(set(subarray)) > 2:
                subarray.pop(0)
                start += 1

            end += 1
        
        return maxFruitsIntoBaskets


if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    fruits = ['A', 'B', 'C', 'A', 'C']  
    expectedOutput = 3
    output = solution.MaxNumberOfFruitsIntoBaskets(fruits)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    fruits = ['A', 'B', 'C', 'B', 'B', 'C']  
    expectedOutput = 5
    output = solution.MaxNumberOfFruitsIntoBaskets(fruits)
    print(output, expectedOutput, output == expectedOutput)