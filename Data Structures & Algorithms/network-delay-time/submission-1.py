import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        graph = {}

        # Build graph
        for u, v, time in times:
            if u not in graph:
                graph[u] = []

            graph[u].append((v, time))

        # Shortest distance to every node
        dist = [float("inf")] * (n + 1)

        # Starting node
        dist[k] = 0

        # (time, node)
        heap = [(0, k)]

        while heap:

            time, node = heapq.heappop(heap)

            # Already found a better path
            if time > dist[node]:
                continue

            for neighbor, edge_time in graph.get(node, []):

                new_time = time + edge_time

                if new_time < dist[neighbor]:

                    dist[neighbor] = new_time

                    heapq.heappush(
                        heap,
                        (new_time, neighbor)
                    )

        # Check if any node cannot be reached
        for node in range(1, n + 1):
            if dist[node] == float("inf"):
                return -1

        return max(dist[1:])
        