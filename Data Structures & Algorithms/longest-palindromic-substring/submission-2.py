class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]
        for i in range(len(s)):
            odd = expand(i, i)
            even = expande(i, i + 1)
            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even
        return result

# class Solution:
    def longestPalindrome(self, s: str) -> str:
        


        n = len(s)

        dp = [[False] * n for _ in range(n)]

        result = ""

        max_len = 0


        # Every single character is palindrome
        for i in range(n):

            dp[i][i] = True

            result = s[i]

            max_len = 1


        # Check substrings
        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1


                # Length 2 case
                if length == 2:

                    dp[i][j] = (s[i] == s[j])

                else:

                    dp[i][j] = (
                        s[i] == s[j]
                        and
                        dp[i + 1][j - 1]
                    )


                if dp[i][j] and length > max_len:

                    result = s[i:j+1]

                    max_len = length

        return result