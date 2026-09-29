import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = {}
        for u, v, time in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, time))
        
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        min_heap = [(0, k)]
        while min_heap:
            time, node = heapq.heappop(min_heap)
            if time > dist[node]:
                continue
            for nei, edge_time in graph.get(node, []):
                new_time = time + edge_time
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(min_heap, (new_time, nei))

        for node in range(1, n + 1):
            if dist[node] == float('inf'):
                return -1
        return max(dist[1:])

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

# DIJKSTRA

# 1. Set starting node distance = 0.
# 2. Set every other distance = infinity.
# 3. Put starting node into a min heap.
# 4. Take the node with smallest distance.
# 5. Look at its neighbors.
# 6. Calculate:

#        current distance + edge weight

# 7. If this is smaller than the neighbor's
#    current distance:
#        update it
#        put neighbor into heap
# 8. Repeat.


# We want the shortest distance from A to every node.
# Initially:
# A = 0
# B = ∞
# C = ∞
# Then we repeatedly:
# Pick the node with the smallest known distance.
# Look at its neighbors.
# Ask:
# "Can I reach this neighbor faster through this node?"
# If yes, update its distance.
# Repeat.
# That is Dijkstra.
