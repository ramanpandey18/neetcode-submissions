class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy_day = 0
        sell_day = 0
        max_profit = 0
        for i in range(n - 1):
            profit = prices[i + 1] - prices[buy_day]
            if profit <= 0:
                buy_day = i + 1
            if profit > max_profit:
                sell_day = i + 1
                max_profit = profit
        return max_profit
            
    

























        n = len(prices)
        buyDay  = 0
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




