class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        # dp(i, holding)
        # = maximum profit from day i onward
        #   when holding tells us whether we currently
        #   own a stock.
        #
        # holding = 0 -> don't own a stock
        # holding = 1 -> own a stock

        memo = {}

        def dp(i, holding):

            # We reached the end.
            # No more profit can be made.
            if i >= n:
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            if holding == 0:
                # Option 1: Buy today
                buy = -prices[i] + dp(i + 1, 1)
                # Option 2: Don't buy today
                skip = dp(i + 1, 0)
                memo[(i, holding)] = max(buy, skip)
            else:
                # Option 1: Sell today
                # After selling, i+1 is cooldown,
                # so we continue from i+2.
                sell = prices[i] + dp(i + 2, 0)
                # Option 2: Keep holding the stock
                hold = dp(i + 1, 1)
                memo[(i, holding)] = max(sell, hold)
            return memo[(i, holding)]
        # Start at day 0 without owning a stock.
        return dp(0, 0)
