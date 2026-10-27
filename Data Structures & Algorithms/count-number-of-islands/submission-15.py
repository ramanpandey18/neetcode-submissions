class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        def dfs(r, c):
            if (r < 0 or r >= ROWS 
                or c < 0 or c >= COLS
                or grid[r][c] == '0'):
                return 0
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)
        return islands
        