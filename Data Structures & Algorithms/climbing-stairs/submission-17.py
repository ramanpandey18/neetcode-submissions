class Solution:
    def climbStairs(self, n: int) -> int:

        # ways[i] = number of distinct ways to reach step i
        ways = [0] * (n + 1)
        ways[0] = 1  # one way to stand at the ground: do nothing

        for step in range(1, n + 1):
            from_one_below = ways[step - 1]
            from_two_below = ways[step - 2] if step >= 2 else 0
            ways[step] = from_one_below + from_two_below

        return ways[n]
