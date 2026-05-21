class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0:
            return 0.0
        
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        for i in range(n):
            result *= x
        return round(result, 5)
        