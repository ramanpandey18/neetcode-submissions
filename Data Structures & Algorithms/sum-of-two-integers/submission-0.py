class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF   # 32 ones — keeps numbers in 32-bit range
        MAX  = 0x7FFFFFFF   # INT_MAX — highest positive 32-bit value

        while b != 0:
            carry = (a & b) << 1   # carry bits
            a = (a ^ b) & MASK     # sum bits, masked to 32 bits
            b = carry  & MASK      # carry, masked to 32 bits

        # If a <= MAX, it's a positive number — return as is
        # If a >  MAX, bit 31 is set — it's negative in 32-bit
        # Convert back: ~(a ^ MASK) flips bits back to Python negative
        return a if a <= MAX else ~(a ^ MASK)
