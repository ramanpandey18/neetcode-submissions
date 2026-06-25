class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for curr_amount in range(1, amount + 1):

            for coin in coins:

                if curr_amount - coin >= 0:
                    dp[curr_amount] = min(
                        dp[curr_amount],
                        1 + dp[curr_amount - coin]
                    )

        return dp[amount] if dp[amount] != float('inf') else -1
        
        memo = {}

        def dfs(rem):

            if rem == 0:
                return 0

            if rem < 0:
                return float('inf')

            if rem in memo:
                return memo[rem]

            ans = float('inf')

            for coin in coins:
                ans = min(ans, 1 + dfs(rem - coin))

            memo[rem] = ans
            return ans

        res = dfs(amount)

        return res if res != float('inf') else -1