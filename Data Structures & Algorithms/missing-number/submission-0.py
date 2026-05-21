class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        
        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor ^= i
        
        # XOR with all array elements
        for num in nums:
            xor ^= num
        
        return xor
        