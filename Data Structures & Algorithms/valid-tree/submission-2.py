class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # n = number of nodes
        # edges = connections between nodes
        # A valid tree has two things:
        # Every node is connected
        # There is no cycle
        # For a graph with n nodes to be a tree, it must have exactly:
        # n - 1 edges
        # if len(edges) != n - 1:
        #     return False
        # 1. Check edges == n - 1
        #   ↓
        #     No → False
        #         ↓
        #         Yes
        #         ↓
        # 2. Build undirected graph
        #         ↓
        # 3. Start DFS from node 0
        #         ↓
        # 4. Visit every connected node
        #         ↓
        # 5. Count visited nodes
        #         ↓
        # visited == n ?
        #     /       \
        #     Yes        No
        #     ↓          ↓
        # True       False

        # n nodes
        # +
        # n - 1 edges
        # +
        # all nodes connected
        # =
        # valid tree

        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Build undirected graph
        graph = {}

        for a, b in edges:

            if a not in graph:
                graph[a] = []

            if b not in graph:
                graph[b] = []

            # Because this is UNDIRECTED:
            # a connects to b
            # b connects to a

            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node):

            # Mark current node as visited
            visited.add(node)

            # Visit all neighbors
            for neighbor in graph.get(node, []):

                # Already visited → don't visit again
                if neighbor in visited:
                    continue

                dfs(neighbor)

        # Start DFS from node 0
        dfs(0)

        # Every node must have been reached
        return len(visited) == n


        if len(edges) != n - 1:
            return False
        
        graph = {}

        for a, b in edges:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if node in visited:
                    continue
                dfs(neighbor)
        
        dfs(0)

        return len(visited) == n    
