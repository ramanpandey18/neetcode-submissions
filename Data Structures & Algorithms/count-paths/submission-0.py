class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # dp[r][c] = number of ways to reach cell (r, c)
        dp = [[0] * n for _ in range(m)]

        # First row:
        # There is only one way to reach each cell:
        # keep moving right.
        for c in range(n):
            dp[0][c] = 1

        # First column:
        # There is only one way to reach each cell:
        # keep moving down.
        for r in range(m):
            dp[r][0] = 1

        # Calculate the remaining cells.
        for r in range(1, m):
            for c in range(1, n):

                # We can reach this cell either:
                # 1. From above
                # 2. From the left
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]
