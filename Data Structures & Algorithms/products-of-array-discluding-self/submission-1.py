class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i]

        postfix = [1] * n
        postfix[n-1] = nums[n-1]
        for i in range (n-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]

        result = [1] * n
        for i in range(n):
            if i == 0:
                result[i] = postfix[i+1]
            elif i == (n - 1):
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1] * postfix[i+1]
        return result
