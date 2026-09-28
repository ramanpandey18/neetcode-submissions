import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}
        for u, v, time in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, time))
        
        dist  = [float("INF")] * (n + 1)
        dist[k] = 0
        min_heap = [(0, k)]

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > dist[node]:
                continue
            for neighbor, edge_time in graph.get(node, []):
                new_time = time + edge_time
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        for node in range (1, n + 1):
            if dist[node] == float("INF"):
                return -1
        
        return max(dist[1:])

        graph = {}
        for u, v, time in times: # Build graph
            if u not in graph:
                graph[u] = []
            graph[u].append((v, time))

        
        dist = [float("inf")] * (n + 1) # Shortest distance to every node
        dist[k] = 0 # Starting node
        heap = [(0, k)] # (time, node)

        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]: # Already found a better path
                continue

            for neighbor, edge_time in graph.get(node, []):
                new_time = time + edge_time
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        # Check if any node cannot be reached
        for node in range(1, n + 1):
            if dist[node] == float("inf"):
                return -1

        return max(dist[1:])
