class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col):
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                grid[row][col] == '0'):
                return
            
            grid[row][col] = '0'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        dfs(0, 0)
        return islands
        
        