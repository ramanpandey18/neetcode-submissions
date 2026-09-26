class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col, idx):
            # Base case: all characters matched
            if idx == len(word):
                return True

            # Out of bounds or wrong character or already visited
            if (row < 0 or row >= ROWS or
                col < 0 or col >= COLS or
                board[row][col] != word[idx] or
                board[row][col] == '#'):
                return False

            # Mark cell as visited
            temp = board[row][col]
            board[row][col] = '#'

            # Explore all 4 directions for next character
            found = (dfs(row - 1, col, idx + 1) or   # up
                    dfs(row  + 1, col, idx + 1) or   # down
                    dfs(row, col - 1, idx + 1) or   # left
                    dfs(row, col + 1, idx + 1))     # right

            # Backtrack — restore the cell
            board[row][col] = temp

            return found

        # Try every cell as a starting point
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False