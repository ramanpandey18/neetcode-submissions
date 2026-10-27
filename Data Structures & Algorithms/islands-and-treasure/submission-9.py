class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr < 0 or nr >= ROWS
                    or nc < 0 or nc >= COLS
                    or grid[nr][nc] != 2147483647):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))


# Add all treasure cells (0) to the queue initially.
# Remove one cell from the queue using popleft().
# Explore its four neighbors: up, down, left, and right.
# If a neighbor contains INF (2147483647), update it to the current cell's distance + 1.
# Add that neighbor to the queue so we can explore its neighbors later.
# Continue until the queue is empty.















        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        # Put all treasure cells into queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    grid[nr][nc] != 2147483647):
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))
