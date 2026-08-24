class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = 0
        sell_day = 0
        max_profit = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[buy_day]
            if profit <= 0:
                buy_day = i + 1
            else:
                max_profit = max(prices[i + 1] - prices[buy_day] , max_profit)
                sell_day = i + 1
        return max_profit
            