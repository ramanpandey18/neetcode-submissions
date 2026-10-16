class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums   = [1, 2, 3, 4]
        # prefix = [1, 1, 2, 6]
        n  = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
