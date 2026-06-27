class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {}
        # def helper(steps_left: int) -> int:
        #     if steps_left == 0:
        #         return 1
        #     if steps_left < 0:
        #         return 0
        #     if steps_left in memo:
        #         return memo[steps_left]
        #     memo[steps_left] = helper(steps_left - 1) + helper(steps_left - 2)
        #     return memo[steps_left]
        # return helper(n)

        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
    
    # def climbStairs(n: int) -> int:
        # Base Cases: 
        # If 0 steps left, we found 1 valid way (standing at the top).
        # If we overshoot (negative steps), this path is invalid (0 ways).
        # if n == 0: return 1
        # if n < 0: return 0
        
        # Recursive Step: Sum of taking 1 step + taking 2 steps
        # return climbStairs(n - 1) + climbStairs(n - 2)

    # print(climbStairs(4))