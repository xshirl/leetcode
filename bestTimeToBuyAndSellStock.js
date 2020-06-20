function maxProfit(prices) {
  let profit = 0;
  for (let i = 0; i < prices.length; i++) {
    for (let j = i + 1; j < prices.length; j++) {
      if (profit < prices[j] - prices[i]) {
        profit = prices[j] - prices[i];
      }
    }
  }
  return profit;
}

function maxProfit2(prices) {
  let minBuyPrice = Infinity;
  let maxProfit = 0;

  for (let price of prices) {
    if (price < minBuyPrice) {
      minBuyPrice = price;
    } else if (price - minBuyPrice > maxProfit) {
      maxProfit = price - minBuyPrice;
    }
  }
  return maxProfit;
}

// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
