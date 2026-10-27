class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Rotting Oranges: We need to count how many minutes pass. Each BFS level represents one minute, so we use for _ in range(len(queue)).
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh = 0
        minutes  = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue and fresh > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nr >= ROWS
                        or nc < 0 or nc >= COLS or
                        grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        return minutes if fresh == 0 else -1
                       