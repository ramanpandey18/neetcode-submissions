class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(row, col, idx):
            if idx == len(word):
                return True

            if (row < 0 or row >= ROWS or 
                col < 0 or col >= COLS or 
                board[row][col] != word[idx] or 
                board[row][col] == "#"):
                return False
            
            temp = board[row][col]
            board[row][col] = "#"
            #up down left right
            found = (backtrack(row - 1, col, idx + 1) or
                    backtrack(row + 1, col, idx + 1) or
                    backtrack(row, col - 1, idx + 1) or
                    backtrack(row, col + 1, idx + 1))
                
            board[row][col] = temp
            return found

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0):
                    return True
        return False


        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            # Base case: all characters matched
            if idx == len(word):
                return True

            # Out of bounds or wrong character or already visited
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx] or
                board[r][c] == '#'):
                return False

            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all 4 directions for next character
            found = (dfs(r + 1, c, idx + 1) or   # down
                    dfs(r - 1, c, idx + 1) or   # up
                    dfs(r, c + 1, idx + 1) or   # right
                    dfs(r, c - 1, idx + 1))     # left

            # Backtrack — restore the cell
            board[r][c] = temp

            return found

        # Try every cell as a starting point
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False