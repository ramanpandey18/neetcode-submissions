class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX =  (1 << 31) - 1   # 2147483647  (bits: 0 followed by 31 ones)
        INT_MIN = -(1 << 31)       # -2147483648 (bits: 1 followed by 31 zeros)

        sign   = -1 if x < 0 else 1
        x      = abs(x)
        result = 0

        while x != 0:
            digit  = x % 10        # pop last digit
            x     //= 10           # remove last digit

            # Check BEFORE multiplying to avoid overflow
            if result > (INT_MAX - digit) // 10:
                return 0

            result = result * 10 + digit

        return sign * result