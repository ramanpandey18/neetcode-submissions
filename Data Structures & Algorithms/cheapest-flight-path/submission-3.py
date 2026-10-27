class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k + 1):
            old_prices = prices.copy()
            for u, v, price in flights:
                if old_prices[u] == float("inf"):
                    continue
                new_price = old_prices[u] + price
                if new_price < prices[v]:
                    prices[v] = new_price
        return prices[dst] if prices[dst] != float("inf") else -1


        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            old_prices = prices.copy()
            for u, v, price in flights:
                if old_prices[u] == float("inf"):
                    continue
                new_price = old_prices[u] + price
                if new_price < prices[v]:
                    prices[v] = new_price
        return prices[dst] if prices[dst] != float("inf") else -1

# You are given:
# - n: Number of cities, numbered 0 to n-1.
# - flights: List of flights [u, v, price], meaning a flight from city u to city v costs price.
# - src: Starting city.
# - dst: Destination city.
# - k: Maximum number of stops allowed between the source and destination.   
# Cheapest Flights Within K Stops — Bellman-Ford Approach
#
# 1. Initialize a prices array of size n with infinity.
#    Set prices[src] = 0 because the cost to reach the source is zero.
#
# 2. Run the algorithm k + 1 times because at most k stops
#    means we can take at most k + 1 flights.
#
# 3. At the beginning of each iteration, make a copy of prices.
#    Use this copy to ensure each iteration considers only routes
#    that existed before the current iteration.
#
# 4. Iterate through every flight (u, v, price).
#
# 5. If city u is unreachable in the previous iteration,
#    skip this flight.
#
# 6. Otherwise, calculate the new cost to reach city v:
#    old_prices[u] + price.
#
# 7. If this new cost is cheaper than the current prices[v],
#    update prices[v].
#
# 8. After all iterations, if prices[dst] is still infinity,
#    return -1 because the destination is unreachable within k stops.
#
# 9. Otherwise, return prices[dst], the cheapest valid flight cost.
#
# Time Complexity: O((k + 1) * E), where E is the number of flights.
# Space Complexity: O(V), where V is the number of cities.