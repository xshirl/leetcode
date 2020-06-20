def maxProfit(prices):
    if len(prices) == 0:
        return 0
    profit = 0
    buy = prices[0]
    for price in prices:
        current = price - buy
        if current > 0:
            profit += current
        buy = price

    return profit

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
