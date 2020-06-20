def maxProfit(prices):
    if not prices:
        return 0

    n, ans = len(prices), 0
    left, buy = [0] * n, prices[0]

    for i in range(1, n):
        left[i] = max(left[i-1], prices[i] - buy)
        buy = min(buy, prices[i])

    right, sell = [0] * n, prices[-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], sell - prices[i])
        sell = max(sell, prices[i])
        ans = max(ans, left[i] + right[i])

    return ans

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/
