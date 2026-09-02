class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n + 1):
            xor ^= i
        for num in nums:
            xor ^= num
        return xor
        
        
        
        
        
        n = len(nums)
        xor = 0
        
        # XOR all numbers from 0 to n
        for i in range(n + 1):
            xor ^= i
        print(xor)
        print("new line")
        # XOR with all array elements
        for num in nums:
            xor ^= num
        print(xor)
        return xor
        