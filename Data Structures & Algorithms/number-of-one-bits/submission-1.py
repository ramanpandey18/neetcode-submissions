class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):          # Fixed 32 iterations → O(1)
            count += (n >> i) & 1     # Check if ith bit is set
        return count
        