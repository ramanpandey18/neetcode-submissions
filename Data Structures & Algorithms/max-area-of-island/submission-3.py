class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] == 0):
                return 0
            grid[row][col] = 0
            area = 1
            area += dfs(row - 1, col) # up
            area += dfs(row + 1, col) # down
            area += dfs(row, col - 1) # left
            area += dfs(row, col + 1) # right
            return area
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_area = dfs(r, c)
                    max_area = max(max_area, curr_area)
        
        dfs(0, 0)

        return max_area
