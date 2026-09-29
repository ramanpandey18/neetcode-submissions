import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # visited set to avoid revisiting the same cell multiple times
        visited = set()

        # Min-heap stores tuples: (water_level_required, row, col)
        # We start at (0,0). The minimum water level to even stand here
        # is grid[0][0] itself.
        min_heap = [(grid[0][0], 0, 0)]
        visited.add((0, 0))

        # 4 possible directions to move: right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while min_heap:
            # Pop the cell that currently needs the SMALLEST water level
            # (this is the greedy/Dijkstra step - always expand the cheapest option)
            water_level, row, col = heapq.heappop(min_heap)

            # If we've reached the bottom-right cell, we're done.
            # Because of the min-heap, this is guaranteed to be the minimum
            # possible water level to reach here.
            if row == n - 1 and col == n - 1:
                return water_level

            # Explore all 4 neighbors
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # Check bounds and make sure we haven't visited this cell yet
                if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))

                    # The water level needed to extend the path to this neighbor
                    # is the max of:
                    #   - the water level already required so far (water_level)
                    #   - this neighbor's own elevation (grid[new_row][new_col])
                    # because both must be submerged/reachable.
                    new_water_level = max(water_level, grid[new_row][new_col])

                    heapq.heappush(min_heap, (new_water_level, new_row, new_col))

        # Problem guarantees a path always exists, so we should never reach here.
        return -1

        