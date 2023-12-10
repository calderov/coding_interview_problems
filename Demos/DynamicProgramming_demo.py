# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.
#
# Solution:
# Use dynamic programming to set a table dp, where dp[i][j] keeps the number of subsets of the first i elements
# of the input that add up to the value j which ranges from 0 to S. Build this table iteratively based on whether
# an element is included in a subset or not. Once the table is populated, return the value stored in the last cell
# of the table, as it contains how many subsets add to S.
#
# Time complexity: O(n * s)
# Space complexity: O(n * s)
def TotalNumberOfSubsetsWithSumS(nums, s):
    rows = len(nums)
    cols = s + 1

    # Initialize the dynamic programming table (dp)
    dp = [[0 for col in range(cols)] for row in range(rows)]

    # Base case: Mark the fist colum as the every set has an empty set 
    #            that adds up to zero.
    for row in range(rows):
        dp[row][0] = 1

    # Base case: A set containing only the first element from nums
    #            can add up to the value of the first element of nums,
    #            mark its corresponding colum.
    if nums[0] < cols:
        dp[0][nums[0]] = 1

    # For each cell on the dynamic programming table
    for row in range(1, rows):
        for col in range(1, cols):
            element = nums[row]

            # Case 1: Exclude the current element
            dp[row][col] += dp[row - 1][col]
            
            # Case 2: Include the current element
            if col >= element:
                dp[row][col] += dp[row - 1][col - element]
    
    # The amount of subsets that add up to S is located
    # in the last cell of the dynamic programming table
    return dp[-1][-1]

if __name__ == "__main__":
    # Example 1
    nums = [1, 1, 2, 3]
    s = 4
    expectedOutput = 3 # The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
                       # Note that we have two similar sets {1, 3}, because we have two '1' in our
                       # input.
    output = TotalNumberOfSubsetsWithSumS(nums, s)
    print(output, expectedOutput, output == expectedOutput)

    # Example 2
    nums = [1, 2, 7, 1, 5] 
    s = 9
    expectedOutput = 3 # The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
    output = TotalNumberOfSubsetsWithSumS(nums, s)
    print(output, expectedOutput, output == expectedOutput)
