class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1 # Empty string has 1 way
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] = dp[i + 1]
            if i + 1 < n:
                number = int(s[i : i + 2])
                if 10 <= number <= 26:
                    dp[i] += dp[i + 2]
        return dp[0]

        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1 # Empty string has 1 way

        for i in range(n - 1, -1, -1):
            # We cannot decode a number starting with 0
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] = dp[i + 1] # Take one digit
            if i + 1 < n: # Take two digits
                number = int(s[i:i + 2])
                if 10 <= number <= 26:
                    dp[i] += dp[i + 2]
        return dp[0]
