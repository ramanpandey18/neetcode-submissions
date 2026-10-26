class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def helper(steps_left: int):
            if steps_left == 0:
                return 1
            if steps_left < 0:
                return 0
            if steps_left in memo:
                return memo[steps_left]
            memo[steps_left] = helper(steps_left - 1) + helper(steps_left - 2)
            return memo[steps_left]
        return helper(n)

# If steps_left == 0, return 1 because we found one valid way.
# If steps_left < 0, return 0 because we went beyond the top.
# Check memo to see if we already calculated the answer for this number of steps.
# Calculate ways by taking either 1 step or 2 steps:
# helper(steps_left - 1) + helper(steps_left - 2)
# Store the result in memo to avoid recalculating it.