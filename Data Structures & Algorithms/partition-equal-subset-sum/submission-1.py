
# class Solution:
#     def canPartition(self, nums: list[int]) -> bool:
#         total = sum(nums)
#         if total % 2 != 0:
#             return False

#         target = total // 2
#         dp = 1 << 0

#         for num in nums:
#             dp |= dp << num

#         return (dp & (1 << target)) != 0


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
        