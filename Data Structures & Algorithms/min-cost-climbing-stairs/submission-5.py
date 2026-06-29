class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        def get_min_cost(i: int) -> int:
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            take_one = cost[i] + get_min_cost(i + 1)
            take_two = cost[i] + get_min_cost(i + 2)
            memo[i] = min(take_one, take_two)
            return memo[i]
        return min(get_min_cost(0), get_min_cost(1))

        memo = {}
        n = len(cost)
        def get_min_cost(i: int) -> int:
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            take_one = cost[i] + get_min_cost(i + 1)
            take_two = cost[i] + get_min_cost(i + 2)

            memo[i] = min(take_one, take_two)
            return memo[i]
        return min(get_min_cost(0), get_min_cost(1))

        