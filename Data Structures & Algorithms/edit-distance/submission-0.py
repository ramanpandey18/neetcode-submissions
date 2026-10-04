class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        # dp[i][j] = minimum number of operations
        # needed to convert word1[i:] into word2[j:].
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # If word1 is empty, we must insert
        # all remaining characters of word2.
        for j in range(n + 1):
            dp[m][j] = n - j

        # If word2 is empty, we must delete
        # all remaining characters of word1.
        for i in range(m + 1):
            dp[i][n] = m - i

        # Fill the table from bottom-right to top-left.
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # Characters already match.
                # No operation is needed.
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]

                else:
                    # Delete word1[i]
                    delete = dp[i + 1][j]

                    # Insert word2[j]
                    insert = dp[i][j + 1]

                    # Replace word1[i] with word2[j]
                    replace = dp[i + 1][j + 1]

                    # We perform one operation plus
                    # the best remaining solution.
                    dp[i][j] = 1 + min(
                        delete,
                        insert,
                        replace
                    )

        # dp[0][0] represents converting the
        # entire word1 into the entire word2.
        return dp[0][0]
    