class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)

        # dp[i][j] =
        # number of ways to form t[j:]
        # using s[i:]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # If t is completely formed,
        # there is exactly 1 way to finish.
        for i in range(m + 1):
            dp[i][n] = 1

        # Fill the table from bottom-right to top-left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Characters match
                if s[i] == t[j]:

                    # Choice 1: use s[i]
                    use = dp[i + 1][j + 1]

                    # Choice 2: skip s[i]
                    skip = dp[i + 1][j]

                    dp[i][j] = use + skip

                else:
                    # Characters don't match,
                    # so we must skip s[i]
                    dp[i][j] = dp[i + 1][j]

        return dp[0][0]
