class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m -1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]

        m = len(text1)
        n = len(text2)

        # dp[i][j] = LCS length between
        # text1[i:] and text2[j:]
        #
        # Extra row and column represent
        # the case where one string is empty.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the table from bottom-right to top-left.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # If characters match, take this character.
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

                # If they don't match, skip one character
                # from either text1 or text2.
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        # dp[0][0] represents the entire two strings.
        return dp[0][0]
