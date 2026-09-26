class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    island_area = dfs(i, j)
                    max_area = max(max_area, island_area)
        return max_area
