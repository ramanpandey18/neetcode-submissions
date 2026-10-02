class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(steps_left: int) -> int:
            if steps_left == 0:
                return 1
            if steps_left < 0:
                return 0
            if steps_left in memo:
                return memo[steps_left]
            memo[steps_left] = helper(steps_left - 1) + helper(steps_left - 2)
            return memo[steps_left]
        return helper(n)
        