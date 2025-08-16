# 121. Best Time to Buy and Sell Stock
#
# You are given an array prices where prices[i] is the price of a given stock
# on the ith day.
# 
# You want to maximize your profit by choosing a single day to buy one stock
# and choosing a different day in the future to sell that stock.
# 
# Return the maximum profit you can achieve from this transaction. If you
# cannot achieve any profit, return 0.
#
# Examples
# 
#   Input: [3, 2, 6, 5, 0, 3]
#   Expected Output: 4
#   Justification: Buy the stock on day 2 (price = 2) and sell it on
#                  day 3 (price = 6). Profit = 6 - 2 = 4.
#
#   Input: [8, 6, 5, 2, 1]
#   Expected Output: 0
#   Justification: Prices are continuously dropping, so no profit can be
#                  made.
# 
#   Input: [1, 2]
#   Expected Output: 1
#   Justification: Buy on day 1 (price = 1) and sell on day 2 (price = 2). 
#                  Profit = 2 - 1 = 1.

# Time complexity: O(n ^ 2)
# Space complexity: O(1)
def getMaxProfitV1(prices):
    maxProfit = 0
    
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            maxProfit = max(maxProfit, prices[j] - prices[i])
    
    return maxProfit

# Time complexity: O(n)
# Space complexity: O(1)
def getMaxProfitV2(prices):
    minPrice = prices[0]
    maxProfit = 0

    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - minPrice)
    
    return maxProfit

def getMaxProfit(prices):
    return getMaxProfitV2(prices)

if __name__ == "__main__":
    prices = [3, 2, 6, 5, 0, 3]
    expectedOutput = 4
    output = getMaxProfit(prices)
    print(output, expectedOutput, output == expectedOutput)
 
    prices = [8, 6, 5, 2, 1]
    expectedOutput = 0
    output = getMaxProfit(prices)
    print(output, expectedOutput, output == expectedOutput)
  
    prices = [1, 2]
    expectedOutput = 1
    output = getMaxProfit(prices)
    print(output, expectedOutput, output == expectedOutput)