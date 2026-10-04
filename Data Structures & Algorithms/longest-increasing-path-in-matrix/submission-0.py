class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(r, c):
            # Already calculated this cell
            if (r, c) in memo:
                return memo[(r, c)]

            # At minimum, the path contains the current cell
            length = 1

            # Four possible directions
            directions = [
                (-1, 0),  # up
                (1, 0),   # down
                (0, -1),  # left
                (0, 1)    # right
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries
                if 0 <= nr < rows and 0 <= nc < cols:

                    # We can only move to a strictly larger value
                    if matrix[nr][nc] > matrix[r][c]:

                        length = max(
                            length,
                            1 + dfs(nr, nc)
                        )

            # Store result for this cell
            memo[(r, c)] = length

            return length

        answer = 0

        # Try starting the path from every cell
        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))

        return answer
        