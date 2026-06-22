class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid or not grid[0]:
        #     return 0
    
        # rows, cols = len(grid), len(grid[0])
        # island_count = 0
        
        # def dfs(r, c):
        #     # Base cases: out of bounds or water
        #     if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
        #         return
            
        #     # Mark current land as visited by turning it into water
        #     grid[r][c] = '0'
            
        #     # Explore all 4 directions
        #     dfs(r + 1, c)  # down
        #     dfs(r - 1, c)  # up
        #     dfs(r, c + 1)  # right
        #     dfs(r, c - 1)  # left
        
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == '1':
        #             island_count += 1
        #             dfs(i, j)
        
        # return island_count

        if not grid or not grid[0]:
            return 0
        rows , cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    island_count += 1
                    dfs(i, j)
        return island_count