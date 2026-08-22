class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buyDay = 0
        sellDay = 0
        maxProfit = 0
        for i in range(n - 1):
            profit = prices[i + 1] - prices[buyDay]
            if profit <= 0:
                buyDay = i + 1
            if profit > maxProfit:
                sellDay = i + 1
                maxProfit = profit
        return maxProfit
            
        