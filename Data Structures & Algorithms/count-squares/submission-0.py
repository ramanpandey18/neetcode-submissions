from collections import defaultdict

class CountSquares:

    def __init__(self):
        # freq[(x, y)] = how many times this point has been added
        self.freq = defaultdict(int)
        # pts_by_x[x] = set of all y values seen at this x
        # used to iterate candidate diagonal points efficiently
        self.pts_by_x = defaultdict(set)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.freq[(x, y)] += 1
        self.pts_by_x[x].add(y)

    def count(self, point: list[int]) -> int:
        x1, y1 = point
        total = 0

        # Iterate every point that shares the same x-column as the query.
        # Each such point is a candidate for corner A = (x1, y2).
        for y2 in self.pts_by_x[x1]:
            if y2 == y1:
                continue          # same row → can't form a square (side = 0)

            side = abs(y2 - y1)  # the square's side length

            # Try both squares: one to the right, one to the left
            for x2 in [x1 + side, x1 - side]:
                # D = (x2, y2)  — diagonal from query point Q=(x1,y1)
                # B = (x2, y1)  — the fourth corner
                # count(D) * count(B) * count(A) where A=(x1,y2) is already
                # confirmed to exist (we're iterating over pts_by_x[x1])
                total += (self.freq[(x1, y2)] *
                          self.freq[(x2, y2)] *
                          self.freq[(x2, y1)])

        return total