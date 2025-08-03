# Ice Cream Parlor
# https://www.hackerrank.com/challenges/icecream-parlor/problem

def iceCreamParlor(m, prices):
    n = len(prices)
    priceIndex = {}

    for i in range(n):
        price = prices[i]
        complement = m - price

        if complement in priceIndex:
            return [priceIndex[complement] + 1, i + 1]
        
        priceIndex[price] = i

    return None

if __name__=="__main__":
    # Example 1
    m = 4
    prices = [1, 4, 5, 3, 2]
    expected = [1, 4]
    output = iceCreamParlor(m, prices)

    print(expected)
    print(output)
    print(output == expected)

    print()

    # Example 2
    m = 4
    prices = [2, 2,4, 3]
    expected = [1, 2]
    output = iceCreamParlor(m, prices)

    print(expected)
    print(output)
    print(output == expected)
