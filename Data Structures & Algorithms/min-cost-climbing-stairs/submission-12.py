class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        top = len(cost)  # the floor above the last step

        # min_cost[i] = minimum cost to arrive at step i
        # we can start at step 0 or 1 for free
        min_cost = [0] * (top + 1)

        for step in range(2, top + 1):
            from_one_below = min_cost[step - 1] + cost[step - 1]
            from_two_below = min_cost[step - 2] + cost[step - 2]
            min_cost[step] = min(from_one_below, from_two_below)

        return min_cost[top]
        