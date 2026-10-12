class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n = number of nodes
        # edges = connections between nodes
        # A valid tree has two things:
        # Every node is connected
        # There is no cycle
        # A graph with n nodes to be a tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        graph = {} # Build undirected graph
        for a, b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
        # Because this is UNDIRECTED: a connects to b b connects to a
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor in visited:
                    continue
                dfs(neighbor)
        dfs(0)
        return len(visited) == n  
