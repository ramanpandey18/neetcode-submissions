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
        