class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # s3 must contain every character from s1 and s2.
        if len(s1) + len(s2) != len(s3):
            return False

        m = len(s1)
        n = len(s2)

        # dp[i][j] = True if we can form the first
        # i + j characters of s3 using the first
        # i characters of s1 and first j characters of s2.
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # We can form an empty s3 using
        # zero characters from both strings.
        dp[0][0] = True

        # Fill the table.
        for i in range(m + 1):
            for j in range(n + 1):

                # Number of characters already used in s3.
                k = i + j

                # Take the next character from s1.
                if i > 0 and dp[i - 1][j]:
                    if s1[i - 1] == s3[k - 1]:
                        dp[i][j] = True

                # Take the next character from s2.
                if j > 0 and dp[i][j - 1]:
                    if s2[j - 1] == s3[k - 1]:
                        dp[i][j] = True

        return dp[m][n]
