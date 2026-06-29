class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        prefix = 0
        suffix = 0
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res
        n = len(nums)
        res = nums[0]
        prefix = 0
        suffix  = 0
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - i - 1] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res