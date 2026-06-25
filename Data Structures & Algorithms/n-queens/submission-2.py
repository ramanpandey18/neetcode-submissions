class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        col_set = set()
        diag1 = set()
        diag2 = set()
        board = [-1] * n

        def backtrack(row):
            if row == n:
                solution = []
                for c in board:
                    solution.append('.' * c + 'Q' + '.' * (n - 1 - c))
                results.append(solution)
                return
            for col in range(n):
                if col in col_set:
                    continue
                if (row - col) in diag1:
                    continue
                if (row + col) in diag2:
                    continue
                
                board[row] = col
                col_set.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)
                col_set.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        backtrack(0)
        return results


        def backtrack(row):
            if row == n:
                solution = []
                for c in board:
                    solution.append('.' * c + 'Q' + '.' * (n - 1- c))
                results.append(solution)
                return
            
            for col in range(n):
                if col in col_set:
                    continue
                if (row - col) in diag1:
                    continue
                if (row + col) in diag2:
                    continue
                board[row] = col
                col_set.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)
                col_set.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        backtrack(0)
        return results

        results = []
        # Track which columns and diagonals are occupied
        col_set  = set()
        diag1    = set()   # top-left → bottom-right  (row - col is constant)
        diag2    = set()   # top-right → bottom-left  (row + col is constant)

        board = [-1] * n   # board[row] = column where queen is placed

        def backtrack(row):
            # Base case: all n rows filled → valid solution
            if row == n:
                # Convert board to the required string format
                solution = []
                for c in board:
                    solution.append('.' * c + 'Q' + '.' * (n - 1 - c))
                results.append(solution)
                return

            for col in range(n):
                # Skip if this column or diagonal is already under attack
                if col in col_set:       continue
                if (row - col) in diag1: continue
                if (row + col) in diag2: continue

                # Place the queen
                board[row] = col
                col_set.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)   # recurse to next row

                # Remove the queen (backtrack)
                col_set.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return results
        