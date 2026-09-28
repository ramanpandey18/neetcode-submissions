class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        nr < 0 or nr >= ROWS or
                        nc < 0 or nc >= COLS or
                        (nr, nc) in visited or
                        heights[nr][nc] < heights[r][c]
                    ):
                        continue

                    visited.add((nr, nc))
                    queue.append((nr, nc))

        # Pacific: top row + left column
        pacific_queue = deque()

        for r in range(ROWS):
            pacific.add((r, 0))
            pacific_queue.append((r, 0))

        for c in range(COLS):
            pacific.add((0, c))
            pacific_queue.append((0, c))

        bfs(pacific_queue, pacific)

        # Atlantic: bottom row + right column
        atlantic_queue = deque()

        for r in range(ROWS):
            atlantic.add((r, COLS - 1))
            atlantic_queue.append((r, COLS - 1))

        for c in range(COLS):
            atlantic.add((ROWS - 1, c))
            atlantic_queue.append((ROWS - 1, c))

        bfs(atlantic_queue, atlantic)

        # Cells that can reach BOTH oceans
        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result
        