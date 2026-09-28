class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []

            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor in visited:
                    continue
                dfs(neighbor)
        
        for node in range(n):
            if node in visited:
                continue
            count += 1

            dfs(node)
        return count
