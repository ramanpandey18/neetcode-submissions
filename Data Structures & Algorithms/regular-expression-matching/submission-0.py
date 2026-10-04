class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dp(i, j):

            # Already calculated
            if (i, j) in memo:
                return memo[(i, j)]

            # Pattern is finished
            # String must also be finished
            if j == len(p):
                return i == len(s)

            # Check whether current characters match
            first_match = (
                i < len(s)
                and (p[j] == s[i] or p[j] == ".")
            )

            # Check if the next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == "*":

                # Choice 1:
                # Treat x* as zero occurrences
                skip = dp(i, j + 2)

                # Choice 2:
                # Use x* to consume one character
                use = False

                if first_match:
                    use = dp(i + 1, j)

                memo[(i, j)] = skip or use

            else:
                # Normal character or '.'
                if first_match:
                    memo[(i, j)] = dp(i + 1, j + 1)
                else:
                    memo[(i, j)] = False

            return memo[(i, j)]

        return dp(0, 0)
