class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Try every coin and choose the option requiring the fewest coins. Memoization avoids recalculating the same remaining amount.
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
