class Solution:
    def canPartition(self, nums: list[int]) -> bool:
# Partition Equal Subset Sum — Simple Steps
# 1. Calculate the total sum of nums.
# 2. If the total is odd, return False.
# 3. Set target = total // 2.
# 4. Create dp of size target + 1, initialize all values to False, and set dp[0] = True.
# 5. For each number num, iterate j backward from target to num.
# 6. Update dp[j] = dp[j] or dp[j - num].
# 7. Return dp[target].
        
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
        