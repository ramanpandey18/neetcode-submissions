class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        postfix = 0
        res = nums[0]
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            postfix = nums[n - 1 - i] * (postfix or 1)
            res = max(res, max(prefix, postfix))
        return res
