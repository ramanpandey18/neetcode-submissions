class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            memo = {}
            n = len(nums)
            def dfs(i):
                if i >= n:
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
                return memo[i]
            return dfs(0)
        return max(helper(nums[:-1]), helper(nums[1:]))




        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, nums):
        rob_1 = 0
        rob_2 = 0
        for num in nums:
            curr = max(rob_1 + num, rob_2)
            rob_1 = rob_2
            rob_2 = curr
        return rob_2