class Solution:
    def rob(self, nums: List[int]) -> int:
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