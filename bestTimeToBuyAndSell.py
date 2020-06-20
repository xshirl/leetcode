def maxProfit(prices):
    profit = 0
    minPrice = float('inf')

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif profit < price - minPrice:
            profit = price - minPrice

    return profit
