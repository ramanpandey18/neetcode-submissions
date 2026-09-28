import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        # graph[u] = [(v, time), ...]
        graph = {}

        for u, v, time in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, time))

        # Shortest known distance to every node
        dist = [float("inf")] * (n + 1)

        # Starting node takes 0 time
        dist[k] = 0

        # (time, node)
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)

            # If we already found a shorter path, skip
            if time > dist[node]:
                continue

            for neighbor, edge_time in graph.get(node, []):

                new_time = time + edge_time

                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        # If any node was unreachable
        for node in range(1, n + 1):
            if dist[node] == float("inf"):
                return -1

        # Time when the LAST node receives the signal
        return max(dist[1:])
        