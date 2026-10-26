class Solution:
    def numDecodings(self, s: str) -> int:
        # 1. Traverse the string backward, from right to left.
        # 2. If s[i] == "0", set dp[i] = 0, because zero cannot be decoded alone.
        # 3. Otherwise, take the one-digit option: dp[i] = dp[i + 1].
        # 4. Check whether the two-digit number s[i:i+2] is between 10 and 26. If valid, add dp[i + 2].
        # 5. Return dp[0], which contains the total number of decoding ways for the entire string.
        n = len(s)
        dp = [1] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            dp[i] = dp[i + 1]
            if i + 1 < n:
                number = int(s[i: i + 2])
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
