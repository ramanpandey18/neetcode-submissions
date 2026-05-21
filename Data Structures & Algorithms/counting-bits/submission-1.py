class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)   # Most optimal way    
        return dp
    
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(x):
            count = 0
            while x:
                x = x & (x - 1)
                count += 1
            return count
    
        return [hammingWeight(i) for i in range(n+1)]