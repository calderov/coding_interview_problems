# Problem: 
# Given two lists of intervals, find the intersection of these two lists.
# Each list consists of disjoint intervals sorted on their start time.
# 
# Examples:
# 
#   Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
#   Output: [2, 3], [5, 6], [7, 7]
#   Explanation: The output list contains the common intervals between the two
#   lists.
#  
#   Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
#   Output: [5, 7], [9, 10]
#   Explanation: The output list contains the common intervals between the two
#   lists.
# 

class Solution:
    # Solution:
    # 
    # Solution complexity:
    # Time complexity: 
    # Space complexity: 
    def foo(self):
        pass

if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    intervals1 = [[1, 3], [5, 6], [7, 9]]
    intervals2 = [[2, 3], [5, 7]]
    expectedOutput = [[2, 3], [5, 6], [7, 7]]
    output = solution.foo(intervals1, intervals2)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
    
    # Example 2:
    intervals1 = [[1, 3], [5, 7], [9, 12]]
    intervals2 = [[5, 10]]
    expectedOutput = [[5, 7], [9, 10]]
    output = solution.foo(intervals1, intervals2)
    print(output)
    print(expectedOutput)
    print(output == expectedOutput)
    print()
     