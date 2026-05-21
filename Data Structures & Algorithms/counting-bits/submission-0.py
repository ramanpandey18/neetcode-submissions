class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(x):
            count = 0
            while x:
                x = x & (x - 1)
                count += 1
            return count
    
        return [hammingWeight(i) for i in range(n+1)]