"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if not intervals:
        #     return 0
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)

        return len(min_heap)


        # Sweep Line Algorithm
        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))
        events.sort(key = lambda x: (x[0], x[1]))
        current_rooms = 0
        max_rooms = 0
        for time, delta in events:
            current_rooms += delta
            max_rooms = max(max_rooms, current_rooms)
        return max_rooms
