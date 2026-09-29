class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #   Connect all points with the minimum possible total cost, without creating a cycle.  
    #     MST
    # ├── Prim's
    # └── Kruskal's

        n = len(points)

        # Cheapest cost to connect each point
        # to our current connected group
        cost = [float("inf")] * n
        cost[0] = 0

        visited = set()

        total_cost = 0

        for _ in range(n):

            # Find the unvisited point with
            # the smallest connection cost
            curr = -1

            for i in range(n):
                if i in visited:
                    continue

                if curr == -1 or cost[i] < cost[curr]:
                    curr = i

            # Add this point to our tree
            visited.add(curr)
            total_cost += cost[curr]

            # Update costs for remaining points
            for i in range(n):

                if i in visited:
                    continue

                distance = (
                    abs(points[curr][0] - points[i][0])
                    + abs(points[curr][1] - points[i][1])
                )

                if distance < cost[i]:
                    cost[i] = distance

        return total_cost