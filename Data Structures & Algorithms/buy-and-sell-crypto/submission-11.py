class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        sell_day = 0
        buy_day = 0
        for i in range(len(prices) - 1):
            curr_profit = prices[i + 1] - prices[buy_day]
            if curr_profit <= 0:
                buy_day = i + 1
            else:
                sell_day = i + 1
                max_profit = max(curr_profit, max_profit)
        return max_profit
     