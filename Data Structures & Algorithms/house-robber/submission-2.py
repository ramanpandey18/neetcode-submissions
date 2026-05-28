# class Solution:

#     def rob(self, nums: list[int]) -> int:

#         if len(nums) == 1:
#             return nums[0]

#         dp = [0] * len(nums)

#         dp[0] = nums[0]

#         dp[1] = max(nums[0], nums[1])

#         for i in range(2, len(nums)):

#             dp[i] = max(
#                 dp[i - 1],
#                 nums[i] + dp[i - 2]
#             )

#         return dp[-1]
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2