# Problem:
# Given two integer arrays to represent weights and profits of ‘N’ items, we
# need to find a subset of these items which will give us maximum profit such
# that their cumulative weight is not more than a given number ‘C.’ Each item
# can only be selected once, which means either we put an item in the
# knapsack or we skip it.
#
# Example:
# Let’s take Merry’s example, who wants to carry some fruits in the knapsack
# to get maximum profit. Here are the weights and profits of the fruits:
#
#   Items: { Apple, Orange, Banana, Melon }
#
#   Weights: { 2, 3, 1, 4 }
#
#   Profits: { 4, 5, 3, 7 }
#
#   Knapsack capacity: 5
#
# Let’s try to put various combinations of fruits in the knapsack, such that
# their total weight is not more than 5:
#
#   Apple + Orange (total weight 5) => 9 profit
#
#   Apple + Banana (total weight 3) => 7 profit
#
#   Orange + Banana (total weight 4) => 8 profit
#
#   Banana + Melon (total weight 5) => 10 profit
#
# This shows that Banana + Melon is the best combination as it gives us the
# maximum profit, and the total weight does not exceed the capacity.

class Solution:
    # Solution:
    # Generate subsets of items (those weights and profits) which aggregated weight is less than the given capacity.
    # From those, keep track of the subset with the largest profit, use a cache to speed up the computing of weight and profit
    # of subsets that include previously known subsets in them. Return the subset with the largest profit.
    #
    # Solution complexity:
    # Time complexity: O(n * c) where n is the number of items and c is the capacity
    # Space complexity: O(n * c)
    def GetMostProfitableCombinationV1(self, weights, profits, capacity):
        maxProfitSubset = tuple()
        maxProfit = 0

        subsetsCache = {tuple(): {'weight': 0, 'profit': 0}}

        for i in range(len(weights)):
            subsets = list(subsetsCache.keys())

            for subset in subsets:
                newSubset = tuple(list(subset) + [i])
                newSubsetWeight = subsetsCache[subset]['weight'] + weights[i]
                newSubsetProfit = subsetsCache[subset]['profit'] + profits[i]
                
                if newSubsetWeight <= capacity:
                    subsetsCache[newSubset] = {'weight': newSubsetWeight, 'profit': newSubsetProfit}

                    if newSubsetProfit > maxProfit:
                        maxProfit = newSubsetProfit
                        maxProfitSubset = newSubset
        
        return list(maxProfitSubset)

    def GetMostProfitableCombinationV2(self, weights, profits, capacity):
        rows = len(weights)
        cols = capacity + 1

        # Initialize dynamic programming table (dp).
        dp = [[0 for col in range(cols)] for row in range(rows)]

        # Base case: Set the profit gained from the first item in the input array into the dp table
        #            for each capacity that is greater than or equal to the weight of the first item.
        for col in range(cols):
            if weights[0] <= col:
                dp[0][col] = profits[0]

        # For each cell in the dynamic programming table
        for row in range(1, rows):
            for col in range(1, cols):
                profit1 = 0
                profit2 = 0

                # Case 1: Exclude the profits of the current element
                profit1 = dp[row - 1][col]

                # Case 2: Include the profits of the current element
                if weights[row] <= col:
                    profit2 = profits[row] + dp[row - 1][col - weights[row]]

                # Take maximum profit and set it as the cell's value
                dp[row][col] = max(profit1, profit2)

        # The maximum profit value should be at the last cell of the dp table
        return dp[-1][-1]

    def GetMostProfitableCombination(self, weights, profits, capacity):
        return self.GetMostProfitableCombinationV2(weights, profits, capacity)

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    capacity = 5
    expectedOutput = 10

    output = solution.GetMostProfitableCombination(weights, profits, capacity)
    print(output, expectedOutput, output == expectedOutput)
    print()

    # Example 2
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    capacity = 7
    expectedOutput = 22

    output = solution.GetMostProfitableCombination(weights, profits, capacity)
    print(output, expectedOutput, output == expectedOutput)