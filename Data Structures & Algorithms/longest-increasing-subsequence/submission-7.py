from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [nums[0]]
        LIS = 1

        for i in range(1, len(nums)):

            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue

            # Find the first element >= nums[i]
            for j in range(len(dp)):
                if dp[j] >= nums[i]:
                    dp[j] = nums[i]
                    break

        return LIS
        
        dp = []
        dp.append(nums[0])
        LIS = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                LIS += 1
                continue
            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]
        return LIS
