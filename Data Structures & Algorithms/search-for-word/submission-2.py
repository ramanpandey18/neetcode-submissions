class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
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