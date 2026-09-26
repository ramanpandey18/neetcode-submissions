class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base cases: out of bounds or water
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return
            
            # Mark current land as visited by turning it into water
            grid[r][c] = '0'
            
            # Explore all 4 directions
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)
        
        return island_count
