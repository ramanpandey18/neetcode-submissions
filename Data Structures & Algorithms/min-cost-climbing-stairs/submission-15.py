class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def get_min_cost(i: int):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            take_one = cost[i] + get_min_cost(i + 1)
            take_two = cost[i] + get_min_cost(i + 2)
            memo[i] = min(take_one, take_two)
            return memo[i]
        return min(get_min_cost(0), get_min_cost(1))


        memo = {}
        def get_min_cost(i: int):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            take_one = cost[i] + get_min_cost(i + 1)
            take_two = cost[i] + get_min_cost(i + 2)
            memo[i] = min(take_one, take_two)
            return memo[i]
        return min(get_min_cost(0), get_min_cost(1))

# 1. If i >= len(cost), return 0 because we have reached or passed the top.
# 2. Check memo to see if the minimum cost from index i is already calculated.
# 3. Calculate the cost of taking 1 step: cost[i] + get_min_cost(i + 1).
# 4. Calculate the cost of taking 2 steps: cost[i] + get_min_cost(i + 2).
# 5. Store the smaller cost in memo[i]:
#    min(take_one, take_two)
# 6. Return min(get_min_cost(0), get_min_cost(1)) because we can start at either index 0 or index 1.
# Key idea: At every stair, choose the move that leads to the minimum total cost.