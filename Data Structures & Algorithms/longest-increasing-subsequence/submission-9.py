class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n, -1, -1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

        # dp[i] = length of the longest
        # increasing subsequence starting at i
        #
        # Every number by itself is a valid
        # increasing subsequence of length 1.
        dp = [1] * len(nums)

        # Process from right to left because
        # dp[i] depends on dp[j] where j > i.
        for i in range(len(nums) - 1, -1, -1):

            # Look at every element after nums[i]
            for j in range(i + 1, len(nums)):

                # nums[j] can come after nums[i]
                # only if it is strictly greater.
                if nums[i] < nums[j]:

                    # Take nums[i], then use the best
                    # increasing subsequence starting at j.
                    dp[i] = max(dp[i], 1 + dp[j])

        # dp[i] gives the best subsequence starting
        # from each index, so take the overall maximum.
        return max(dp)