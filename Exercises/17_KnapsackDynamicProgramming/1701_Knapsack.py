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
    def GetMostProfitableCombination(self, weights, profits, capacity):
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

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    capacity = 5
    expectedOutput = [2, 3]

    output = solution.GetMostProfitableCombination(weights, profits, capacity)
    print(output, sum([profits[i] for i in output]))
    print(expectedOutput, sum([profits[i] for i in expectedOutput]))
    print(output == expectedOutput)
    print()

    # Example 2
    weights = [1, 2, 3, 5]
    profits = [1, 6, 10, 16]
    capacity = 7
    expectedOutput = [1, 3]

    output = solution.GetMostProfitableCombination(weights, profits, capacity)
    print(output, sum([profits[i] for i in output]))
    print(expectedOutput, sum([profits[i] for i in expectedOutput]))
    print(output == expectedOutput)