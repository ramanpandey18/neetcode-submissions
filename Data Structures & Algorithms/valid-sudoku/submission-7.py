class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows    = {0: {"5", "3", "7"}, 1: {"6", "1", "9", "5"}, ...}
        # cols    = {0: {"5", "6", "8"}, 1: {"3", "9"}, ...}
        # squares = {(0, 0): {"5", "3", "6", "9", "8"}, (0, 1): {"7", "1", "9", "5"}, ...}
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
