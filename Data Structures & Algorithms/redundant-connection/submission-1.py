class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)

        parent = [i for i in range(n + 1)]

        def find(x):
            while x != parent[x]:
                parent[x] = x
            return x
        
        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return [a, b]
            
            parent[root_a] = root_b

        n = len(edges)

        # Initially, every node is its own parent
        parent = [i for i in range(n + 1)]

        # Find the root/leader of a node
        def find(x):

            # Keep going until we reach the node
            # that is its own parent
            while x != parent[x]:
                x = parent[x]

            return x

        # Process every edge
        for a, b in edges:

            # Find the group of a
            root_a = find(a)

            # Find the group of b
            root_b = find(b)

            # If both have the same root,
            # they are already connected.
            #
            # Adding this edge creates a cycle.
            if root_a == root_b:
                return [a, b]

            # Otherwise join the two groups
            parent[root_a] = root_b

