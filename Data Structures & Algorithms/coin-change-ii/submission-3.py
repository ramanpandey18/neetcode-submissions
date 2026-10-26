class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Key idea: Count all combinations, processing each coin first so different orders of the same coins are not counted separately.
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[amount]
        
        
        
        
        
        # # dp[a] = number of combinations that make amount a
        # dp = [0] * (amount + 1)

        # # There is exactly one way to make amount 0:
        # # choose no coins.
        # dp[0] = 1

        # # Process each coin one by one.
        # # This ensures that different orders of
        # # the same coins are NOT counted separately.
        # for coin in coins:

        #     # Try using this coin to make every
        #     # amount from coin up to target amount.
        #     for a in range(coin, amount + 1):

        #         # We can make amount 'a' by:
        #         # 1. Making 'a - coin'
        #         # 2. Adding the current coin
        #         dp[a] += dp[a - coin]

        # return dp[amount]

    