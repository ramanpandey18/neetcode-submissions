class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arrLen = len(prices)
        if arrLen <= 0:
            return 0
        buyDay = 0
        sellDay = 0
        maxProfit = 0
        for i in range(arrLen - 1):
            profit = prices[i+1] - prices[buyDay]
            print("profit", profit)
            if profit <= 0:
                buyDay  = i + 1 
                # sellDay = i
            if profit > maxProfit:
                sellDay = i + 1
                maxProfit = profit
            # print("sellDay", sellDay)
            # print("buyDay", buyDay)
            # print("maxProfit", maxProfit)
        return maxProfit
        