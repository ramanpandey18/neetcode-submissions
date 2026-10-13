class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
# Initialize dp[i] = 1 because every element forms a subsequence of length 1.
# For each index i, check all previous indices j. If nums[j] < nums[i], update dp[i] = max(dp[i], dp[j] + 1).
# Return max(dp) because the longest increasing subsequence can end at any index.