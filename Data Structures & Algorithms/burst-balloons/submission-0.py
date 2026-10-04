class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # Add virtual balloons with value 1
        nums = [1] + nums + [1]

        n = len(nums)

        # dp[left][right] =
        # maximum coins from bursting all balloons
        # between left and right
        dp = [[0] * n for _ in range(n)]

        # length is the distance between left and right
        # We need at least one balloon between them.
        for length in range(2, n):

            for left in range(0, n - length):

                right = left + length

                # Try every balloon as the LAST balloon
                for k in range(left + 1, right):

                    coins = (
                        nums[left]
                        * nums[k]
                        * nums[right]
                    )

                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][k]
                        + dp[k][right]
                        + coins
                    )

        return dp[0][n - 1]
