class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1, 2, 6, 24]
        # postfix = [24, 24, 12, 4]
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
        
        n = len(nums)
        result = [1] * n

        # Step 1: Store prefix products in result
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: Multiply by postfix products
        postfix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
 