class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
    
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
        
        return n == 1
    def sum_of_squares(self, num: int) -> int:
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total