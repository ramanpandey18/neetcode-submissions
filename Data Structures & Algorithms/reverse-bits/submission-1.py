class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = n & 1
            result = (result << 1) | bit
            n = n >> 1
        return result
        
        
        
        
        
        
        
        result = 0
        for i in range(32):          # Must process exactly 32 bits
            # Get the least significant bit of n
            bit = n & 1
            
            # Add this bit to the result at the correct position (from left)
            result = (result << 1) | bit
            
            # Remove the processed bit from n
            n = n >> 1
        
        return result
        