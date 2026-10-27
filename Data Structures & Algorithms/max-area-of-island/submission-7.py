class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0
        def dfs(r, c):
            if (r < 0 or r >= ROWS 
                or c < 0 or c >= COLS
                or grid[r][c] == 0):
                return 0
            grid[r][c] = 0
            area = 1
            area += dfs(r - 1, c)
            area += dfs(r + 1, c)
            area += dfs(r, c - 1)
            area += dfs(r, c + 1)
            return area

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    curr_area = dfs(row, col)
                    max_area = max(max_area, curr_area)
        return max_area
        