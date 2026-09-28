"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # visited[curr] = clone
        # original node → cloned node
        # visited = {
        #     Node(1): Node(1'),
        #     Node(2): Node(2'),
        #     Node(3): Node(3')
        # }
        # 1. Check if already cloned
        # 2. Create clone
        # 3. Clone/connect all neighbors
        if not node:
            return None
        visited = {}
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            
            clone = Node(curr.val)
            visited[curr] = clone
            for nei in curr.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node)

        #     if curr in visited:
        #         return visited[curr]
        #     clone = Node(curr.val)
        #     visited[curr] = clone

        #     for nei in curr.neighbors:
        #         clone.neighbors.append(dfs(nei))
        #     return clone
        
        # return dfs(node)










