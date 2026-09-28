class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque

class Solution:
    def solve(self, board):
        # Original O
        #     ↓
        # Is it connected to boundary?
        #     ↓
        # YES
        #     ↓
        #     O → S
        #     ↓
        # BFS finds other connected O's
        #     ↓
        #     O → S
        #     ↓
        # BFS finished
        #     ↓
        # Remaining O's = surrounded
        #     ↓
        # Remaining O → X
        #     ↓
        # S → O
        #     ↓
        # Final board
        ROWS = len(board)
        COLS = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        
        # Find all O's on the boundary
        for r in range(ROWS):
            if board[r][0] == "O":
                queue.append((r, 0))
                board[r][0] = "S"

            if board[r][COLS - 1] == "O": 
                queue.append((r, COLS - 1))
                board[r][COLS - 1] = "S"

        for c in range(COLS):
            if board[0][c] == "O":
                queue.append((0, c))
                board[0][c] = "S"

            if board[ROWS - 1][c] == "O": 
                queue.append((ROWS - 1, c))
                board[ROWS - 1][c] = "S"

        # BFS from boundary O's
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc 
                if (
                    nr < 0  or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    board[nr][nc] != "O"):
                    continue
                board[nr][nc] = "S"
                queue.append((nr, nc))   

        # Capture remaining O's
        # Restore safe S's back to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
